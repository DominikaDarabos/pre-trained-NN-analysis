import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from application import MainApp
from NewModelDialog import NewModelDialog
from NewFigureDialog import NewFigureDialog
from PySide6.QtWidgets import  QTextBrowser

"""
GUI testing for the main app.
"""


@pytest.fixture
def main(qtbot):
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
    newModel.create_project()
    qtbot.addWidget(newModel)
    return dialog

def test_load_start_window(main):
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

def test_functionalities(main):
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
    main.dropdown_menu.actions()[5].trigger()
    assert main.isVisible() == False

