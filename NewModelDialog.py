from PySide6 import QtWidgets
from utils import main, new_model
from Project import Project
import re, os, sys
from Analyzer import Analyzer
import h5py
import importlib.util
import innvestigate
import tensorflow as tf

activations = {
    "None": "all",
    "Max activation": "max_activation"
}

class NewModelDialog(QtWidgets.QDialog, new_model.Ui_Dialog):
    def __init__(self, main, purpose=None, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.activateWindow()
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
        #TODO:
        self.load_input_file()

    # Slot to show the main window
    def create_project(self):
        #self.main_window.showMaximized()  # Show the main window
        #self.app.set_shadow_effect(enabled=False)
        self.collect_selected_analyzers()
        self.load_model_files()
        self.app.project = self.project
        self.app.load_start_window()
        self.hide()  # Hide the dialog
    
    def create_analyzers(self):
        self.collect_selected_analyzers()
        for name, analyzer in self.project.analyzers.items():
            self.app.create_analyzer(name, analyzer)
            self.app.project.analyzers[name] = analyzer
        self.app.populate_list_widget()
        self.app.listWidget.setCurrentRow(len(self.app.project.analyzers)-1)
        self.app.update_main_tab()
        self.hide()
    
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
            self.load_input_file()

    def collect_selected_analyzers(self):
        # Get checked state of checkboxes
        if self.checkBox_IG.isChecked():
            try:
                ref = int(self.referenceLine.text())
            except:
                ref = 0
                print("ref is set")
            try:
                step = int(self.stepLine.text())
            except:
                step = 64
                print("step is set")
            name = f"IG - {self.comboBox_IG.currentText()} - {ref} - {step}"
            self.project.analyzers[name] = Analyzer(reference_input = ref, steps = step)
            self.project.analyzers[name].activation = activations[self.comboBox_IG.currentText()]
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
            except ValueError:
                pass
    
    def load_model_files(self):
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

        if self.project.test_x is not None:
            self.project.predictions = self.project.model.predict(self.project.test_x, verbose = 2)
    
    def load_input_file(self):
        if os.path.isfile(self.project.input_file_path):
            try:
                with h5py.File(self.project.input_file_path, 'r') as hf:
                    self.project.test_x = hf['test_x'][:]
                    self.project.test_y = hf['test_y'][:]
                    self.project.number_of_classes = self.project.test_y.shape[1]
            except:
                self.selectInputLine.setText(f"Error in loading {self.project.input_file_path}.")
            for possible_class_num in range(self.project.test_y.shape[1]):
                self.comboBox_LRP_Z.addItem(f"Index {possible_class_num}")
                self.comboBox_LRP_AB.addItem(f"Index {possible_class_num}")
                self.comboBox_LRP_Epsilon.addItem(f"Index {possible_class_num}")

            