#!/usr/bin/env python3
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTextBrowser,QVBoxLayout, QFrame, QGridLayout, QCheckBox, QGraphicsView, QWidget
from PySide6.QtCore import QSize, QCoreApplication
from utils import main
import sys, os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import h5py
import importlib.util
import io
import innvestigate

from NewModelDialog import NewModelDialog
from NewFigureDialog import NewFigureDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from Figure import Figure_
tf.compat.v1.disable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def apply_stylesheet(app):
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    # Construct the full path to the QSS file
    qss_path = os.path.join(script_dir, "qss", "MacOS.qss")
    print(qss_path)
    style_file = QtCore.QFile(qss_path)
    if style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
        stream = QtCore.QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        style_file.close()


class MainApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        # open in full screen
        self.showMaximized()
        self.setWindowTitle("Analyzer application")
        self.effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.set_shadow_effect(enabled=True)
        self.projects = []

        self.upper_new_plot_button.clicked.connect(self.show_create_figure_dialog)
        self.bottom_new_plot_button.clicked.connect(self.show_create_figure_dialog)

    # add elements to side menu bar
    def populate_list_widget(self):
        sideMenuElements = [analyzer for analyzer, values in self.projects[0].config["analyzers"].items() if values["checked"]]
        self.listWidget.addItems(sideMenuElements)
        print(self.projects[0].config)

        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None
    
    def load_files(self):
        if os.path.isfile(self.projects[0].custom_object_file_path):
            file_path = self.projects[0].custom_object_file_path
            splitted_path = file_path.split("/")
            class_name = splitted_path[-1].split(".")[0]

            module_dir = "/".join(splitted_path[:-1])
            sys.path.append(module_dir)

            module_name = class_name
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            my_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(my_module)

            my_class = getattr(my_module, class_name)
            custom_objects = {} 
            custom_objects[class_name] = my_class

            print("Successfully loaded custom object file")
        if os.path.isfile(self.projects[0].model_file_path):
            self.projects[0].model = tf.keras.models.load_model(self.projects[0].model_file_path, custom_objects=custom_objects)
            self.projects[0].model_wo_softmax = innvestigate.model_wo_softmax(self.projects[0].model)
            print("Successfully loaded model file")
        if os.path.isfile(self.projects[0].input_file_path):
            with h5py.File(self.projects[0].input_file_path, 'r') as hf:
                self.projects[0].test_x = hf['test_x'][:]
                self.projects[0].test_y = hf['test_y'][:]
            print("Successfully loaded input file")

    def set_shadow_effect(self, enabled=True):
        if enabled:
            self.effect.setEnabled(True)
            self.effect.setOpacity(0.2)
            self.setGraphicsEffect(self.effect)
        else:
            self.effect.setEnabled(False)

    def add_project(self, project):
        self.projects.append(project)
    
    def on_sidemenu_clicked(self, item):
        self.upperPlotTabWidget.clear()
        self.bottomPlotTabWidget.clear()
        analyzer = str(self.listWidget.currentItem().text())
        upperPlotCount = self.projects[0].config["analyzers"][analyzer]["upper_plot_count"]
        for tab_idx in range(upperPlotCount):
            upperPlot = self.projects[0].config["analyzers"][analyzer]["upper_tabs"][f"tab_{tab_idx}"]
            self.upperPlotTabWidget.addTab(upperPlot, f"Tab {tab_idx + 1}")
            self.load_plot("upper", tab_idx)
        bottomPlotCount = self.projects[0].config["analyzers"][analyzer]["bottom_plot_count"]
        for tab_idx in range(bottomPlotCount):
            bottomPlot = self.projects[0].config["analyzers"][analyzer]["bottom_tabs"][f"tab_{tab_idx}"]
            self.bottomPlotTabWidget.addTab(bottomPlot, f"Tab {tab_idx + 1}")
            self.load_plot("bottom", tab_idx)
    
    def load_start_window(self):
        self.populate_list_widget()
        self.load_files()
        self.populate_analyzers()
        self.inputDataInfo.clear()
        self.inputDataInfo.append(f"Shape: {self.projects[0].test_x.shape}")
        self.inputDataInfo.append(f"Type: {type(self.projects[0].test_x)}")
        self.inputDataInfo.append(f"First element:\n{self.projects[0].test_x[:1]}")
        self.inputDataInfo.append("---")
        #self.inputDataInfo.append(str(self.projects[0].config["analyzers"]["LRP_Z"]["analyzer"].analyze(self.projects[0].test_x)))

        self.outputDataInfo.clear()
        self.outputDataInfo.append(f"Shape: {self.projects[0].test_y.shape}")
        self.outputDataInfo.append(f"Type: {type(self.projects[0].test_y)}")
        self.outputDataInfo.append(f"First five element:\n{self.projects[0].test_y[:5]}")
        self.outputDataInfo.append("---")
        self.listWidget.setCurrentRow(0)
        self.listWidget.itemClicked.connect(self.on_sidemenu_clicked)

        sys.stdout = io.StringIO()

        # Get the model summary
        self.projects[0].model.summary()

        # Get the captured output
        model_summary = sys.stdout.getvalue()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Append the model summary to self.modelInfo
        self.modelInfo.clear()
        self.modelInfo.append(model_summary)
    
    def show_create_figure_dialog(self):
        sender_button = self.sender()
        if sender_button == self.upper_new_plot_button:
            qt_dialog = NewFigureDialog(self, self.projects[0], place = 0)
            qt_dialog.exec_()
        elif sender_button == self.bottom_new_plot_button:
            qt_dialog = NewFigureDialog(self, self.projects[0], place = 1)
            qt_dialog.exec_()
    
    def populate_analyzers(self):
        ### create IG ###
        if self.projects[0].config["analyzers"]["IG"]["checked"]:
            self.projects[0].config["analyzers"]["IG"]["analyzer"] = \
                innvestigate.create_analyzer("integrated_gradients", self.projects[0].model_wo_softmax,\
                neuron_selection_mode=self.projects[0].config["analyzers"]["IG"]["activation"],\
                reference_inputs=0, steps = 64)
        ### create LRP_Z
        if self.projects[0].config["analyzers"]["LRP_Z"]["checked"]:
            self.projects[0].config["analyzers"]["LRP_Z"]["analyzer"] = \
                innvestigate.create_analyzer("lrp.z", self.projects[0].model, disable_model_checks=True,\
                neuron_selection_mode=self.projects[0].config["analyzers"]["LRP_Z"]["activation"])
        ### create LRP_EPSILON ###
        if self.projects[0].config["analyzers"]["LRP_Epsilon"]["checked"]:
            self.projects[0].config["analyzers"]["LRP_Epsilon"]["analyzer"] = \
                innvestigate.create_analyzer("lrp.epsilon", self.projects[0].model,\
                disable_model_checks=True, neuron_selection_mode=self.projects[0].config["analyzers"]["LRP_Epsilon"]["activation"],\
                **{"epsilon": self.projects[0].config["analyzers"]["LRP_Epsilon"]["epsilon"]})
        if self.projects[0].config["analyzers"]["LRP_AB"]["checked"]:
            if self.projects[0].config["analyzers"]["LRP_AB"]["alpha"] == 1 and self.projects[0].config["analyzers"]["LRP_AB"]["beta"] == 0:
                self.projects[0].config["analyzers"]["LRP_AB"]["analyzer"] = \
                    innvestigate.create_analyzer("lrp.alpha_1_beta_0", self.projects[0].model,\
                    disable_model_checks=True, neuron_selection_mode=self.projects[0].config["analyzers"]["LRP_AB"]["activation"])
            if self.projects[0].config["analyzers"]["LRP_AB"]["alpha"] == 2 and self.projects[0].config["analyzers"]["LRP_AB"]["beta"] == 1:
                self.projects[0].config["analyzers"]["LRP_AB"]["analyzer"] = \
                    innvestigate.create_analyzer("lrp.alpha_2_beta_1", self.projects[0].model,\
                    disable_model_checks=True, neuron_selection_mode=self.projects[0].config["analyzers"]["LRP_AB"]["activation"])

    def create_new_upper_comparison_figure(self, figure):
        analyzer = str(self.listWidget.currentItem().text())
        upperPlotCount = self.projects[0].config["analyzers"][analyzer]["upper_plot_count"]

        upperPlotTab = QWidget()
        upperPlotTab.setObjectName(f"upperPlotTab_{upperPlotCount}")
        gridLayout_3 = QGridLayout(upperPlotTab)
        gridLayout_3.setObjectName(u"gridLayout_3")
        upperFigureInfoFrame = QFrame(upperPlotTab)
        upperFigureInfoFrame.setObjectName(f"upperFigureInfoFrame_{upperPlotCount}")
        upperFigureInfoFrame.setMinimumSize(QSize(100, 0))
        upperFigureInfoFrame.setMaximumSize(QSize(200, 16777215))
        upperFigureInfoFrame.setFrameShape(QFrame.StyledPanel)
        upperFigureInfoFrame.setFrameShadow(QFrame.Raised)
        gridLayout_5 = QGridLayout(upperFigureInfoFrame)
        gridLayout_5.setSpacing(0)
        gridLayout_5.setObjectName(u"gridLayout_5")
        gridLayout_5.setContentsMargins(0, 0, 0, 0)
        upperFigureAttributes = QTextBrowser(upperFigureInfoFrame)
        upperFigureAttributes.setObjectName(f"upperFigureAttributes_{upperPlotCount}")
        upperFigureAttributes.setMinimumSize(QSize(100, 100))
        upperFigureAttributes.setMaximumSize(QSize(200, 250))
        gridLayout_5.addWidget(upperFigureAttributes, 0, 0, 1, 1)
        upperChannelsFrame = QFrame(upperFigureInfoFrame)
        upperChannelsFrame.setObjectName(f"upperChannelsFrame_{upperPlotCount}")
        upperChannelsFrame.setMinimumSize(QSize(100, 100))
        upperChannelsFrame.setMaximumSize(QSize(200, 250))
        upperChannelsFrame.setFrameShape(QFrame.StyledPanel)
        upperChannelsFrame.setFrameShadow(QFrame.Raised)
        verticalLayout_3 = QVBoxLayout(upperChannelsFrame)
        verticalLayout_3.setObjectName(u"verticalLayout_3")
        UpperPlot_Channel_1 = QCheckBox(upperChannelsFrame)
        UpperPlot_Channel_1.setObjectName(f"UpperPlot_{upperPlotCount}_Channel_1")
        verticalLayout_3.addWidget(UpperPlot_Channel_1)
        UpperPlot_Channel_2 = QCheckBox(upperChannelsFrame)
        UpperPlot_Channel_2.setObjectName(f"UpperPlot_{upperPlotCount}_Channel_2")
        verticalLayout_3.addWidget(UpperPlot_Channel_2)
        UpperPlot_Channel_3 = QCheckBox(upperChannelsFrame)
        UpperPlot_Channel_3.setObjectName(f"UpperPlot_{upperPlotCount}_Channel_3")
        verticalLayout_3.addWidget(UpperPlot_Channel_3)
        UpperPlot_Channel_4 = QCheckBox(upperChannelsFrame)
        UpperPlot_Channel_4.setObjectName(f"UpperPlot_{upperPlotCount}_Channel_4")
        verticalLayout_3.addWidget(UpperPlot_Channel_4)
        gridLayout_5.addWidget(upperChannelsFrame, 1, 0, 1, 1)
        gridLayout_3.addWidget(upperFigureInfoFrame, 0, 2, 1, 1)
        upperPlot = QGraphicsView(upperPlotTab)
        upperPlot.setObjectName(f"upperPlot_{upperPlotCount}")
        upperPlot.setMinimumSize(QSize(400, 0))
        gridLayout_3.addWidget(upperPlot, 0, 1, 1, 1)
        UpperPlot_Channel_1.setText(QCoreApplication.translate("MainWindow", u"Channel_1", None))
        UpperPlot_Channel_2.setText(QCoreApplication.translate("MainWindow", u"Channel_2", None))
        UpperPlot_Channel_3.setText(QCoreApplication.translate("MainWindow", u"Channel_3", None))
        UpperPlot_Channel_4.setText(QCoreApplication.translate("MainWindow", u"Channel_4", None))
        self.upperPlotTabWidget.addTab(upperPlotTab, f"Tab {upperPlotCount + 1}")
        self.projects[0].config["analyzers"][analyzer]["upper_tabs"][f"tab_{upperPlotCount}"] = upperPlotTab
        self.load_plot("upper", upperPlotCount)
        self.projects[0].increase_upper_plot_count(analyzer)

    def create_new_bottom_comparison_figure(self, figure):
        analyzer = str(self.listWidget.currentItem().text())
        bottomPlotCount = self.projects[0].config["analyzers"][analyzer]["bottom_plot_count"]
        bottomPlotTab = QWidget()
        bottomPlotTab.setObjectName(f"bottomPlotTab_{bottomPlotCount}")
        gridLayout_3 = QGridLayout(bottomPlotTab)
        gridLayout_3.setObjectName(u"gridLayout_3")
        bottomFigureInfoFrame = QFrame(bottomPlotTab)
        bottomFigureInfoFrame.setObjectName(f"bottomFigureInfoFrame_{bottomPlotCount}")
        bottomFigureInfoFrame.setMinimumSize(QSize(100, 0))
        bottomFigureInfoFrame.setMaximumSize(QSize(200, 16777215))
        bottomFigureInfoFrame.setFrameShape(QFrame.StyledPanel)
        bottomFigureInfoFrame.setFrameShadow(QFrame.Raised)
        gridLayout_5 = QGridLayout(bottomFigureInfoFrame)
        gridLayout_5.setSpacing(0)
        gridLayout_5.setObjectName(u"gridLayout_5")
        gridLayout_5.setContentsMargins(0, 0, 0, 0)
        bottomFigureAttributes = QTextBrowser(bottomFigureInfoFrame)
        bottomFigureAttributes.setObjectName(f"bottomFigureAttributes_{bottomPlotCount}")
        bottomFigureAttributes.setMinimumSize(QSize(100, 100))
        bottomFigureAttributes.setMaximumSize(QSize(200, 250))
        gridLayout_5.addWidget(bottomFigureAttributes, 0, 0, 1, 1)
        bottomChannelsFrame = QFrame(bottomFigureInfoFrame)
        bottomChannelsFrame.setObjectName(f"bottomChannelsFrame_{bottomPlotCount}")
        bottomChannelsFrame.setMinimumSize(QSize(100, 100))
        bottomChannelsFrame.setMaximumSize(QSize(200, 250))
        bottomChannelsFrame.setFrameShape(QFrame.StyledPanel)
        bottomChannelsFrame.setFrameShadow(QFrame.Raised)
        verticalLayout_3 = QVBoxLayout(bottomChannelsFrame)
        verticalLayout_3.setObjectName(u"verticalLayout_3")
        bottomPlot_Channel_1 = QCheckBox(bottomChannelsFrame)
        bottomPlot_Channel_1.setObjectName(f"bottomPlot_{bottomPlotCount}_Channel_1")
        verticalLayout_3.addWidget(bottomPlot_Channel_1)
        bottomPlot_Channel_2 = QCheckBox(bottomChannelsFrame)
        bottomPlot_Channel_2.setObjectName(f"bottomPlot_{bottomPlotCount}_Channel_2")
        verticalLayout_3.addWidget(bottomPlot_Channel_2)
        bottomPlot_Channel_3 = QCheckBox(bottomChannelsFrame)
        bottomPlot_Channel_3.setObjectName(f"bottomPlot_{bottomPlotCount}_Channel_3")
        verticalLayout_3.addWidget(bottomPlot_Channel_3)
        bottomPlot_Channel_4 = QCheckBox(bottomChannelsFrame)
        bottomPlot_Channel_4.setObjectName(f"bottomPlot_{bottomPlotCount}_Channel_4")
        verticalLayout_3.addWidget(bottomPlot_Channel_4)
        gridLayout_5.addWidget(bottomChannelsFrame, 1, 0, 1, 1)
        gridLayout_3.addWidget(bottomFigureInfoFrame, 0, 2, 1, 1)
        bottomPlot = QGraphicsView(bottomPlotTab)
        bottomPlot.setObjectName(f"bottomPlot_{bottomPlotCount}")
        bottomPlot.setMinimumSize(QSize(400, 0))
        gridLayout_3.addWidget(bottomPlot, 0, 1, 1, 1)
        bottomPlot_Channel_1.setText(QCoreApplication.translate("MainWindow", u"Channel_1", None))
        bottomPlot_Channel_2.setText(QCoreApplication.translate("MainWindow", u"Channel_2", None))
        bottomPlot_Channel_3.setText(QCoreApplication.translate("MainWindow", u"Channel_3", None))
        bottomPlot_Channel_4.setText(QCoreApplication.translate("MainWindow", u"Channel_4", None))
        self.bottomPlotTabWidget.addTab(bottomPlotTab, f"Tab {bottomPlotCount + 1}")
        self.projects[0].config["analyzers"][analyzer]["bottom_tabs"][f"tab_{bottomPlotCount}"] = bottomPlotTab


        self.load_plot("bottom", bottomPlotCount)
        self.projects[0].increase_bottom_plot_count(analyzer)

    def load_plot(self, position, tab_number):
        analyzer = str(self.listWidget.currentItem().text())
        #plotCount = self.projects[0].config["analyzers"][analyzer][f"{position}_plot_count"]
        current_tab = self.projects[0].config["analyzers"][analyzer][f"{position}_tabs"].get(f"tab_{tab_number}")
        if current_tab:
            scene = QtWidgets.QGraphicsScene()
            current_plot = current_tab.findChild(QtWidgets.QGraphicsView, f"{position}Plot_{tab_number}")
            if current_plot:
                current_plot.setScene(scene)
            else:
                print(f"{position}Plot_{tab_number} not found")

        figure = Figure(figsize=(4, 3), dpi=100)
        axes = figure.gca()

        x = np.linspace(1, 10)
        y = np.linspace(1, 10)
        y1 = np.linspace(11, 20)
        axes.plot(x, y, "-k", label="first one")
        axes.plot(x, y1, "-b", label="second one")
        axes.legend()
        axes.grid(True)

        canvas = FigureCanvas(figure)
        scene.addWidget(canvas)
        current_plot.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MainApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()