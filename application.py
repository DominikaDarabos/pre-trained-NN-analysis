#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QPushButton, QTextBrowser,QVBoxLayout,  QLabel, QFrame, QGridLayout, QHBoxLayout, QCheckBox, QRadioButton, QLineEdit, QGraphicsScene, QApplication, QGraphicsView, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QSize, QCoreApplication
from utils import main, new_model, create_new_figure
import sys, os, re
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import h5py
import importlib.util
import io
import innvestigate

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from Project import Project
from Figure import Figure_
tf.compat.v1.disable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

activations = {
    "None": "all",
    "Index": "index",
    "Max activation": "max_activation"
}


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

class NewModelDialog(QtWidgets.QDialog, new_model.Ui_Dialog):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.activateWindow()
        self.app = main
        self.project = Project()
        self.createButton.clicked.connect(self.create_project)
        self.selectModelButton.clicked.connect(self.select_model_dialog)
        self.selectCustomButton.clicked.connect(self.select_custom_dialog)
        self.selectInputButton.clicked.connect(self.select_input_dialog)

    # Slot to show the main window
    def create_project(self):
        self.hide()  # Hide the dialog
        #self.main_window.showMaximized()  # Show the main window
        self.app.set_shadow_effect(enabled=False)
        self.collect_selected_analyzers()
        self.app.add_project(self.project)
        self.app.load_start_window()
    
    def select_model_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select model", "", "All Files (*)", options=options)
        if file:
            self.project.set_model_file(file)
            self.selectModelLine.setText(file)
    
    def select_custom_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select custom object file", "", "All Files (*)", options=options)
        if file:
            self.project.set_custom_file(file)
            self.selectCustomLine.setText(file)
    
    def select_input_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select input", "", "All Files (*)", options=options)
        if file:
            self.project.set_input_file(file)
            self.selectInputLine.setText(file)
    
    def collect_selected_analyzers(self):
        # Get checked state of checkboxes
        self.project.config["analyzers"]["IG"]["checked"]            = self.checkBox_IG.isChecked()
        self.project.config["analyzers"]["LRP_Z"]["checked"]         = self.checkBox_LRP_Z.isChecked()
        self.project.config["analyzers"]["LRP_AB"]["checked"]        = self.checkBox_LRP_AB.isChecked()
        self.project.config["analyzers"]["LRP_Epsilon"]["checked"]   = self.checkBox_LRP_Epsilon.isChecked()

        self.project.config["analyzers"]["IG"]["activation"]             = activations[self.comboBox_IG.currentText()]
        self.project.config["analyzers"]["LRP_Z"]["activation"]          = activations[self.comboBox_LRP_Z.currentText()]
        self.project.config["analyzers"]["LRP_AB"]["activation"]         = activations[self.comboBox_LRP_AB.currentText()]
        self.project.config["analyzers"]["LRP_Epsilon"]["activation"]    = activations[self.comboBox_LRP_Epsilon.currentText()]

        alphaBetaString = self.AlphaBetaComboBox.currentText()
        numbers_as_strings = re.findall(r'\d+', alphaBetaString)
        numbers_as_integers = [int(num_str) for num_str in numbers_as_strings]
        self.project.config["analyzers"]["LRP_AB"]["alpha"] = numbers_as_integers[0]
        self.project.config["analyzers"]["LRP_AB"]["beta"] = numbers_as_integers[1]
        eps_input = self.EpsilonInput.text()
        if eps_input.isnumeric():
            self.project.config["analyzers"]["LRP_Epsilon"]["epsilon"] = float(self.EpsilonInput.text())
        else:
            #TODO: pop up error window
            self.project.config["analyzers"]["LRP_Epsilon"]["checked"] = False

class NewFigureDialog(QtWidgets.QDialog, create_new_figure.Ui_Dialog):
    def __init__(self, main, project, place, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.activateWindow()
        self.app = main
        self.project = project
        self.place = place
        self.plotTypeCombo.currentIndexChanged.connect(self.on_combobox_selection_change)
        self.createButton.clicked.connect(self.create_figure)

    def on_combobox_selection_change(self):
        selected_option = self.plotTypeCombo.currentText()

        if selected_option == "Comparison":
            self.setup_widgets_for_comparison()
        elif selected_option == "Distribution":
            self.setup_widgets_for_distribution()
    
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            if child.layout():
                self.clear_layout(child.layout())
    
    def clear_frame(self, frame):
        layout = frame.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_frame(frame)
    
    def create_figure(self):
        figure = Figure_()
        figure.config["class"] = self.classCombo.currentText().lower()
        figure.config["prediction_quality"] = self.predQualCombo.currentText().lower().replace(" ", "_")
        if self.plotTypeCombo.currentText() == "Comparison":
            figure.add_default_comparison()
            if self.singleSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"] = self.singleAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"] = self.singleSampleLineRadio_2.isChecked()
            if self.averageSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"] = self.averageSampleScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"] = self.averageSampleLineRadio_2.isChecked()
            if self.singleAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["scatter"] = self.singleAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["line"] = self.singleAnalyzerLineRadio_2.isChecked()
            if self.averageAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] = self.averageAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] = self.averageAnalyzerLineRadio_2.isChecked()
        elif self.plotTypeCombo.currentText() == "Distribution":
            figure.add_default_distribution()
            if self.boxRadio.isChecked():
                figure.config["plot_type"]["distribution"]["box_plot"]["avtivated"] = True
                if self.numOfBinsInput.text().isnumeric():
                    figure.config["plot_type"]["distribution"]["box_plot"]["num_of_bins"] = int(self.numOfBinsInput.text())
                else:
                    figure.config["plot_type"]["distribution"]["box_plot"]["num_of_bins"] = 30
            if self.histRadio.isChecked():
                figure.config["plot_type"]["distribution"]["histogram"]["avtivated"] = True
                if self.AnalyzerCheckbow.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["show_all_class"] = self.analyzerRadio.isChecked()
                if self.inputCheckbox.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["show_all_class"] = self.inputRadio.isChecked()
        
        if self.place == 0:
            self.app.create_new_upper_comparison_figure(figure)
        elif self.place == 1:
            self.app.create_new_bottom_comparison_figure(figure)
        self.accept()


    def setup_widgets_for_comparison(self):
        # Clear the layout if it's not empty
        self.clear_frame(self.baseFrame_2)

        self.channelsFrame = QFrame(self.baseFrame_2)
        self.channelsFrame.setObjectName(u"channelsFrame")
        self.channelsFrame.setFrameShape(QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.channelsFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.channelsTitle = QLabel(self.channelsFrame)
        self.channelsTitle.setObjectName(u"channelsTitle")
        self.channelsTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_3.addWidget(self.channelsTitle, 0, 0, 1, 1)
        self.singleSampleCheckbox = QCheckBox(self.channelsFrame)
        self.singleSampleCheckbox.setObjectName(u"singleSampleCheckbox")
        self.gridLayout_3.addWidget(self.singleSampleCheckbox, 1, 0, 1, 1)
        self.averageSampleCheckbox = QCheckBox(self.channelsFrame)
        self.averageSampleCheckbox.setObjectName(u"averageSampleCheckbox")
        self.gridLayout_3.addWidget(self.averageSampleCheckbox, 2, 0, 1, 1)
        self.singleAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.singleAnalyzerCheckbox.setObjectName(u"singleAnalyzerCheckbox")
        self.gridLayout_3.addWidget(self.singleAnalyzerCheckbox, 3, 0, 1, 1)
        self.averageAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.averageAnalyzerCheckbox.setObjectName(u"averageAnalyzerCheckbox")
        self.gridLayout_3.addWidget(self.averageAnalyzerCheckbox, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.channelsFrame, 0, 0, 1, 1)
        self.radioFrame = QFrame(self.baseFrame_2)
        self.radioFrame.setObjectName(u"radioFrame")
        self.radioFrame.setFrameShape(QFrame.StyledPanel)
        self.radioFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.radioFrame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.averageSampleFrame = QFrame(self.radioFrame)
        self.averageSampleFrame.setObjectName(u"averageSampleFrame")
        self.averageSampleFrame.setFrameShape(QFrame.StyledPanel)
        self.averageSampleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.averageSampleFrame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.singleAnalyzerLineRadio_2 = QRadioButton(self.averageSampleFrame)
        self.singleAnalyzerLineRadio_2.setObjectName(u"singleAnalyzerLineRadio_2")
        self.gridLayout_8.addWidget(self.singleAnalyzerLineRadio_2, 0, 0, 1, 1)
        self.singleAnalyzerScatterRadio_2 = QRadioButton(self.averageSampleFrame)
        self.singleAnalyzerScatterRadio_2.setObjectName(u"singleAnalyzerScatterRadio_2")
        self.gridLayout_8.addWidget(self.singleAnalyzerScatterRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageSampleFrame, 2, 0, 1, 1)
        self.singleAnalyzerFrame = QFrame(self.radioFrame)
        self.singleAnalyzerFrame.setObjectName(u"singleAnalyzerFrame")
        self.singleAnalyzerFrame.setFrameShape(QFrame.StyledPanel)
        self.singleAnalyzerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.singleAnalyzerFrame)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.averageAnalyzerScatterRadio_2 = QRadioButton(self.singleAnalyzerFrame)
        self.averageAnalyzerScatterRadio_2.setObjectName(u"averageAnalyzerScatterRadio_2")
        self.gridLayout_9.addWidget(self.averageAnalyzerScatterRadio_2, 0, 0, 1, 1)
        self.averageAnalyzerLineRadio_2 = QRadioButton(self.singleAnalyzerFrame)
        self.averageAnalyzerLineRadio_2.setObjectName(u"averageAnalyzerLineRadio_2")
        self.gridLayout_9.addWidget(self.averageAnalyzerLineRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.singleAnalyzerFrame, 3, 0, 1, 1)
        self.singleSampleFrame = QFrame(self.radioFrame)
        self.singleSampleFrame.setObjectName(u"singleSampleFrame")
        self.singleSampleFrame.setFrameShape(QFrame.StyledPanel)
        self.singleSampleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.singleSampleFrame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.singleSampleLineRadio_2 = QRadioButton(self.singleSampleFrame)
        self.singleSampleLineRadio_2.setObjectName(u"singleSampleLineRadio_2")
        self.gridLayout_7.addWidget(self.singleSampleLineRadio_2, 0, 0, 1, 1)
        self.singleSampleScatterRadio_2 = QRadioButton(self.singleSampleFrame)
        self.singleSampleScatterRadio_2.setObjectName(u"singleSampleScatterRadio_2")
        self.gridLayout_7.addWidget(self.singleSampleScatterRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.singleSampleFrame, 1, 0, 1, 1)
        self.labelFrame = QFrame(self.radioFrame)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.labelFrame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scatterTitle_2 = QLabel(self.labelFrame)
        self.scatterTitle_2.setObjectName(u"scatterTitle_2")
        self.scatterTitle_2.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.scatterTitle_2, 0, 0, 1, 1)
        self.linetitle_2 = QLabel(self.labelFrame)
        self.linetitle_2.setObjectName(u"linetitle_2")
        self.linetitle_2.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.linetitle_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.labelFrame, 0, 0, 1, 1)
        self.averageAnalyzerFrame = QFrame(self.radioFrame)
        self.averageAnalyzerFrame.setObjectName(u"averageAnalyzerFrame")
        self.averageAnalyzerFrame.setFrameShape(QFrame.StyledPanel)
        self.averageAnalyzerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.averageAnalyzerFrame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.averageSampleLineRadio_2 = QRadioButton(self.averageAnalyzerFrame)
        self.averageSampleLineRadio_2.setObjectName(u"averageSampleLineRadio_2")
        self.gridLayout_10.addWidget(self.averageSampleLineRadio_2, 0, 0, 1, 1)
        self.averageSampleScatterRadio_2 = QRadioButton(self.averageAnalyzerFrame)
        self.averageSampleScatterRadio_2.setObjectName(u"averageSampleScatterRadio_2")
        self.gridLayout_10.addWidget(self.averageSampleScatterRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageAnalyzerFrame, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.radioFrame, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)



        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Average sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Average analyzer score", None))
        self.singleAnalyzerLineRadio_2.setText("")
        self.singleAnalyzerScatterRadio_2.setText("")
        self.averageAnalyzerScatterRadio_2.setText("")
        self.averageAnalyzerLineRadio_2.setText("")
        self.singleSampleLineRadio_2.setText("")
        self.singleSampleScatterRadio_2.setText("")
        self.scatterTitle_2.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.linetitle_2.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.averageSampleLineRadio_2.setText("")
        self.averageSampleScatterRadio_2.setText("")
    
    def setup_widgets_for_distribution(self):
        self.clear_frame(self.baseFrame_2)
    
        self.figureTypeTitle = QLabel(self.baseFrame_2)
        self.figureTypeTitle.setObjectName(u"figureTypeTitle")
        self.figureTypeTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_2.addWidget(self.figureTypeTitle, 0, 0, 1, 1)
        self.boxFrame = QFrame(self.baseFrame_2)
        self.boxFrame.setObjectName(u"boxFrame")
        self.boxFrame.setFrameShape(QFrame.StyledPanel)
        self.boxFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.boxFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.boxRadio = QRadioButton(self.boxFrame)
        self.boxRadio.setObjectName(u"boxRadio")
        self.gridLayout_6.addWidget(self.boxRadio, 0, 0, 1, 1)
        self.numOfBinsInput = QLineEdit(self.boxFrame)
        self.numOfBinsInput.setObjectName(u"numOfBinsInput")
        self.gridLayout_6.addWidget(self.numOfBinsInput, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.boxFrame, 1, 0, 1, 1)
        self.histFrame = QFrame(self.baseFrame_2)
        self.histFrame.setObjectName(u"histFrame")
        self.histFrame.setFrameShape(QFrame.StyledPanel)
        self.histFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.histFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.histRadio = QRadioButton(self.histFrame)
        self.histRadio.setObjectName(u"histRadio")
        self.gridLayout_3.addWidget(self.histRadio, 0, 0, 1, 1)
        self.histDetailesFrame = QFrame(self.histFrame)
        self.histDetailesFrame.setObjectName(u"histDetailesFrame")
        self.histDetailesFrame.setFrameShape(QFrame.StyledPanel)
        self.histDetailesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.histDetailesFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.AnalyzerCheckbow = QCheckBox(self.histDetailesFrame)
        self.AnalyzerCheckbow.setObjectName(u"AnalyzerCheckbow")
        self.gridLayout_5.addWidget(self.AnalyzerCheckbow, 0, 0, 1, 1)
        self.analyzerRadio = QRadioButton(self.histDetailesFrame)
        self.analyzerRadio.setObjectName(u"analyzerRadio")
        self.gridLayout_5.addWidget(self.analyzerRadio, 0, 1, 1, 1)
        self.inputCheckbox = QCheckBox(self.histDetailesFrame)
        self.inputCheckbox.setObjectName(u"inputCheckbox")
        self.gridLayout_5.addWidget(self.inputCheckbox, 1, 0, 1, 1)
        self.inputRadio = QRadioButton(self.histDetailesFrame)
        self.inputRadio.setObjectName(u"inputRadio")
        self.gridLayout_5.addWidget(self.inputRadio, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.histDetailesFrame, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.histFrame, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)

        self.figureTypeTitle.setText(QCoreApplication.translate("Dialog", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("Dialog", u"Box plot", None))
        self.numOfBinsInput.setText(QCoreApplication.translate("Dialog", u"Number of bins", None))
        self.histRadio.setText(QCoreApplication.translate("Dialog", u"Histogram", None))
        self.AnalyzerCheckbow.setText(QCoreApplication.translate("Dialog", u"Analyzer relevance scores", None))
        self.analyzerRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.inputCheckbox.setText(QCoreApplication.translate("Dialog", u"Input", None))
        self.inputRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MainApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()