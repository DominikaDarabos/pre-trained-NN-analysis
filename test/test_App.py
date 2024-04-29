import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from application import MainApp
from NewModelDialog import NewModelDialog
from NewFigureDialog import NewFigureDialog
from ErrorDialog import ErrorDialog
from PySide6.QtWidgets import  QTextBrowser
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

"""
GUI testing for the main app.
"""


@pytest.fixture
def main(qtbot):
    """
    Model for a 3 classed classification with custom layer.
    """
    dialog = MainApp(purpose = "test")
    qtbot.addWidget(dialog)
    newModel = NewModelDialog(dialog, "project")
    newModel.selectModelLine.setText("synhermite_full_model.h5")
    newModel.selectInputLine.setText("synhermite_test_data.h5")
    newModel.selectCustomLine.setText("VPLayer.py")
    newModel.checkBox_LRP_AB.setChecked(True)
    newModel.AlphaBetaComboBox.setCurrentIndex(1)
    newModel.comboBox_LRP_AB.setCurrentIndex(1)
    newModel.checkBox_IG.setChecked(True)
    newModel.referenceLine.setText("0")
    newModel.stepLine.setText("64")
    newModel.comboBox_IG.setCurrentIndex(1)
    qtbot.addWidget(newModel)
    newModel.createButton.click()
    return dialog

@pytest.fixture
def simple_main(qtbot):
    """
    Model for a binary classification without custom layer.
    """
    dialog = MainApp(purpose = "test")
    qtbot.addWidget(dialog)
    newModel = NewModelDialog(dialog, "project")
    newModel.selectModelLine.setText("model_without_custom_object.h5")
    newModel.selectInputLine.setText("synhermite_test_data.h5")
    newModel.checkBox_LRP_Z.setChecked(True)
    newModel.comboBox_LRP_Z.setCurrentIndex(1)
    newModel.checkBox_LRP_Epsilon.setChecked(True)
    newModel.EpsilonInput.setText("0.00001")
    newModel.comboBox_LRP_Epsilon.setCurrentIndex(1)

    qtbot.addWidget(newModel)
    newModel.createButton.click()
    return dialog

def test_load_start_window_with_custom_model(main):
    assert len(main.project.analyzers) == 2
    assert main.info_and_error_browser.toPlainText() == "Input files are loaded successfully.\nIG analyzer is successfully loaded.\nLRP_AB analyzer is successfully loaded."
    assert "IG - Max activation - 0 - 64" in main.project.analyzers
    assert main.project.analyzers["IG - Max activation - 0 - 64"].innvestigate_analyzer != None
    assert "LRP_AB - Max activation - 1 - 0" in main.project.analyzers
    assert main.project.analyzers["LRP_AB - Max activation - 1 - 0"].innvestigate_analyzer != None
    assert main.project.model_file_path == "synhermite_full_model.h5"
    assert main.project.custom_object_file_path == "VPLayer.py"
    assert main.project.input_file_path == "synhermite_test_data.h5"
    assert main.project.model != None
    assert main.project.model_wo_softmax != None
    assert main.project.test_x.shape == (6000,40)
    assert main.project.test_y.shape == (6000,3)
    assert main.project.predictions.shape == (6000,3)
    assert main.project.number_of_classes == 3
    assert main.listWidget.count() == 2
    assert main.infoWidget.count() == 5
    assert main.get_current_analyzer() == "IG - Max activation - 0 - 64"
    assert main.inputDataInfo.toPlainText().startswith("shape")
    assert main.outputDataInfo.toPlainText().startswith("shape")
    assert main.validationInfo.toPlainText().startswith("number")
    assert main.modelInfo.toPlainText().startswith("Model")
    assert len(main.dropdown_menu.actions()) == 6


def test_load_start_window_with_simple_model(simple_main):
    assert len(simple_main.project.analyzers) == 2
    assert simple_main.info_and_error_browser.toPlainText() == "Input files are loaded successfully.\nLRP_Z analyzer is successfully loaded.\nLRP_Epsilon analyzer is successfully loaded."
    assert "LRP_Z - Max activation" in simple_main.project.analyzers
    assert simple_main.project.analyzers["LRP_Z - Max activation"].innvestigate_analyzer != None
    assert "LRP_Epsilon - Max activation - 1e-05" in simple_main.project.analyzers
    assert simple_main.project.analyzers["LRP_Epsilon - Max activation - 1e-05"].innvestigate_analyzer != None
    assert simple_main.project.model_file_path == "model_without_custom_object.h5"
    assert simple_main.project.custom_object_file_path == ""
    assert simple_main.project.input_file_path == "synhermite_test_data.h5"
    assert simple_main.project.model != None
    assert simple_main.project.model_wo_softmax != None
    assert simple_main.project.test_x.shape == (6000,40)
    assert simple_main.project.test_y.shape == (6000,3)
    assert simple_main.project.predictions.shape == (6000,3)
    assert simple_main.project.number_of_classes == 3
    assert simple_main.listWidget.count() == 2
    assert simple_main.infoWidget.count() == 5
    assert simple_main.get_current_analyzer() == "LRP_Z - Max activation"
    assert simple_main.inputDataInfo.toPlainText().startswith("shape")
    assert simple_main.outputDataInfo.toPlainText().startswith("shape")
    assert simple_main.validationInfo.toPlainText().startswith("number")
    assert simple_main.modelInfo.toPlainText().startswith("Model")
    assert len(simple_main.dropdown_menu.actions()) == 6

def test_functionalities_with_custom_model(main):
    """
    Test add new analyzer from menu.
    """
    main.dropdown_menu.actions()[4].trigger()
    assert isinstance(main.qt_dialog, NewModelDialog)
    main.qt_dialog.checkBox_LRP_Z.setChecked(True)
    main.qt_dialog.create_analyzers()
    assert len(main.project.analyzers) == 3
    assert "LRP_Z - None" in main.project.analyzers

    """
    Test adding new figure(s) for the IG analyzer.
    """
    main.listWidget.setCurrentRow(0)
    main.upper_new_plot_button.click()
    assert isinstance(main.qt_dialog, NewFigureDialog)
    main.qt_dialog.classCombo.setCurrentIndex(2)
    main.qt_dialog.predQualCombo.setCurrentIndex(1)
    main.qt_dialog.singleSampleCheckbox.setChecked(True)
    main.qt_dialog.averageAnalyzerCheckbox.setChecked(True)
    main.qt_dialog.check_form()
    assert main.upperPlotTabWidget.count() == 1
    assert len(main.qt_dialog.errorLog) == 0
    assert len(main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config[f"upper_tabs"]) == 1
    assert main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config["upper_plot_count"] == 1
    plotTab = main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config[f"upper_tabs"][f"tab_0"]
    figureAttributes = plotTab.findChild(QTextBrowser, f"upperFigureAttributes_0")
    info_content = "plot_type: comparison \nclass: 2\nprediction quality: incorrect\nactivation: max_activation - neurons with greater influence on the final decision are weighted "
    assert figureAttributes.toPlainText() == info_content

    main.upper_new_plot_button.click()
    assert isinstance(main.qt_dialog, NewFigureDialog)
    main.qt_dialog.classCombo.setCurrentIndex(1)
    main.qt_dialog.predQualCombo.setCurrentIndex(0)
    main.qt_dialog.averageSampleCheckbox.setChecked(True)
    main.qt_dialog.averageAnalyzerCheckbox.setChecked(True)
    main.qt_dialog.check_form()
    assert main.upperPlotTabWidget.count() == 2
    assert len(main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config[f"upper_tabs"]) == 2
    assert main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config["upper_plot_count"] == 2

    main.bottom_new_plot_button.click()
    assert isinstance(main.qt_dialog, NewFigureDialog)
    main.qt_dialog.plotTypeCombo.setCurrentIndex(1)
    main.qt_dialog.boxRadio.setChecked(True)
    main.qt_dialog.boxEveryN.setText("10")
    main.qt_dialog.histRadio.setChecked(False)
    main.qt_dialog.check_form()
    assert main.bottomPlotTabWidget.count() == 1
    assert len(main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config[f"upper_tabs"]) == 2
    assert main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config["upper_plot_count"] == 2
    assert len(main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config[f"bottom_tabs"]) == 1
    assert main.project.analyzers["IG - Max activation - 0 - 64"].ui_elements_config["bottom_plot_count"] == 1

    """
    Click on an other analyzer in the menu, create a figure and then click on the first one again
    """
    main.listWidget.setCurrentRow(2)
    main.update_main_tab()
    assert main.get_current_analyzer() == "LRP_Z - None"
    assert main.upperPlotTabWidget.count() == 0
    assert main.bottomPlotTabWidget.count() == 0
    main.bottom_new_plot_button.click()
    main.qt_dialog.plotTypeCombo.setCurrentIndex(1)
    main.qt_dialog.boxRadio.setChecked(True)
    main.qt_dialog.check_form()
    assert main.bottomPlotTabWidget.count() == 1
    assert len(main.project.analyzers["LRP_Z - None"].ui_elements_config[f"upper_tabs"]) == 0
    assert main.project.analyzers["LRP_Z - None"].ui_elements_config["upper_plot_count"] == 0
    assert len(main.project.analyzers["LRP_Z - None"].ui_elements_config[f"bottom_tabs"]) == 1
    assert main.project.analyzers["LRP_Z - None"].ui_elements_config["bottom_plot_count"] == 1
    assert main.upperPlotTabWidget.count() == 0
    assert main.bottomPlotTabWidget.count() == 1

    main.listWidget.setCurrentRow(0)
    main.update_main_tab()
    assert main.upperPlotTabWidget.count() == 2
    assert main.bottomPlotTabWidget.count() == 1

    """
    Test the clear upper figures tabs from the menu
    """
    main.dropdown_menu.actions()[0].trigger()
    assert main.upperPlotTabWidget.count() == 0
    assert main.bottomPlotTabWidget.count() == 1

    """
    Test the clear bottom figures tabs from the menu
    """
    main.dropdown_menu.actions()[1].trigger()
    assert main.upperPlotTabWidget.count() == 0
    assert main.bottomPlotTabWidget.count() == 0

    """
    Test the exit from the menu
    """
    plt.close('all')
    main.dropdown_menu.actions()[5].trigger()
    assert main.isVisible() == False



def test_functionalities_with_simple_model(simple_main):
    """
    Test add new analyzer from menu.
    """
    simple_main.dropdown_menu.actions()[4].trigger()
    assert isinstance(simple_main.qt_dialog, NewModelDialog)
    simple_main.qt_dialog.checkBox_IG.setChecked(True)
    simple_main.qt_dialog.referenceLine.setText("2")
    simple_main.qt_dialog.stepLine.setText("10")
    simple_main.qt_dialog.comboBox_IG.setCurrentIndex(1)
    simple_main.qt_dialog.create_analyzers()
    assert len(simple_main.project.analyzers) == 3
    assert "IG - Max activation - 2 - 10" in simple_main.project.analyzers

    """
    Test adding new figure(s) for the IG analyzer.
    """
    simple_main.listWidget.setCurrentRow(0)
    simple_main.upper_new_plot_button.click()
    assert isinstance(simple_main.qt_dialog, NewFigureDialog)
    simple_main.qt_dialog.classCombo.setCurrentIndex(2)
    simple_main.qt_dialog.predQualCombo.setCurrentIndex(1)
    simple_main.qt_dialog.singleSampleCheckbox.setChecked(True)
    simple_main.qt_dialog.averageAnalyzerCheckbox.setChecked(True)
    simple_main.qt_dialog.check_form()
    assert simple_main.upperPlotTabWidget.count() == 1
    assert len(simple_main.qt_dialog.errorLog) == 0
    assert len(simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config[f"upper_tabs"]) == 1
    assert simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config["upper_plot_count"] == 1
    plotTab = simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config[f"upper_tabs"][f"tab_0"]
    figureAttributes = plotTab.findChild(QTextBrowser, f"upperFigureAttributes_0")
    info_content = "plot_type: comparison \nclass: 2\nprediction quality: incorrect\nactivation: max_activation - neurons with greater influence on the final decision are weighted "
    assert figureAttributes.toPlainText() == info_content

    simple_main.upper_new_plot_button.click()
    assert isinstance(simple_main.qt_dialog, NewFigureDialog)
    simple_main.qt_dialog.classCombo.setCurrentIndex(1)
    simple_main.qt_dialog.predQualCombo.setCurrentIndex(0)
    simple_main.qt_dialog.averageSampleCheckbox.setChecked(True)
    simple_main.qt_dialog.averageAnalyzerCheckbox.setChecked(True)
    simple_main.qt_dialog.check_form()
    assert simple_main.upperPlotTabWidget.count() == 2
    assert len(simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config[f"upper_tabs"]) == 2
    assert simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config["upper_plot_count"] == 2

    simple_main.bottom_new_plot_button.click()
    assert isinstance(simple_main.qt_dialog, NewFigureDialog)
    simple_main.qt_dialog.plotTypeCombo.setCurrentIndex(1)
    simple_main.qt_dialog.boxRadio.setChecked(True)
    simple_main.qt_dialog.boxEveryN.setText("10")
    simple_main.qt_dialog.histRadio.setChecked(False)
    simple_main.qt_dialog.check_form()
    assert simple_main.bottomPlotTabWidget.count() == 1
    assert len(simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config[f"upper_tabs"]) == 2
    assert simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config["upper_plot_count"] == 2
    assert len(simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config[f"bottom_tabs"]) == 1
    assert simple_main.project.analyzers["LRP_Z - Max activation"].ui_elements_config["bottom_plot_count"] == 1

    """
    Click on an other analyzer in the menu, create a figure and then click on the first one again
    """
    simple_main.listWidget.setCurrentRow(2)
    simple_main.update_main_tab()
    assert simple_main.get_current_analyzer() == "IG - Max activation - 2 - 10"
    assert simple_main.upperPlotTabWidget.count() == 0
    assert simple_main.bottomPlotTabWidget.count() == 0
    simple_main.bottom_new_plot_button.click()
    simple_main.qt_dialog.plotTypeCombo.setCurrentIndex(1)
    simple_main.qt_dialog.boxRadio.setChecked(True)
    simple_main.qt_dialog.check_form()
    assert simple_main.bottomPlotTabWidget.count() == 1
    assert len(simple_main.project.analyzers["IG - Max activation - 2 - 10"].ui_elements_config[f"upper_tabs"]) == 0
    assert simple_main.project.analyzers["IG - Max activation - 2 - 10"].ui_elements_config["upper_plot_count"] == 0
    assert len(simple_main.project.analyzers["IG - Max activation - 2 - 10"].ui_elements_config[f"bottom_tabs"]) == 1
    assert simple_main.project.analyzers["IG - Max activation - 2 - 10"].ui_elements_config["bottom_plot_count"] == 1
    assert simple_main.upperPlotTabWidget.count() == 0
    assert simple_main.bottomPlotTabWidget.count() == 1

    simple_main.listWidget.setCurrentRow(0)
    simple_main.update_main_tab()
    assert simple_main.upperPlotTabWidget.count() == 2
    assert simple_main.bottomPlotTabWidget.count() == 1

    """
    Test the clear upper figures tabs from the menu
    """
    simple_main.dropdown_menu.actions()[0].trigger()
    assert simple_main.upperPlotTabWidget.count() == 0
    assert simple_main.bottomPlotTabWidget.count() == 1

    """
    Test the clear bottom figures tabs from the menu
    """
    simple_main.dropdown_menu.actions()[1].trigger()
    assert simple_main.upperPlotTabWidget.count() == 0
    assert simple_main.bottomPlotTabWidget.count() == 0

    """
    Test the exit from the menu
    """
    plt.close('all')
    simple_main.dropdown_menu.actions()[5].trigger()
    assert simple_main.isVisible() == False

