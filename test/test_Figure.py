import os, sys
import pytest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Figure import Figure_


"""
Unit tests for Figure.py
Tests are only for functions which do not utilize plot creation.
"""



@pytest.fixture
def figure():
    return Figure_()

def test_add_default_comparison(figure):
    figure.add_default_comparison()
    assert "comparison" in figure.config["plot_type"]
    assert "random_count" in figure.config["plot_type"]["comparison"]
    assert "channels" in figure.config["plot_type"]["comparison"]

def test_add_default_distribution(figure):
    figure.add_default_distribution()
    assert "distribution" in figure.config["plot_type"]
    assert "box_plot" in figure.config["plot_type"]["distribution"]
    assert "histogram" in figure.config["plot_type"]["distribution"]

def test_is_comparison(figure):
    assert not figure.is_comparison()
    figure.add_default_comparison()
    assert figure.is_comparison()

def test_is_hist_distribution(figure):
    assert not figure.is_hist_distribution()
    figure.add_default_distribution()
    figure.config["plot_type"]["distribution"]["histogram"]["activated"] = True
    assert figure.is_hist_distribution()

def test_is_box_distribution(figure):
    assert not figure.is_box_distribution()
    figure.add_default_distribution()
    figure.config["plot_type"]["distribution"]["box_plot"]["activated"] = True
    assert figure.is_box_distribution()

def test_normalize():
    data = np.array([1, 2, 3, 4, 5])
    normalized_data = Figure_().normalize(data, 0, 1)
    assert np.allclose(normalized_data, np.array([0, 0.25, 0.5, 0.75, 1]))

def test_upsample(figure):
    data = np.array([1, 2, 3])
    expected_output = np.array([1, 1.5, 2, 2.5, 3])
    np.testing.assert_array_almost_equal(figure.upsample(data, 2), expected_output)

    data = np.array([1, 2, 3])
    expected_output = np.array([1, 1.3333333333333333, 1.6666666666666665, 2, 2.3333333333333335, 2.666666666666667, 3])
    np.testing.assert_array_almost_equal(figure.upsample(data, 3), expected_output)

    data = np.array([1, 2, 3])
    expected_output = np.array([1, 2, 3])
    np.testing.assert_array_almost_equal(figure.upsample(data, 1), expected_output)

    data = np.array([1])
    expected_output = np.array([1])
    np.testing.assert_array_almost_equal(figure.upsample(data, 2), expected_output)