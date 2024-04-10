import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from NewFigureDialog import NewFigureDialog
from Project import Project
from Analyzer import Analyzer

"""
GUI tests for NewFigureDialog.
Different poll selections and errorlogs are tested.
Used original classes:
    - Project
    - Analyzer
"""


class mainMock():
    def __init__(self):
        self.project = Project()
        self.project.number_of_classes = 3
        self.project.analyzers["IG"] = Analyzer()
    
    def get_current_analyzer(self):
        return "IG"

    def create_new_figure(self, place, figure):
        return


@pytest.fixture
def dialog_upper(qtbot):
    main = mainMock()
    dialog = NewFigureDialog(main, "upper")
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def dialog_bottom(qtbot):
    main = mainMock()
    dialog = NewFigureDialog(main, "bottom")
    qtbot.addWidget(dialog)
    return dialog


def test_on_combobox_selection_change(dialog_upper):
    dialog_upper.plotTypeCombo.setCurrentText("Comparison")
    assert hasattr(dialog_upper, "singleSampleCheckbox")
    assert hasattr(dialog_upper, "averageSampleScatterRadio")
    assert hasattr(dialog_upper, "averageAnalyzerLineRadio")
    assert not hasattr(dialog_upper, "boxRadio")
    assert not hasattr(dialog_upper, "histRadio")

    dialog_upper.plotTypeCombo.setCurrentText("Distribution")
    assert hasattr(dialog_upper, "boxRadio")
    assert hasattr(dialog_upper, "histRadio")

def test_clear_frame(dialog_upper):
    def has_element(frame):
        layout = frame.layout()
        if layout.count() > 0:
                return True
        return False
    assert has_element(dialog_upper.channelsFrame)
    dialog_upper.clear_frame(dialog_upper.channelsFrame)
    assert not has_element(dialog_upper.channelsFrame)

def test_load_classes(dialog_upper):
    dialog_upper.load_classes()    
    dialog_upper.classCombo.setCurrentIndex(0)
    assert dialog_upper.classCombo.currentText() == '0'
    dialog_upper.classCombo.setCurrentIndex(1)
    assert dialog_upper.classCombo.currentText() == '1'
    dialog_upper.classCombo.setCurrentIndex(2)
    assert dialog_upper.classCombo.currentText() == '2'


def test_create_figure(dialog_upper):
    dialog_upper.classCombo.addItem("0")
    dialog_upper.classCombo.setCurrentIndex(0)
    dialog_upper.predQualCombo.setCurrentIndex(1)
    dialog_upper.singleSampleCheckbox.setChecked(True)
    dialog_upper.singleSampleScatterRadio.setChecked(True)
    dialog_upper.averageSampleCheckbox.setChecked(False)
    dialog_upper.averageAnalyzerCheckbox.setChecked(True)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    figure = dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"][0]
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
    assert len(dialog_upper.errorLog) == 0

    dialog_upper.singleSampleCheckbox.setChecked(False)
    dialog_upper.averageSampleCheckbox.setChecked(False)
    dialog_upper.averageAnalyzerCheckbox.setChecked(False)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    assert len(dialog_upper.errorLog) == 1
    assert dialog_upper.errorLog[0] == "At least one channel should be selected for the comparison plot."


    dialog_upper.plotTypeCombo.setCurrentIndex(1)
    dialog_upper.boxRadio.setChecked(False)
    dialog_upper.histRadio.setChecked(False)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 1
    assert len(dialog_upper.errorLog) == 1
    assert dialog_upper.errorLog[0] == "Either boxplot or histogram plot should be selected for distribution plot."

    dialog_upper.plotTypeCombo.setCurrentIndex(1)
    dialog_upper.predQualCombo.setCurrentIndex(0)
    dialog_upper.boxRadio.setChecked(True)
    dialog_upper.histRadio.setChecked(False)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 2
    figure = dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"][1]
    assert figure.config["prediction_quality"] == "correct"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] == 50
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == False

    dialog_upper.plotTypeCombo.setCurrentIndex(1)
    dialog_upper.predQualCombo.setCurrentIndex(2)
    dialog_upper.boxRadio.setChecked(True)
    dialog_upper.boxEveryN.setText("10")
    dialog_upper.histRadio.setChecked(False)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 3
    figure = dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"][1]
    assert figure.config["prediction_quality"] == "false_positive"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] == 10
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == False


    dialog_upper.plotTypeCombo.setCurrentIndex(1)
    dialog_upper.boxRadio.setChecked(False)
    dialog_upper.histRadio.setChecked(True)
    dialog_upper.analyzerRadio.setChecked(False)
    dialog_upper.inputRadio.setChecked(False)

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 2
    assert len(dialog_upper.errorLog) == 1
    assert dialog_upper.errorLog[0] == "Either analyzer or input should be selected under histogram plot."


    dialog_upper.plotTypeCombo.setCurrentIndex(1)
    dialog_upper.boxRadio.setChecked(False)
    dialog_upper.histRadio.setChecked(True)
    dialog_upper.analyzerRadio.setChecked(True)
    dialog_upper.showAllAnalyzerRadio.setChecked(True)
    dialog_upper.histNumOfBins.setText("4")

    dialog_upper.create_figure()
    assert len(dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"]) == 3
    figure = dialog_upper.app.project.analyzers["IG"].ui_elements_config["upper_figures"][2]
    assert figure.config["channels"] == range(0,3)
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == False
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] == 4



def test_create_figure(dialog_bottom):
    dialog_bottom.classCombo.addItem("1")
    dialog_bottom.classCombo.setCurrentIndex(0)
    dialog_bottom.predQualCombo.setCurrentIndex(1)
    dialog_bottom.singleSampleCheckbox.setChecked(True)
    dialog_bottom.singleSampleScatterRadio.setChecked(True)
    dialog_bottom.averageSampleCheckbox.setChecked(True)
    dialog_bottom.averageAnalyzerCheckbox.setChecked(True)

    dialog_bottom.create_figure()
    assert len(dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"]) == 1
    figure = dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"][0]
    assert figure.config["class"] == "0"
    assert figure.config["channels"] == [0]
    assert figure.config["prediction_quality"] == "incorrect"
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["activated"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activated"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"] == True
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] == False
    assert figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] == True
    assert len(dialog_bottom.errorLog) == 0

    dialog_bottom.plotTypeCombo.setCurrentIndex(1)
    dialog_bottom.predQualCombo.setCurrentIndex(0)
    dialog_bottom.boxRadio.setChecked(True)
    dialog_bottom.boxEveryN.setText("10")
    dialog_bottom.histRadio.setChecked(False)

    dialog_bottom.create_figure()
    assert len(dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"]) == 2
    figure = dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"][1]
    assert figure.config["prediction_quality"] == "correct"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] == 10
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == False

    dialog_bottom.plotTypeCombo.setCurrentIndex(1)
    dialog_bottom.predQualCombo.setCurrentIndex(3)
    dialog_bottom.boxRadio.setChecked(False)
    dialog_bottom.histRadio.setChecked(True)
    dialog_bottom.analyzerRadio.setChecked(True)
    dialog_bottom.showAllAnalyzerRadio.setChecked(True)
    dialog_bottom.histNumOfBins.setText("4")

    dialog_bottom.create_figure()
    assert len(dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"]) == 3
    figure = dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"][2]
    assert figure.config["channels"] == range(0,3)
    assert figure.config["prediction_quality"] == "false_negative"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == False
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] == 4

    dialog_bottom.plotTypeCombo.setCurrentIndex(1)
    dialog_bottom.boxRadio.setChecked(False)
    dialog_bottom.histRadio.setChecked(True)
    dialog_bottom.predQualCombo.setCurrentIndex(2)
    dialog_bottom.analyzerRadio.setChecked(True)
    dialog_bottom.showAllAnalyzerRadio.setChecked(True)
    dialog_bottom.histNumOfBins.setText("dummy")

    dialog_bottom.create_figure()
    assert len(dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"]) == 4
    figure = dialog_bottom.app.project.analyzers["IG"].ui_elements_config["bottom_figures"][3]
    assert figure.config["channels"] == range(0,3)
    assert figure.config["prediction_quality"] == "false_positive"
    assert figure.config["plot_type"]["distribution"]["box_plot"]["activated"] == False
    assert figure.config["plot_type"]["distribution"]["histogram"]["activated"] == True
    assert figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] == 30

