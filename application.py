#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore

from utils import main, new_model
import sys, os

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
        sideMenuElements = [analyzer for analyzer, boolean in self.projects["first"].checkbox_states.items() if boolean]
        self.listWidget.addItems(sideMenuElements)

    def set_shadow_effect(self, enabled=True):
        if enabled:
            self.effect.setEnabled(True)
            self.effect.setOpacity(0.2)
            self.setGraphicsEffect(self.effect)
        else:
            self.effect.setEnabled(False)

    def add_project(self, project, name):
        self.projects[name] = project


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
        self.collect_selected_analyzers()
        project = Project()
        project.set_model_file = self.model_file_path
        project.set_custom_file = self.custom_object_file_path
        project.set_input_file = self.input_file_path
        project.checkbox_states = self.checkbox_states
        project.combo_box_values = self.combo_box_values

        self.app.add_project(project, "first")
        print(self.app.projects["first"].checkbox_states)
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
    
    def collect_selected_analyzers(self):
        # Get checked state of checkboxes
        self.checkbox_states = {
            "IG": self.ui.checkBox_IG.isChecked(),
            "LRP_Z": self.ui.checkBox_LRP_Z.isChecked(),
            "LRP_AB": self.ui.checkBox_LRP_AB.isChecked(),
            "LRP_Epsilon": self.ui.checkBox_LRP_Epsilon.isChecked()
        }

        # Get selected items from combo boxes
        self.combo_box_values = {
            "IG": self.ui.comboBox_IG.currentText(),
            "LRP_Z": self.ui.comboBox_LRP_Z.currentText(),
            "LRP_AB": self.ui.comboBox_LRP_AB.currentText(),
            "LRP_Epsilon": self.ui.comboBox_LRP_Epsilon.currentText()
        }

        print("Checkbox states:", self.checkbox_states)
        print("Combo box values:", self.combo_box_values)

class Project():
    def __init__(self):
        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None
        self.checkbox_states = {}
        self.combo_box_values = {}

    def set_model_file(self, path):
        self.model_file_path = path

    def set_input_file(self, path):
        self.input_file_path = path

    def set_custom_file(self, path):
        self.model_custom_path = path

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    apply_stylesheet(app)
    qt_app = MyQtApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()