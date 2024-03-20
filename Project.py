from Analyzer import Analyzer

class Project():
    def __init__(self):
        #TODO: until testing
        self.model_file_path = "C:/Users/dominika/vpnet/trained_models/ecg_train_test_full_model.h5"
        self.custom_object_file_path = "C:/Users/dominika/vpnet/tensorflow/VPLayer.py"
        self.input_file_path = "C:/Users/dominika/vpnet/tensorflow/ecg_test_data.h5"
        self.model = None
        self.model_wo_softmax = None
        self.test_x = None
        self.test_y = None
        self.number_of_classes = None
        self.analyzers = {}

    def set_model_file(self, path):
        self.model_file_path = path

    def set_input_file(self, path):
        self.input_file_path = path

    def set_custom_file(self, path):
        self.custom_object_file_path = path