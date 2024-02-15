#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore

from utils import main, new_model
import sys, os, re

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

class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        # open in full screen
        self.showMaximized()

        self.setWindowTitle("Analyzer application")
        self.effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.set_shadow_effect(enabled=True)

        self.projects = {}

    # add elements to side menu bar
    def populate_list_widget(self):
        sideMenuElements = [analyzer for analyzer, values in self.projects["first"].config["analyzers"].items() if values["checked"]]
        self.listWidget.addItems(sideMenuElements)
        print(self.projects["first"].config)

    def set_shadow_effect(self, enabled=True):
        if enabled:
            self.effect.setEnabled(True)
            self.effect.setOpacity(0.2)
            self.setGraphicsEffect(self.effect)
        else:
            self.effect.setEnabled(False)

    def add_project(self, project, name):
        self.projects[name] = project
        #


class NewModelDialog(QtWidgets.QDialog):
    def __init__(self, main,  parent=None):
        super().__init__(parent)
        self.ui = new_model.Ui_Dialog()
        self.ui.setupUi(self)
        self.activateWindow()
        self.app = main
        self.ui.createButton.clicked.connect(self.create_project)
        self.ui.selectModelButton.clicked.connect(self.select_model_dialog)
        self.ui.selectCustomButton.clicked.connect(self.select_custom_dialog)
        self.ui.selectInputButton.clicked.connect(self.select_input_dialog)

        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None

        self.checkbox_states = {}
        self.combo_box_values = {}

    # Slot to show the main window
    def create_project(self):
        self.hide()  # Hide the dialog
        #self.main_window.showMaximized()  # Show the main window
        self.app.set_shadow_effect(enabled=False)
        project = Project()
        self.collect_selected_analyzers(project)

        self.app.add_project(project, "first")
        self.app.populate_list_widget()
        
    
    def select_model_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select model", "", "All Files (*)", options=options)
        if file:
            self.model_file_path = file
            self.ui.selectModelLine.setText(file)
    
    def select_custom_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select custom object file", "", "All Files (*)", options=options)
        if file:
            self.custom_object_file_path = file
            self.ui.selectCustomLine.setText(file)
    
    def select_input_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select input", "", "All Files (*)", options=options)
        if file:
            self.input_file_path = file
            self.ui.selectInputLine.setText(file)
    
    def collect_selected_analyzers(self, project):
        project.set_model_file = self.model_file_path
        project.set_custom_file = self.custom_object_file_path
        project.set_input_file = self.input_file_path

        # Get checked state of checkboxes
        project.config["analyzers"]["IG"]["checked"]            = self.ui.checkBox_IG.isChecked()
        project.config["analyzers"]["LRP_Z"]["checked"]         = self.ui.checkBox_LRP_Z.isChecked()
        project.config["analyzers"]["LRP_AB"]["checked"]        = self.ui.checkBox_LRP_AB.isChecked()
        project.config["analyzers"]["LRP_Epsilon"]["checked"]   = self.ui.checkBox_LRP_Epsilon.isChecked()

        project.config["analyzers"]["IG"]["activation"]             = self.ui.comboBox_IG.currentText()
        project.config["analyzers"]["LRP_Z"]["activation"]          = self.ui.comboBox_LRP_Z.currentText()
        project.config["analyzers"]["LRP_AB"]["activation"]         = self.ui.comboBox_LRP_AB.currentText()
        project.config["analyzers"]["LRP_Epsilon"]["activation"]    = self.ui.comboBox_LRP_Epsilon.currentText()

        alphaBetaString = self.ui.AlphaBetaComboBox.currentText()
        numbers_as_strings = re.findall(r'\d+', alphaBetaString)
        numbers_as_integers = [int(num_str) for num_str in numbers_as_strings]
        project.config["analyzers"]["LRP_AB"]["alpha"] = numbers_as_integers[0]
        project.config["analyzers"]["LRP_AB"]["beta"] = numbers_as_integers[1]

        project.config["analyzers"]["LRP_Epsilon"]["epsilon"] = float(self.ui.EpsilonInput.text())


class Project():
    def __init__(self):
        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None
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
        self.config["files"]["model_path"] = path

    def set_input_file(self, path):
        self.config["files"]["data_path"] = path

    def set_custom_file(self, path):
        self.config["files"]["custom_object_path"] = path

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MyQtApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()