from Analyzer import Analyzer
import numpy as np

class Project():
    def __init__(self):
        self.model_file_path = None
        self.custom_object_file_path = None
        self.input_file_path = None
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

    def convert_prediction_to_labels(self):
        """
        Convert the predictions in a from like the given label.
        """
        max_indices = np.argmax(self.predictions, axis=1)
        pred_labels = np.zeros_like(self.predictions)
        pred_labels[np.arange(len(self.predictions)), max_indices] = 1
        return pred_labels

    def get_predicted_classes(self):
        """
        Returns a one-dimensional array with the predicted classes.
        """
        return np.argmax(self.predictions, axis=1)

    def get_truth_classes(self):
        """
        Returns a one-dimensional array with the actual classes.
        """
        return np.argmax(self.test_y, axis=1)

    def get_truth_class_indices(self, class_num):
        """
        Returns a one-dimensional array with the inidices where the sample actually belongs to the given class.
        """
        return np.where(self.get_truth_classes() == class_num)[0]

    def get_pred_class_indices(self, class_num):
        """
        Returns a one-dimensional array with the inidices where the sample - based on the prediction - belongs to the given class.
        """
        return np.where(self.get_predicted_classes() == class_num)[0]

    def get_correct_prediction_indices(self):
        """
        Returns a one-dimensional array containing the indices of the samples for which the prediction was correct.
        """
        predicted_labels = np.argmax(self.predictions, axis=1)
        return np.where(predicted_labels == np.argmax(self.test_y, axis=1))[0]
    
    def get_correct_pred_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was correct and the sample belongs to the given class.
        """
        zero_indices = np.intersect1d(np.where(self.test_y[:, class_num] == 0)[0],\
                                  np.where(self.convert_prediction_to_labels()[:, class_num] == 0)[0])
        one_indices = np.intersect1d(np.where(self.test_y[:, class_num] == 1)[0],\
                                  np.where(self.convert_prediction_to_labels()[:, class_num] == 1)[0])
        return np.union1d(zero_indices, one_indices)

    def get_incorrect_prediction_indices(self):
        """
        Returns a one-dimensional array containing the indices of the samples for which the prediction was incorrect.
        """
        predicted_labels = np.argmax(self.predictions, axis=1)
        return np.where(predicted_labels != np.argmax(self.test_y, axis=1))[0]

    def get_correct_pos_prediction_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was correctly positive and the sample belongs to the given class.
        """
        correct_pred_indices = self.get_correct_prediction_indices()
        class_indices = self.get_truth_class_indices(class_num)
        return np.intersect1d(correct_pred_indices, class_indices)

    def get_correct_neg_prediction_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was correctly negative and the sample belongs to the given class.
        """
        return np.intersect1d(np.where(self.test_y[:, class_num] == 0)[0],\
                                  np.where(self.convert_prediction_to_labels()[:, class_num] == 0)[0])

    
    def get_false_positive_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was falsely positive and the sample belongs to the given class.
        """
        return np.intersect1d(np.where(self.test_y[:, class_num] == 0)[0],\
                                  np.where(self.convert_prediction_to_labels()[:, class_num] == 1)[0])

    def get_false_negative_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was falsely negative and the sample belongs to the given class.
        """
        return np.intersect1d(np.where(self.test_y[:, class_num] == 1)[0],\
                                  np.where(self.convert_prediction_to_labels()[:, class_num] == 0)[0])

    def get_incorrect_prediction_indices_for_class(self, class_num):
        """
        Returns a one-dimensional array containing the indices of the samples
        for which the prediction was incorrect and the sample belongs to the given class.
        """
        false_pos_indices = self.get_false_positive_indices_for_class(class_num)
        false_neg_indices = self.get_false_negative_indices_for_class(class_num)
        return np.union1d(false_pos_indices, false_neg_indices)
