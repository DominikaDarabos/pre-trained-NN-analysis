#!/usr/bin/env python3
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTextBrowser,QVBoxLayout, QFrame, QGridLayout, QCheckBox, QGraphicsView, QWidget
from PySide6.QtCore import QSize, QCoreApplication, Qt
from utils import main
import sys, os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import h5py
import importlib.util
import io
import innvestigate
from PySide6.QtWidgets import QSizePolicy

from NewModelDialog import NewModelDialog
from NewFigureDialog import NewFigureDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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
        #self.set_shadow_effect(enabled=True)
        self.project = None
        self.active_upper_plot = None
        self.active_bottom_plot = None
        self.changedTab = None

        self.upper_new_plot_button.clicked.connect(self.show_create_figure_dialog)
        self.bottom_new_plot_button.clicked.connect(self.show_create_figure_dialog)
        self.upperPlotTabWidget.currentChanged.connect(self.upper_tab_changed)
        self.bottomPlotTabWidget.currentChanged.connect(self.bottom_tab_changed)

    def get_current_analyzer(self):
        return str(self.listWidget.currentItem().text())
    
    def upper_tab_changed(self, index):
        self.active_upper_plot = index
        self.changedTab = 0
    
    def bottom_tab_changed(self, index):
        self.active_bottom_plot = index
        self.changedTab = 1

    # add elements to side menu bar
    def populate_list_widget(self):
        sideMenuElements = [analyzer for analyzer in self.project.analyzers.keys()]
        self.listWidget.addItems(sideMenuElements)

        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None
    
    def load_files(self):
        if os.path.isfile(self.project.custom_object_file_path):
            file_path = self.project.custom_object_file_path
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
        if os.path.isfile(self.project.model_file_path):
            self.project.model = tf.keras.models.load_model(self.project.model_file_path, custom_objects=custom_objects)
            self.project.model_wo_softmax = innvestigate.model_wo_softmax(self.project.model)
            print("Successfully loaded model file")
        if os.path.isfile(self.project.input_file_path):
            with h5py.File(self.project.input_file_path, 'r') as hf:
                self.project.test_x = hf['test_x'][:]
                self.project.test_y = hf['test_y'][:]
                self.project.predictions = self.project.model.predict(self.project.test_x, verbose = 2)
            self.project.number_of_classes = self.project.test_y.shape[1]
            print("Successfully loaded input file")

    def set_shadow_effect(self, enabled=True):
        if enabled:
            self.effect.setEnabled(True)
            self.effect.setOpacity(0.2)
            self.setGraphicsEffect(self.effect)
        else:
            self.effect.setEnabled(False)
    
    def on_sidemenu_clicked(self, item):
        self.upperPlotTabWidget.clear()
        self.bottomPlotTabWidget.clear()
        analyzer = self.get_current_analyzer()
        upperPlotCount = self.project.analyzers[analyzer].ui_elements_config["upper_plot_count"]
        for tab_idx in range(upperPlotCount):
            upperPlot = self.project.analyzers[analyzer].ui_elements_config["upper_tabs"][f"tab_{tab_idx}"]
            self.upperPlotTabWidget.addTab(upperPlot, f"Tab {tab_idx + 1}")
            self.load_plot("upper", tab_idx)
        bottomPlotCount = self.project.analyzers[analyzer].ui_elements_config["bottom_plot_count"]
        for tab_idx in range(bottomPlotCount):
            bottomPlot = self.project.analyzers[analyzer].ui_elements_config["bottom_tabs"][f"tab_{tab_idx}"]
            self.bottomPlotTabWidget.addTab(bottomPlot, f"Tab {tab_idx + 1}")
            self.load_plot("bottom", tab_idx)
    
    def load_start_window(self):
        self.populate_list_widget()
        self.load_files()
        self.populate_analyzers()
        self.inputDataInfo.clear()
        self.inputDataInfo.append(f"Shape: {self.project.test_x.shape}")
        self.inputDataInfo.append(f"Type: {type(self.project.test_x)}")
        self.inputDataInfo.append(f"First element:\n{self.project.test_x[:1]}")
        self.inputDataInfo.append("---")

        self.outputDataInfo.clear()
        self.outputDataInfo.append(f"Shape: {self.project.test_y.shape}")
        self.outputDataInfo.append(f"Type: {type(self.project.test_y)}")
        self.outputDataInfo.append(f"First five element:\n{self.project.test_y[:5]}")
        self.outputDataInfo.append("---")
        self.listWidget.setCurrentRow(0)
        self.listWidget.itemClicked.connect(self.on_sidemenu_clicked)

        sys.stdout = io.StringIO()

        # Get the model summary
        self.project.model.summary()

        # Get the captured output
        model_summary = sys.stdout.getvalue()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Append the model summary to self.modelInfo
        self.modelInfo.clear()
        self.modelInfo.append(model_summary)
        self.upperPlotFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottomPlotFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Calculate half of the main window height
        half_height = self.height() / 2
        
        # Set the fixed height for the frames
        self.upperPlotFrame.setFixedHeight(half_height)
        self.bottomPlotFrame.setFixedHeight(half_height)
    
    def show_create_figure_dialog(self):
        sender_button = self.sender()
        if sender_button == self.upper_new_plot_button:
            qt_dialog = NewFigureDialog(self, place = 0)
            qt_dialog.exec_()
        elif sender_button == self.bottom_new_plot_button:
            qt_dialog = NewFigureDialog(self, place = 1)
            qt_dialog.exec_()

    def populate_analyzers(self):
        ### create IG ###
        if "IG" in self.project.analyzers:
            self.project.analyzers["IG"].innvestigate_analyzer = \
                innvestigate.create_analyzer("integrated_gradients", self.project.model_wo_softmax,\
                neuron_selection_mode=self.project.analyzers["IG"].activation,\
                reference_inputs= self.project.analyzers["IG"].reference_input, steps = self.project.analyzers["IG"].steps)
            
            self.project.analyzers["IG"].analyzer_output = self.project.analyzers["IG"].innvestigate_analyzer.analyze(self.project.test_x)

        ### create LRP_Z
        if "LRP_Z" in self.project.analyzers:
            self.project.analyzers["LRP_Z"].innvestigate_analyzer = \
                innvestigate.create_analyzer("lrp.z", self.project.model, disable_model_checks=True,\
                neuron_selection_mode=self.project.analyzers["LRP_Z"].activation)

            self.project.analyzers["LRP_Z"].analyzer_output = self.project.analyzers["LRP_Z"].innvestigate_analyzer.analyze(self.project.test_x)

        ### create LRP_EPSILON ###
        if "LRP_Epsilon" in self.project.analyzers:
            self.project.analyzers["LRP_Epsilon"].innvestigate_analyzer = \
                innvestigate.create_analyzer("lrp.epsilon", self.project.model,\
                disable_model_checks=True, neuron_selection_mode=self.project.analyzers["LRP_Epsilon"].activation,\
                **{"epsilon": self.project.analyzers["LRP_Epsilon"].epsilon})

            self.project.analyzers["LRP_Epsilon"].analyzer_output = self.project.analyzers["LRP_Epsilon"].innvestigate_analyzer.analyze(self.project.test_x)

        ### create LRP_AB ###
        if "LRP_AB" in self.project.analyzers:
            if self.project.analyzers["LRP_AB"].alpha == 1 and self.project.analyzers["LRP_AB"].beta == 0:
                self.project.analyzers["LRP_AB"].innvestigate_analyzer = \
                    innvestigate.create_analyzer("lrp.alpha_1_beta_0", self.project.model,\
                    disable_model_checks=True, neuron_selection_mode=self.project.analyzers["LRP_AB"].activation)

                self.project.analyzers["LRP_Z"].analyzer_output = self.project.analyzers["LRP_Z"].innvestigate_analyzer.analyze(self.project.test_x)

            if self.project.analyzers["LRP_AB"].alpha == 2 and self.project.analyzers["LRP_AB"].beta == 1:
                self.project.analyzers["LRP_AB"].innvestigate_analyzer = \
                    innvestigate.create_analyzer("lrp.alpha_2_beta_1", self.project.model,\
                    disable_model_checks=True, neuron_selection_mode=self.project.analyzers["LRP_AB"].activation)

                self.project.analyzers["LRP_AB"].analyzer_output = self.project.analyzers["LRP_AB"].innvestigate_analyzer.analyze(self.project.test_x)

    def checkbox_state_changed(self):
        checked_checkboxes = [checkbox for checkbox in self.checkboxes if checkbox.isChecked()]
        classes = [int(checkbox.objectName().split("_")[-1])-1 for checkbox in checked_checkboxes]
        self.load_plot("upper", self.active_upper_plot, classes = classes)
        analyzer = self.get_current_analyzer()
        plotTab = self.project.analyzers[analyzer].ui_elements_config[f"upper_tabs"][f"tab_{self.active_upper_plot}"]
        figureAttributes = plotTab.findChild(QTextBrowser, f"upperFigureAttributes_{self.active_upper_plot}")
        figureAttributes.append(str(classes))

    def create_new_comparison_figure(self, place, figure):
        analyzer = self.get_current_analyzer()
        plotCount = self.project.analyzers[analyzer].ui_elements_config[f"{place}_plot_count"]

        plotTab = QWidget()
        plotTab.setObjectName(f"{place}PlotTab_{plotCount}")
        gridLayout_3 = QGridLayout(plotTab)
        gridLayout_3.setObjectName(u"gridLayout_3")
        figureInfoFrame = QFrame(plotTab)
        figureInfoFrame.setObjectName(f"{place}FigureInfoFrame_{plotCount}")
        figureInfoFrame.setMinimumSize(QSize(100, 0))
        figureInfoFrame.setMaximumSize(QSize(200, 16777215))
        figureInfoFrame.setFrameShape(QFrame.StyledPanel)
        figureInfoFrame.setFrameShadow(QFrame.Raised)
        gridLayout_5 = QGridLayout(figureInfoFrame)
        gridLayout_5.setSpacing(0)
        gridLayout_5.setObjectName(u"gridLayout_5")
        gridLayout_5.setContentsMargins(0, 0, 0, 0)
        figureAttributes = QTextBrowser(figureInfoFrame)
        figureAttributes.setObjectName(f"{place}FigureAttributes_{plotCount}")
        figureAttributes.setMinimumSize(QSize(100, 100))
        figureAttributes.setMaximumSize(QSize(200, 250))
        gridLayout_5.addWidget(figureAttributes, 0, 0, 1, 1)
        channelsFrame = QFrame(figureInfoFrame)
        channelsFrame.setObjectName(f"{place}ChannelsFrame_{plotCount}")
        channelsFrame.setMinimumSize(QSize(100, 100))
        channelsFrame.setMaximumSize(QSize(200, 250))
        channelsFrame.setFrameShape(QFrame.StyledPanel)
        channelsFrame.setFrameShadow(QFrame.Raised)
        verticalLayout_3 = QVBoxLayout(channelsFrame)
        verticalLayout_3.setObjectName(u"verticalLayout_3")
        if figure.is_comparison():
            plot_Channel_1 = QCheckBox(channelsFrame)
            plot_Channel_1.setObjectName(f"{place}Plot_{plotCount}_Channel_1")
            verticalLayout_3.addWidget(plot_Channel_1)
            plot_Channel_2 = QCheckBox(channelsFrame)
            plot_Channel_2.setObjectName(f"{place}Plot_{plotCount}_Channel_2")
            verticalLayout_3.addWidget(plot_Channel_2)
            plot_Channel_3 = QCheckBox(channelsFrame)
            plot_Channel_3.setObjectName(f"{place}Plot_{plotCount}_Channel_3")
            verticalLayout_3.addWidget(plot_Channel_3)
            plot_Channel_1.setText(QCoreApplication.translate("MainWindow", u"Single sample", None))
            plot_Channel_2.setText(QCoreApplication.translate("MainWindow", u"Average sample", None))
            plot_Channel_3.setText(QCoreApplication.translate("MainWindow", u"Single analyzer", None))
            plot_Channel_4 = QCheckBox(channelsFrame)
            plot_Channel_4.setObjectName(f"{place}Plot_{plotCount}_Channel_4")
            verticalLayout_3.addWidget(plot_Channel_4)
            plot_Channel_4.setText(QCoreApplication.translate("MainWindow", u"Average analyzer", None))
        if figure.is_hist_distribution():
            self.checkboxes = [] 
            for i in range(self.project.number_of_classes):
                checkbox = QCheckBox(channelsFrame)
                checkbox.setObjectName(f"plot_Channel_{i+1}")
                checkbox.setText(QCoreApplication.translate("MainWindow", f"Class {i+1}", None))
                checkbox.stateChanged.connect(self.checkbox_state_changed) 
                verticalLayout_3.addWidget(checkbox)
                self.checkboxes.append(checkbox)
        gridLayout_5.addWidget(channelsFrame, 1, 0, 1, 1)
        gridLayout_3.addWidget(figureInfoFrame, 0, 2, 1, 1)
        plot = QGraphicsView(plotTab)
        plot.setObjectName(f"{place}Plot_{plotCount}")
        plot.setMinimumSize(QSize(400, 0))
        gridLayout_3.addWidget(plot, 0, 1, 1, 1)
        
        if place == "upper":
            self.upperPlotTabWidget.addTab(plotTab, f"Tab {plotCount + 1}")
            self.project.analyzers[analyzer].increase_upper_plot_count()
        if place == "bottom":
            self.bottomPlotTabWidget.addTab(plotTab, f"Tab {plotCount + 1}")
            self.project.analyzers[analyzer].increase_bottom_plot_count()
        self.project.analyzers[analyzer].ui_elements_config[f"{place}_tabs"][f"tab_{plotCount}"] = plotTab

        self.load_plot(place, plotCount)


    def load_plot(self, position, tab_number, classes = None):
        analyzer = self.get_current_analyzer()
        current_tab = self.project.analyzers[analyzer].ui_elements_config[f"{position}_tabs"].get(f"tab_{tab_number}")
        if current_tab:
            scene = QtWidgets.QGraphicsScene()
            current_plot = current_tab.findChild(QtWidgets.QGraphicsView, f"{position}Plot_{tab_number}")
            if current_plot:
                current_plot.setScene(scene)
            else:
                print(f"{position}Plot_{tab_number} not found")
        print("len:" , len(self.project.analyzers[analyzer].ui_elements_config[f"{position}_figures"]), tab_number)
        figure = self.project.analyzers[analyzer].ui_elements_config[f"{position}_figures"][tab_number]
        if "distribution" in figure.config["plot_type"] and figure.config["plot_type"]["distribution"]["histogram"]["activated"]:
            fig = figure.plot_relevance_score_distribution(self.project, analyzer, classes = classes)
        elif "distribution" in figure.config["plot_type"] and figure.config["plot_type"]["distribution"]["box_plot"]["activated"]:
            fig = figure.plot_grouped_boxplot(self.project, analyzer)
        elif "comparison" in figure.config["plot_type"]:
            fig = figure.plot_comparison(self.project, analyzer)
        else:
            fig = plt.figure()
            axes = fig.gca()

            x = np.linspace(1, 10)
            y = np.linspace(1, 10)
            y1 = np.linspace(11, 20)
            axes.plot(x, y, "-k", label="first one")
            axes.plot(x, y1, "-b", label="second one")
            axes.legend()
            axes.grid(True)

        canvas = FigureCanvas(fig)
        scene.addWidget(canvas)
        current_plot.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MainApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.setWindowFlags(qt_dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()