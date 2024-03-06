#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QPushButton, QLabel, QFrame, QGridLayout, QCheckBox, QRadioButton, QLineEdit
from PySide6.QtCore import QSize, QCoreApplication
from utils import main, new_model, create_new_figure
import sys, os, re
import tensorflow as tf
import h5py
import importlib.util
import io
import innvestigate
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
        first_row_text = self.inputDataInfo.toPlainText().split('---')[0]
        self.inputDataInfo.clear()
        self.inputDataInfo.append(first_row_text)
        self.inputDataInfo.append('---')
        self.inputDataInfo.append(item.text())
    
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
        qt_dialog = NewFigureDialog(self.projects[0])
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
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.activateWindow()
        self.app = main
        self.project = project
        self.plotTypeCombo.currentIndexChanged.connect(self.on_combobox_selection_change)

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

    def setup_widgets_for_comparison(self):
        # Clear the layout if it's not empty
        self.clear_frame(self.baseFrame_2)

        self.channelsFrame = QFrame(self.baseFrame_2)
        self.channelsFrame.setObjectName(u"channelsFrame")
        self.channelsFrame.setFrameShape(QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.channelsFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.scatterFrame = QFrame(self.baseFrame_2)
        self.scatterFrame.setObjectName(u"scatterFrame")
        self.scatterFrame.setFrameShape(QFrame.StyledPanel)
        self.scatterFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.scatterFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scatterTitle = QLabel(self.scatterFrame)
        self.scatterTitle.setObjectName(u"scatterTitle")
        self.scatterTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4.addWidget(self.scatterTitle, 0, 0, 1, 1)
        self.singleSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.singleSampleScatterRadio.setObjectName(u"singleSampleScatterRadio")
        self.gridLayout_4.addWidget(self.singleSampleScatterRadio, 1, 0, 1, 1)
        self.averageSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.averageSampleScatterRadio.setObjectName(u"averageSampleScatterRadio")
        self.gridLayout_4.addWidget(self.averageSampleScatterRadio, 2, 0, 1, 1)
        self.singleAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.singleAnalyzerScatterRadio.setObjectName(u"singleAnalyzerScatterRadio")
        self.gridLayout_4.addWidget(self.singleAnalyzerScatterRadio, 3, 0, 1, 1)
        self.averageAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.averageAnalyzerScatterRadio.setObjectName(u"averageAnalyzerScatterRadio")
        self.gridLayout_4.addWidget(self.averageAnalyzerScatterRadio, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.scatterFrame, 0, 1, 1, 1)
        self.LineFrame = QFrame(self.baseFrame_2)
        self.LineFrame.setObjectName(u"LineFrame")
        self.LineFrame.setFrameShape(QFrame.StyledPanel)
        self.LineFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.LineFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.linetitle = QLabel(self.LineFrame)
        self.linetitle.setObjectName(u"linetitle")
        self.linetitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.linetitle, 0, 0, 1, 1)
        self.singleSampleLineRadio = QRadioButton(self.LineFrame)
        self.singleSampleLineRadio.setObjectName(u"singleSampleLineRadio")
        self.gridLayout_5.addWidget(self.singleSampleLineRadio, 1, 0, 1, 1)
        self.averageSampleLineRadio = QRadioButton(self.LineFrame)
        self.averageSampleLineRadio.setObjectName(u"averageSampleLineRadio")
        self.gridLayout_5.addWidget(self.averageSampleLineRadio, 2, 0, 1, 1)
        self.singleAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.singleAnalyzerLineRadio.setObjectName(u"singleAnalyzerLineRadio")
        self.gridLayout_5.addWidget(self.singleAnalyzerLineRadio, 3, 0, 1, 1)
        self.averageAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.averageAnalyzerLineRadio.setObjectName(u"averageAnalyzerLineRadio")
        self.gridLayout_5.addWidget(self.averageAnalyzerLineRadio, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.LineFrame, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)



        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Avarage sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Avarage analyzer score", None))
        self.scatterTitle.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.singleSampleScatterRadio.setText("")
        self.averageSampleScatterRadio.setText("")
        self.singleAnalyzerScatterRadio.setText("")
        self.averageAnalyzerScatterRadio.setText("")
        self.linetitle.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.singleSampleLineRadio.setText("")
        self.averageSampleLineRadio.setText("")
        self.singleAnalyzerLineRadio.setText("")
        self.averageAnalyzerLineRadio.setText("")
    
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
class Project():
    def __init__(self):
        #TODO: until testing
        self.model_file_path = "C:/Users/dominika/vpnet/trained_models/full_keras_model.h5"
        self.custom_object_file_path = "C:/Users/dominika/vpnet/tensorflow/VPLayer.py"
        self.input_file_path = "C:/Users/dominika/vpnet/tensorflow/synhermite_test_data.h5"
        self.model = None
        self.model_wo_softmax = None
        self.test_x = None
        self.test_y = None
        self.config = {
            "analyzers": {
                "IG": {
                    "checked": False,
                    "activation": None,
                    "analyzer": None
                },
                "LRP_Z": {
                    "checked": False,
                    "activation": None,
                    "analyzer": None
                },
                "LRP_AB": {
                    "checked": False,
                    "activation": None,
                    "alpa": False,
                    "beta": None,
                    "analyzer": None
                },
                "LRP_Epsilon": {
                    "checked": False,
                    "activation": None,
                    "epsilon": None,
                    "analyzer": None
                }
            }
        }

    def set_model_file(self, path):
        self.model_file_path = path

    def set_input_file(self, path):
        self.input_file_path = path

    def set_custom_file(self, path):
        self.custom_object_file_path = path

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MainApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()