from PySide6 import QtWidgets
from utils import new_model
from Project import Project
import re, os, sys
from Analyzer import Analyzer
import h5py
import importlib.util
import innvestigate
import tensorflow as tf
from ErrorDialog import ErrorDialog

activations = {
    "None": "all",
    "Max activation": "max_activation"
}

class NewModelDialog(QtWidgets.QDialog, new_model.Ui_Dialog):
    def __init__(self, main, purpose=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app = main
        self.project = Project()
        if purpose == "project":
            self.add_input_frame()
            self.selectModelButton.clicked.connect(self.select_model_dialog)
            self.selectCustomButton.clicked.connect(self.select_custom_dialog)
            self.selectInputButton.clicked.connect(self.select_input_dialog)
        self.add_analyzer_frame()
        self.add_create_button()
        self.createButton.clicked.connect(self.create_project)
        self.errorLog = []

    def close_window(self):
        self.close()

    def create_project(self):
        """
        Checks if the input files and the selections are correct, and starts the main window or show an error dialog accordingly.
        """
        self.errorLog = []
        self.check_input_files()
        self.collect_selected_analyzers()
        self.load_model_files()
        if len(self.errorLog) > 0:
            error_dialog = ErrorDialog(self.errorLog)
            error_dialog.exec()
            return
        self.app.project = self.project
        self.app.load_start_window()
        self.accept()
    
    def create_analyzers(self):
        """
        Checks if the the selections are correct, and load the additional analyzers or show an error dialog accordingly.
        """
        self.errorLog = []
        self.collect_selected_analyzers()
        if len(self.errorLog) > 0:
            error_dialog = ErrorDialog(self.errorLog)
            error_dialog.exec()
            return
        for name, analyzer in self.project.analyzers.items():
            if self.app.create_analyzer(name, analyzer):
                self.app.project.analyzers[name] = analyzer
        self.app.populate_list_widget()
        self.app.listWidget.setCurrentRow(len(self.app.project.analyzers)-1)
        self.app.update_main_tab()
        self.accept()
    
    def select_model_dialog(self):
        """
        Check and load model file selection.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select model", "", "All Files (*)", options=options)
        if file:
            self.project.set_model_file(file)
            self.selectModelLine.setText(file)
    
    def select_custom_dialog(self):
        """
        Check and load custom file selection.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select custom object file", "", "All Files (*)", options=options)
        if file:
            self.project.set_custom_file(file)
            self.selectCustomLine.setText(file)
    
    def select_input_dialog(self):
        """
        Check and load input file selection.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select input", "", "All Files (*)", options=options)
        if file:
            self.project.set_input_file(file)
            self.selectInputLine.setText(file)
            self.load_input_file()

    def collect_selected_analyzers(self):
        """
        Gather the selected information on the poll from the analyzers.
        """
        self.project.analyzers = {}
        if self.checkBox_IG.isChecked():
            try:
                ref = int(self.referenceLine.text())
                step = int(self.stepLine.text())
                name = f"IG - {self.comboBox_IG.currentText()} - {ref} - {step}"
                self.project.analyzers[name] = Analyzer(reference_input = ref, steps = step)
                self.project.analyzers[name].activation = activations[self.comboBox_IG.currentText()]
            except:
                self.errorLog.append("<font color='red'>Integrated gradient's reference and step value have to be numbers.</font>")
        if self.checkBox_LRP_Z.isChecked():
            name = f"LRP_Z - {self.comboBox_LRP_Z.currentText()}"
            if self.comboBox_LRP_Z.currentText().startswith("Index"):
                self.project.analyzers[name] = Analyzer(neuron = int(self.comboBox_LRP_Z.currentText().split(" ")[-1]))
                self.project.analyzers[name].activation = "index"
            else:
                self.project.analyzers[name] = Analyzer()
                self.project.analyzers[name].activation = activations[self.comboBox_LRP_Z.currentText()]
        if self.checkBox_LRP_AB.isChecked():
            alphaBetaString = self.AlphaBetaComboBox.currentText()
            numbers_as_strings = re.findall(r'\d+', alphaBetaString)
            numbers_as_integers = [int(num_str) for num_str in numbers_as_strings]
            name = f"LRP_AB - {self.comboBox_LRP_AB.currentText()} - {numbers_as_integers[0]} - {numbers_as_integers[1]}"
            if self.comboBox_LRP_AB.currentText().startswith("Index"):
                self.project.analyzers[name] =  Analyzer(alpha = numbers_as_integers[0], beta = numbers_as_integers[1],\
                                                              neuron = int(self.comboBox_LRP_AB.currentText().split(" ")[-1]))
                self.project.analyzers[name].activation = "index"
            else:
                self.project.analyzers[name] =  Analyzer(alpha = numbers_as_integers[0], beta = numbers_as_integers[1])
                self.project.analyzers[name].activation = activations[self.comboBox_LRP_AB.currentText()]
        if self.checkBox_LRP_Epsilon.isChecked():
            try:
                eps = float(self.EpsilonInput.text())
                name = f"LRP_Epsilon - {self.comboBox_LRP_Epsilon.currentText()} - {eps}"
                if self.comboBox_LRP_Epsilon.currentText().startswith("Index"):
                    self.project.analyzers[name] = Analyzer(epsilon = eps, neuron = int(self.comboBox_LRP_Epsilon.currentText().split(" ")[-1]))
                    self.project.analyzers[name].activation = "index"
                else:
                    self.project.analyzers[name] = Analyzer(epsilon = eps)
                    self.project.analyzers[name].activation = activations[self.comboBox_LRP_Epsilon.currentText()]
            except:
                self.errorLog.append("<font color='red'>Epsilon value must be a number.</font>")  
    
    def load_model_files(self):
        """
        Load the trained model and the custom class from the files. 
        """
        if os.path.isfile(self.project.custom_object_file_path):
            try:
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

            except Exception as err:
                self.errorLog.append(f"<font color='red'>Error during loading custom file: {err}</font>")
        else:
            custom_objects = {}
        if os.path.isfile(self.project.model_file_path):
            try:
                self.project.model = tf.keras.models.load_model(self.project.model_file_path, custom_objects=custom_objects)
                self.project.model_wo_softmax = innvestigate.model_wo_softmax(self.project.model)
            except Exception as err:
                self.errorLog.append(f"<font color='red'>Error during loading model file: {err}</font>")

        if self.project.test_x is not None:
            self.project.predictions = self.project.model.predict(self.project.test_x, verbose = 2)
        else:
            self.errorLog.append("<font color='red'>Input file is not loaded.</font>")
    
    def load_input_file(self):
        """
        Load the input from file.
        """
        if self.project.input_file_path == "" and os.path.isfile(self.selectInputLine.text()):
            self.project.input_file_path = self.selectInputLine.text()
        if os.path.isfile(self.project.input_file_path):
            try:
                with h5py.File(self.project.input_file_path, 'r') as hf:
                    self.project.test_x = hf['test_x'][:]
                    self.project.test_y = hf['test_y'][:]
                    self.project.number_of_classes = self.project.test_y.shape[1]
            except Exception as err:
                self.selectInputLine.setText(f"<font color='red'>Error in loading {self.project.input_file_path} : {err}.</font>")
                return
            for possible_class_num in range(self.project.test_y.shape[1]):
                self.comboBox_LRP_Z.addItem(f"Index {possible_class_num}")
                self.comboBox_LRP_AB.addItem(f"Index {possible_class_num}")
                self.comboBox_LRP_Epsilon.addItem(f"Index {possible_class_num}")

    def check_input_files(self):
        """
        Checks and gather errors from the file input lines.
        """
        if self.selectModelLine.text() == "Select model":
            self.errorLog.append("<font color='red'>Model file is not selected.</font>")
        elif not os.path.isfile(self.selectModelLine.text()):
            self.errorLog.append("<font color='red'>Model file does not exits.</font>")
        elif self.project.model_file_path == "" and os.path.isfile(self.selectModelLine.text()):
            self.project.model_file_path = self.selectModelLine.text()
        elif not os.path.isfile(self.project.model_file_path) and os.path.isfile(self.selectModelLine.text()):
            self.project.model_file_path = self.selectModelLine.text()

        if self.project.custom_object_file_path == "" and os.path.isfile(self.selectCustomLine.text()):
            self.project.custom_object_file_path = self.selectCustomLine.text()
        elif not os.path.isfile(self.project.custom_object_file_path) and os.path.isfile(self.selectCustomLine.text()):
            self.project.custom_object_file_path = self.selectCustomLine.text()
        
        if self.selectInputLine.text() == "Select input file":
            self.errorLog.append("<font color='red'>Input file is not selected.</font>")
        elif not os.path.isfile(self.selectInputLine.text()):
            self.errorLog.append("<font color='red'>Input file does not exits.</font>")
        elif self.project.input_file_path == "" and os.path.isfile(self.selectInputLine.text()):
            self.project.input_file_path = self.selectInputLine.text()
            self.load_input_file()
        elif not os.path.isfile(self.project.input_file_path) and os.path.isfile(self.selectInputLine.text()):
            self.project.input_file_path = self.selectInputLine.text()
        if self.selectInputLine.text().startswith("Error in loading"):
            self.errorLog.append("<font color='red'>Error in loading input file</font>")

            

            