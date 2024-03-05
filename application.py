#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore
from utils import main, new_model
import sys, os, re
import tensorflow as tf
import h5py
import importlib.util
import io


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
        self.inputDataInfo.clear()
        self.inputDataInfo.append(f"Shape: {self.projects[0].test_x.shape}")
        self.inputDataInfo.append(f"Type: {type(self.projects[0].test_x)}")
        self.inputDataInfo.append(f"First element:\n{self.projects[0].test_x[:1]}")
        self.inputDataInfo.append("---")

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




class NewModelDialog(QtWidgets.QDialog):
    def __init__(self, main,  parent=None):
        super().__init__(parent)
        self.ui = new_model.Ui_Dialog()
        self.ui.setupUi(self)
        self.activateWindow()
        self.app = main
        self.project = Project()
        self.ui.createButton.clicked.connect(self.create_project)
        self.ui.selectModelButton.clicked.connect(self.select_model_dialog)
        self.ui.selectCustomButton.clicked.connect(self.select_custom_dialog)
        self.ui.selectInputButton.clicked.connect(self.select_input_dialog)

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
            self.ui.selectModelLine.setText(file)
    
    def select_custom_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select custom object file", "", "All Files (*)", options=options)
        if file:
            self.project.set_custom_file(file)
            self.ui.selectCustomLine.setText(file)
    
    def select_input_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select input", "", "All Files (*)", options=options)
        if file:
            self.project.set_input_file(file)
            self.ui.selectInputLine.setText(file)
    
    def collect_selected_analyzers(self):
        # Get checked state of checkboxes
        self.project.config["analyzers"]["IG"]["checked"]            = self.ui.checkBox_IG.isChecked()
        self.project.config["analyzers"]["LRP_Z"]["checked"]         = self.ui.checkBox_LRP_Z.isChecked()
        self.project.config["analyzers"]["LRP_AB"]["checked"]        = self.ui.checkBox_LRP_AB.isChecked()
        self.project.config["analyzers"]["LRP_Epsilon"]["checked"]   = self.ui.checkBox_LRP_Epsilon.isChecked()

        self.project.config["analyzers"]["IG"]["activation"]             = self.ui.comboBox_IG.currentText()
        self.project.config["analyzers"]["LRP_Z"]["activation"]          = self.ui.comboBox_LRP_Z.currentText()
        self.project.config["analyzers"]["LRP_AB"]["activation"]         = self.ui.comboBox_LRP_AB.currentText()
        self.project.config["analyzers"]["LRP_Epsilon"]["activation"]    = self.ui.comboBox_LRP_Epsilon.currentText()

        alphaBetaString = self.ui.AlphaBetaComboBox.currentText()
        numbers_as_strings = re.findall(r'\d+', alphaBetaString)
        numbers_as_integers = [int(num_str) for num_str in numbers_as_strings]
        self.project.config["analyzers"]["LRP_AB"]["alpha"] = numbers_as_integers[0]
        self.project.config["analyzers"]["LRP_AB"]["beta"] = numbers_as_integers[1]
        eps_input = self.ui.EpsilonInput.text()
        if eps_input != "":
            if eps_input.isnumeric():
                self.project.config["analyzers"]["LRP_Epsilon"]["epsilon"] = float(self.ui.EpsilonInput.text())
            else:
                #TODO: pop up error window
                self.project.config["analyzers"]["LRP_Epsilon"]["checked"] = False


class Project():
    def __init__(self):
        #TODO: until testing
        self.model_file_path = "C:/Users/dominika/vpnet/trained_models/full_keras_model.h5"
        self.custom_object_file_path = "C:/Users/dominika/vpnet/tensorflow/VPLayer.py"
        self.input_file_path = "C:/Users/dominika/vpnet/tensorflow/synhermite_test_data.h5"
        self.model = None
        self.test_x = None
        self.test_y = None
        self.config = {
            "files":{
                "model_path": "",
                "custom_object_path": "",
                "data_path": ""
            },
            "analyzers": {
                "IG": {
                    "checked": False,
                    "activation": None
                },
                "LRP_Z": {
                    "checked": False,
                    "activation": None
                },
                "LRP_AB": {
                    "checked": False,
                    "activation": None,
                    "alpa": False,
                    "beta": None
                },
                "LRP_Epsilon": {
                    "checked": False,
                    "activation": None,
                    "epsilon": None
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