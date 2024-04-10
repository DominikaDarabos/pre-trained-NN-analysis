import sys
import os
import pytest
from PySide6.QtWidgets import QListWidget

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from NewModelDialog import NewModelDialog
from Project import Project
from Analyzer import Analyzer

"""
GUI tests for NewModelDialog.
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
        self.listWidget = QListWidget()
    
    def get_current_analyzer(self):
        return "IG"

    def create_new_figure(self, place, figure):
        return
    
    def load_start_window(self):
        return

    def populate_list_widget(self):
        return

    def update_main_tab(self):
        return

@pytest.fixture
def start_dialog(qtbot):
    main = mainMock()
    dialog = NewModelDialog(main, "project")
    qtbot.addWidget(dialog)
    return dialog


@pytest.fixture
def add_dialog(qtbot):
    main = mainMock()
    dialog = NewModelDialog(main)
    qtbot.addWidget(dialog)
    return dialog

def test_collect_selected_analyzers_IG(add_dialog):
    add_dialog.errorLog = []
    add_dialog.checkBox_IG.setChecked(True)
    add_dialog.referenceLine.setText("dummy")
    add_dialog.comboBox_IG.setCurrentIndex(1)
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 1
    assert len(add_dialog.project.analyzers) == 0
    assert "<font color='red'>Integrated gradient's reference and step value have to be numbers.</font>" in add_dialog.errorLog

def test_collect_selected_analyzers_LRP_Z(add_dialog):
    add_dialog.errorLog = []
    add_dialog.checkBox_LRP_Z.setChecked(True)
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 0
    assert len(add_dialog.project.analyzers) == 1
    print(add_dialog.project.analyzers.keys())
    assert "LRP_Z - None" in add_dialog.project.analyzers

    add_dialog.checkBox_LRP_Z.setChecked(True)
    add_dialog.comboBox_LRP_Z.setCurrentIndex(1)
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 0
    assert len(add_dialog.project.analyzers) == 1
    assert "LRP_Z - Max activation" in add_dialog.project.analyzers

def test_collect_selected_analyzers_LRP_AB(add_dialog):
    add_dialog.errorLog = []
    add_dialog.checkBox_LRP_AB.setChecked(True)
    add_dialog.AlphaBetaComboBox.setCurrentIndex(0)
    add_dialog.comboBox_LRP_AB.setCurrentIndex(1)
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 0
    assert len(add_dialog.project.analyzers) == 1
    assert "LRP_AB - Max activation - 2 - 1" in add_dialog.project.analyzers

    add_dialog.checkBox_LRP_AB.setChecked(True)
    add_dialog.AlphaBetaComboBox.setCurrentIndex(1)
    add_dialog.comboBox_LRP_AB.setCurrentIndex(0)
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 0
    assert len(add_dialog.project.analyzers) == 1
    assert "LRP_AB - None - 1 - 0" in add_dialog.project.analyzers

def test_collect_selected_analyzers_LRP_eps(add_dialog):
    add_dialog.errorLog = []
    add_dialog.checkBox_LRP_Epsilon.setChecked(True)
    add_dialog.EpsilonInput.setText("0.1")
    add_dialog.collect_selected_analyzers()
    assert len(add_dialog.errorLog) == 0
    assert len(add_dialog.project.analyzers) == 1
    assert "LRP_Epsilon - None - 0.1" in add_dialog.project.analyzers

def test_check_input_files_model(start_dialog):
    start_dialog.errorLog = []
    start_dialog.selectModelLine.setText("dummy")
    start_dialog.check_input_files()
    assert start_dialog.project.model_file_path == ""

    start_dialog.errorLog = []
    start_dialog.selectModelLine.setText(os.path.abspath(__file__))
    start_dialog.check_input_files()
    assert start_dialog.project.model_file_path == os.path.abspath(__file__)

def test_check_input_files_custom(start_dialog):
    start_dialog.errorLog = []
    start_dialog.selectCustomLine.setText("dummy")
    start_dialog.check_input_files()
    assert start_dialog.project.custom_object_file_path == ""

    start_dialog.errorLog = []
    start_dialog.selectCustomLine.setText(os.path.abspath(__file__))
    start_dialog.check_input_files()
    assert start_dialog.project.custom_object_file_path == os.path.abspath(__file__)

def test_check_input_files_input(start_dialog):
    start_dialog.errorLog = []
    start_dialog.selectInputLine.setText("dummy")
    start_dialog.check_input_files()
    assert start_dialog.project.input_file_path == ""

    start_dialog.errorLog = []
    start_dialog.selectInputLine.setText(os.path.abspath(__file__))
    start_dialog.check_input_files()
    assert start_dialog.project.input_file_path == os.path.abspath(__file__)
