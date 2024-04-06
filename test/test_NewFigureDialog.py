import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from NewFigureDialog import NewFigureDialog
from Project import Project
from Analyzer import Analyzer

from PySide6.QtWidgets import  QLabel


class mainMock():
    def __init__(self):
        self.project = Project()
        self.project.number_of_classes = 3
        self.project.analyzers["IG"] = Analyzer()
    
    def get_current_analyzer(self):
        return "IG"

    def create_new_comparison_figure(self, place, figure):
        return


@pytest.fixture
def dialog(qtbot):
    main = mainMock()
    dialog = NewFigureDialog(main, "upper")
    qtbot.addWidget(dialog)
    return dialog

def test_on_combobox_selection_change(dialog):
    dialog.plotTypeCombo.setCurrentText("Comparison")
    assert hasattr(dialog, "singleSampleCheckbox")
    assert hasattr(dialog, "averageSampleScatterRadio")
    assert hasattr(dialog, "averageAnalyzerLineRadio")
    assert not hasattr(dialog, "boxRadio")
    assert not hasattr(dialog, "histRadio")

    dialog.plotTypeCombo.setCurrentText("Distribution")
    assert hasattr(dialog, "boxRadio")
    assert hasattr(dialog, "histRadio")

def test_clear_frame(dialog):
    def has_element(frame):
        layout = frame.layout()
        if layout.count() > 0:
                return True
        return False
    assert has_element(dialog.channelsFrame)
    dialog.clear_frame(dialog.channelsFrame)
    assert not has_element(dialog.channelsFrame)

def test_load_classes(dialog):
    dialog.load_classes()    
    dialog.classCombo.setCurrentIndex(0)
    assert dialog.classCombo.currentText() == '0'
    dialog.classCombo.setCurrentIndex(1)
    assert dialog.classCombo.currentText() == '1'
    dialog.classCombo.setCurrentIndex(2)
    assert dialog.classCombo.currentText() == '2'


def test_create_figure(dialog):
    dialog.classCombo.addItem("0")
    dialog.classCombo.setCurrentIndex(0)
    dialog.predQualCombo.setCurrentIndex(1)
    dialog.singleSampleCheckbox.setChecked(True)
    dialog.singleSampleScatterRadio.setChecked(True)
    dialog.averageSampleCheckbox.setChecked(False)
    dialog.averageAnalyzerCheckbox.setChecked(True)

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    figure = dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"][0]
    assert figure.config["class"] == "0"
    assert figure.config["channels"] == [0]
    assert figure.config["prediction_quality"] == "incorrect"
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["activated"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activated"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] == True
    assert len(dialog.errorLog) == 0

    dialog.singleSampleCheckbox.setChecked(False)
    dialog.averageSampleCheckbox.setChecked(False)
    dialog.averageAnalyzerCheckbox.setChecked(False)

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    assert len(dialog.errorLog) == 1
    assert dialog.errorLog[0] == "At least one channel should be selected for the comparison plot."


    dialog.plotTypeCombo.setCurrentIndex(1)
    dialog.boxRadio.setChecked(False)
    dialog.histRadio.setChecked(False)

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    assert len(dialog.errorLog) == 1
    assert dialog.errorLog[0] == "Either boxplot or histogram plot should be selected for distribution plot."

    dialog.plotTypeCombo.setCurrentIndex(1)
    dialog.predQualCombo.setCurrentIndex(0)
    dialog.boxRadio.setChecked(True)
    dialog.histRadio.setChecked(False)

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 2
    figure = dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"][1]
    assert figure.config["prediction_quality"] == "correct"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] == 50
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == False


    dialog.plotTypeCombo.setCurrentIndex(1)
    dialog.boxRadio.setChecked(False)
    dialog.histRadio.setChecked(True)
    dialog.analyzerRadio.setChecked(False)
    dialog.inputRadio.setChecked(False)

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 2
    assert len(dialog.errorLog) == 1
    assert dialog.errorLog[0] == "Either analyzer or input should be selected under histogram plot."


    dialog.plotTypeCombo.setCurrentIndex(1)
    dialog.boxRadio.setChecked(False)
    dialog.histRadio.setChecked(True)
    dialog.analyzerRadio.setChecked(True)
    dialog.showAllAnalyzerRadio.setChecked(True)
    dialog.histNumOfBins.setText("4")

    dialog.create_figure()
    assert len(dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 3
    figure = dialog.app.project.analyzers["IG"].ui_elements_config["upper_figures"][2]
    assert figure.config["channels"] == range(0,3)
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == False
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] == 4

