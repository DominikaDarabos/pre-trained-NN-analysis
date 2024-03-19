from PySide6 import QtWidgets
from utils import main, new_model
from Project import Project
import re

activations = {
    "None": "all",
    "Index": "index",
    "Max activation": "max_activation"
}

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