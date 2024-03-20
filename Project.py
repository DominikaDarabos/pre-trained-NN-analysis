from Analyzer import Analyzer
import numpy as np

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
        self.predictions = None
        self.number_of_classes = None
        self.analyzers = {}

    def set_model_file(self, path):
        self.model_file_path = path

    def set_input_file(self, path):
        self.input_file_path = path

    def set_custom_file(self, path):
        self.custom_object_file_path = path


    ##########################################################
    ############### Prediction Qualities #####################
    ##########################################################

    def get_predicted_classes(self):
        return np.argmax(self.predictions, axis=1)

    def get_truth_classes(self):
        return np.argmax(self.test_y, axis=1)

    def get_truth_class_indices(self, class_num):
        # gives the indices of a certain class based on the ground truth label
        return np.where(self.get_truth_classes() == class_num)[0]

    def get_pred_class_indices(self, class_num):
        return np.where(self.get_predicted_classes() == class_num)[0]

    def get_correct_prediction_indices(self):
        predicted_labels = np.argmax(self.predictions, axis=1)
        return np.where(predicted_labels == np.argmax(self.test_y, axis=1))[0]

    def get_incorrect_prediction_indices(self):
        predicted_labels = np.argmax(self.predictions, axis=1)
        return np.where(predicted_labels != np.argmax(self.test_y, axis=1))[0]

    def get_correct_pos_prediction_indices_for_class(self, class_num):
        correct_pred_indices = self.get_correct_prediction_indices()
        class_indices = self.get_truth_class_indices(class_num)
        return np.intersect1d(correct_pred_indices, class_indices)

    def get_correct_neg_prediction_indices_for_class(self, class_num):
        correct_pred_indices = self.get_correct_prediction_indices()
        class_indices = self.get_truth_class_indices(class_num)
        mask = np.isin(correct_pred_indices, class_indices)
        return correct_pred_indices[~mask]

    def get_incorrect_prediction_indices_for_class(self, class_num):
        false_pos_indices = self.get_false_positive_indices(class_num)
        false_neg_indices = self.get_false_negative_indices(class_num)
        return np.union1d(false_pos_indices, false_neg_indices)

    def get_false_positive_indices(self, class_num):
        truth_class_indices = self.get_truth_class_indices(class_num)
        truth_not_class_indices = np.setdiff1d(np.arange(0, self.predictions.shape[0]), truth_class_indices)
        pred_class_indices = self.get_pred_class_indices(class_num)
        return np.intersect1d(truth_not_class_indices, pred_class_indices)

    def get_false_negative_indices(self, class_num):
        incorrect_pred_indices = self.get_incorrect_prediction_indices()
        class_indices = self.get_truth_class_indices(class_num)
        return np.intersect1d(incorrect_pred_indices, class_indices)