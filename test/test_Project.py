import sys
import os
import pytest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Project import Project

"""
Unit tests for Project.py
"""

@pytest.fixture
def project():
    return Project()

predictions_two_elements = np.array([
    [0.8, 0.2],
    [0.3, 0.7],
    [0.4, 0.6],
    [0.3, 0.7],
    [0.1, 0.9],
    [0.8, 0.2],
    [0.7, 0.3],
    [0.6, 0.4],
    [0.7, 0.3],
    [0.2, 0.8]])
labels_two_elements = np.array([
    [1., 0.], # correct
    [0., 1.], # correct
    [1., 0.],
    [0., 1.], # correct
    [0., 1.], # correct
    [1., 0.], # correct
    [1., 0.], # correct
    [0., 1.],
    [0., 1.],
    [1., 0.] 
])

predictions_three_elements = np.array([
    [0.8, 0.1, 0.1],
    [0.1, 0.7, 0.2],
    [0.1, 0.6, 0.3],
    [0.3, 0.4, 0.3],
    [0.1, 0.2, 0.7],
    [0.2, 0.2, 0.6],
    [0.4, 0.3, 0.3],
    [0.1, 0.5, 0.4],
    [0.5, 0.3, 0.2],
    [0.2, 0.5, 0.3]
])

labels_three_elements = np.array([
    [1., 0., 0.], # correct for class 0
    [0., 1., 0.], # correct for class 1
    [0., 0., 1.], 
    [1., 0., 0.], 
    [0., 0., 1.], # correct for class 2
    [0., 0., 1.], # correct for class 2
    [0., 1., 0.], 
    [0., 0., 1.], 
    [1., 0., 0.], # correct for class 0
    [0., 1., 0.]  # correct for class 1
])


def test_convert_prediction_to_labels(project):
    project.predictions = predictions_three_elements
    expected_output = np.array([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 1., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
        [0., 0., 1.],
        [1., 0., 0.],
        [0., 1., 0.],
        [1., 0., 0.],
        [0., 1., 0.]
    ])
    assert np.array_equal(project.convert_prediction_to_labels(), expected_output)

def test_get_predicted_classes(project):
    project.predictions = predictions_two_elements
    expected_result = np.array([0, 1, 1, 1, 1, 0, 0, 0, 0, 1])
    assert np.array_equal(project.get_predicted_classes(), expected_result)

    project.predictions = predictions_three_elements
    expected_result = np.array([0,1,1,1,2,2,0,1,0,1])
    assert np.array_equal(project.get_predicted_classes(), expected_result)


def test_get_truth_classes(project):
    project.test_y = labels_two_elements
    expected_output = np.array([0,1,0,1,1,0,0,1,1,0])
    assert np.array_equal(project.get_truth_classes(), expected_output)

    project.test_y = labels_three_elements
    expected_output = np.array([0,1,2,0,2,2,1,2,0,1])
    assert np.array_equal(project.get_truth_classes(), expected_output)

def test_get_truth_class_indices(project):
    project.test_y = labels_two_elements
    expected_output = np.array([0,2,5,6,9])
    assert np.array_equal(project.get_truth_class_indices(0), expected_output)
    expected_output = np.array([1,3,4,7,8])
    assert np.array_equal(project.get_truth_class_indices(1), expected_output)

    project.test_y = labels_three_elements
    expected_output = np.array([0,3,8])
    assert np.array_equal(project.get_truth_class_indices(0), expected_output)
    expected_output = np.array([1,6,9])
    assert np.array_equal(project.get_truth_class_indices(1), expected_output)
    expected_output = np.array([2,4,5,7])
    assert np.array_equal(project.get_truth_class_indices(2), expected_output)


def test_get_pred_class_indices(project):
    project.predictions = predictions_two_elements
    expected_output = np.array([0,5,6,7,8])
    assert np.array_equal(project.get_pred_class_indices(0), expected_output)
    expected_output = np.array([1,2,3,4,9])
    assert np.array_equal(project.get_pred_class_indices(1), expected_output)

    project.predictions = predictions_three_elements
    expected_output = np.array([0,6,8])
    assert np.array_equal(project.get_pred_class_indices(0), expected_output)
    expected_output = np.array([1,2,3,7,9])
    assert np.array_equal(project.get_pred_class_indices(1), expected_output)
    expected_output = np.array([4,5])
    assert np.array_equal(project.get_pred_class_indices(2), expected_output)

def test_get_correct_prediction_indices(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([0,1,3,4,5,6])
    assert np.array_equal(project.get_correct_prediction_indices(), expected_output)

    project.predictions = predictions_three_elements
    project.test_y = labels_three_elements
    expected_output = np.array([0,1,4,5,8,9])
    assert np.array_equal(project.get_correct_prediction_indices(), expected_output)

def test_get_correct_pred_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([0,1,3,4,5,6])
    assert np.array_equal(project.get_correct_pred_indices_for_class(0), expected_output)
    expected_output = np.array([0,1,3,4,5,6])
    assert np.array_equal(project.get_correct_pred_indices_for_class(1), expected_output)

    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([0,1,2,4,5,7,8,9])
    assert np.array_equal(project.get_correct_pred_indices_for_class(0), expected_output)
    expected_output = np.array([0,1,4,5,8,9])
    assert np.array_equal(project.get_correct_pred_indices_for_class(1), expected_output)
    expected_output = np.array([0,1,3,4,5,6,8,9])
    assert np.array_equal(project.get_correct_pred_indices_for_class(2), expected_output)

def test_get_incorrect_prediction_indices(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([2,7,8,9])
    assert np.array_equal(project.get_incorrect_prediction_indices(), expected_output)

    project.predictions = predictions_three_elements
    project.test_y = labels_three_elements
    expected_output = np.array([2,3,6,7])
    assert np.array_equal(project.get_incorrect_prediction_indices(), expected_output)

def test_get_correct_pos_prediction_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([0,5,6])
    assert np.array_equal(project.get_correct_pos_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([1,3,4])
    assert np.array_equal(project.get_correct_pos_prediction_indices_for_class(1), expected_output)

    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([0,8])
    assert np.array_equal(project.get_correct_pos_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([1,9])
    assert np.array_equal(project.get_correct_pos_prediction_indices_for_class(1), expected_output)
    expected_output = np.array([4,5])
    assert np.array_equal(project.get_correct_pos_prediction_indices_for_class(2), expected_output)

def test_get_correct_neg_prediction_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([1,3,4])
    assert np.array_equal(project.get_correct_neg_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([0,5,6])
    assert np.array_equal(project.get_correct_neg_prediction_indices_for_class(1), expected_output)



    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([1,2,4,5,7,9])
    assert np.array_equal(project.get_correct_neg_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([0,4,5,8])
    assert np.array_equal(project.get_correct_neg_prediction_indices_for_class(1), expected_output)
    expected_output = np.array([0,1,3,6,8,9])
    assert np.array_equal(project.get_correct_neg_prediction_indices_for_class(2), expected_output)

def test_get_false_positive_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([7,8])
    assert np.array_equal(project.get_false_positive_indices_for_class(0), expected_output)
    expected_output = np.array([2,9])
    assert np.array_equal(project.get_false_positive_indices_for_class(1), expected_output)

    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([6])
    assert np.array_equal(project.get_false_positive_indices_for_class(0), expected_output)
    expected_output = np.array([2,3,7])
    assert np.array_equal(project.get_false_positive_indices_for_class(1), expected_output)
    expected_output = np.array([])
    assert np.array_equal(project.get_false_positive_indices_for_class(2), expected_output)

def test_get_false_negative_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([2,9])
    assert np.array_equal(project.get_false_negative_indices_for_class(0), expected_output)
    expected_output = np.array([7,8])
    assert np.array_equal(project.get_false_negative_indices_for_class(1), expected_output)

    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([3])
    assert np.array_equal(project.get_false_negative_indices_for_class(0), expected_output)
    expected_output = np.array([6])
    assert np.array_equal(project.get_false_negative_indices_for_class(1), expected_output)
    expected_output = np.array([2,7])
    assert np.array_equal(project.get_false_negative_indices_for_class(2), expected_output)

def test_get_incorrect_prediction_indices_for_class(project):
    project.predictions = predictions_two_elements
    project.test_y = labels_two_elements
    expected_output = np.array([2,7,8,9])
    assert np.array_equal(project.get_incorrect_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([2,7,8,9])
    assert np.array_equal(project.get_incorrect_prediction_indices_for_class(1), expected_output)

    project.test_y = labels_three_elements
    project.predictions = predictions_three_elements
    expected_output = np.array([3,6])
    assert np.array_equal(project.get_incorrect_prediction_indices_for_class(0), expected_output)
    expected_output = np.array([2,3,6,7])
    assert np.array_equal(project.get_incorrect_prediction_indices_for_class(1), expected_output)
    expected_output = np.array([2,7])
    assert np.array_equal(project.get_incorrect_prediction_indices_for_class(2), expected_output)