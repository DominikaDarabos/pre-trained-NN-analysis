from PySide6 import QtWidgets
from utils import create_new_figure
from PySide6.QtCore import  QCoreApplication

from Figure import Figure_
from ErrorDialog import ErrorDialog


class NewFigureDialog(QtWidgets.QDialog, create_new_figure.Ui_Dialog):
    def __init__(self, main, place, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.setup_widgets_for_comparison()
        self.app = main
        self.place = place
        self.plotTypeCombo.currentIndexChanged.connect(self.on_combobox_selection_change)
        self.createButton.clicked.connect(self.check_form)
        self.cancelButton.clicked.connect(self.close_window)
        self.load_classes()
        self.errorLog = []
    
    def check_form(self):
        """
        Checks if the poll should be accepted or an errordialog should be shown
        """
        self.create_figure()
        if len(self.errorLog) == 0:
            self.accept()
        else:
            error_dialog = ErrorDialog(self.errorLog)
            error_dialog.exec()
            return

    def on_combobox_selection_change(self):
        """
        Changes the GUI according to the plot type selection.
        """
        selected_option = self.plotTypeCombo.currentText()

        if selected_option == "Comparison":
            self.setup_widgets_for_comparison()
        elif selected_option == "Distribution":
            self.setup_widgets_for_distribution()
    
    def clear_frame(self, frame):
        """
        Delete all the GUI objects from the given frame.
        """
        layout = frame.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_frame(frame)

    def load_classes(self):
        """
        Based on the number of classes, the class combobox is filled.
        """
        num_of_classes = self.app.project.number_of_classes
        for num in range(num_of_classes):
            self.classCombo.addItem("")
            self.classCombo.setItemText(num, QCoreApplication.translate("Dialog", str(num), None))

    def close_window(self):
        self.close()
    
    def create_figure(self):
        """
        Gather the selected inputs and fill up the errorlog.
        """
        self.errorLog = []
        figure = Figure_()
        figure.config["class"] = self.classCombo.currentText()
        figure.config["channels"] = [int(self.classCombo.currentText())]
        figure.config["prediction_quality"] = self.predQualCombo.currentText().lower().replace(" ", "_")
        if self.plotTypeCombo.currentText() == "Comparison":
            figure.add_default_comparison()
            if self.singleSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["activated"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"] = self.singleSampleScatterRadio.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"] = self.singleSampleLineRadio.isChecked()
            if self.averageSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activated"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"] = self.averageSampleScatterRadio.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"] = self.averageSampleLineRadio.isChecked()
            if self.averageAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] = self.averageAnalyzerScatterRadio.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] = self.averageAnalyzerLineRadio.isChecked()
            if not self.singleSampleCheckbox.isChecked() and not self.averageSampleCheckbox.isChecked() and not self.averageAnalyzerCheckbox.isChecked():
                self.errorLog.append("<font color='red'>At least one channel should be selected for the comparison plot.</font>")
        elif self.plotTypeCombo.currentText() == "Distribution":
            figure.add_default_distribution()
            if self.boxRadio.isChecked():
                figure.config["plot_type"]["distribution"]["box_plot"]["activated"] = True
                try:
                    figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] = int(self.boxEveryN.text())
                except:
                    figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] = 50
            elif self.histRadio.isChecked():
                figure.config["plot_type"]["distribution"]["histogram"]["activated"] = True
                try:
                    figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] = int(self.histNumOfBins.text())
                except:
                    figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] = 30
                if self.analyzerRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"] = True
                    if self.showAllAnalyzerRadio.isChecked():
                        figure.config["channels"] = range(self.app.project.number_of_classes)
                elif self.inputRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["input"] = True
                    if self.showAllInputRadio.isChecked():
                        figure.config["channels"] = range(self.app.project.number_of_classes)
                else:
                    self.errorLog.append("<font color='red'>Either analyzer or input should be selected under histogram plot.</font>")
            else:
                self.errorLog.append("<font color='red'>Either boxplot or histogram plot should be selected for distribution plot.</font>")
        if len(self.errorLog) == 0:
            analyzer = self.app.get_current_analyzer()
            self.app.project.analyzers[analyzer].ui_elements_config[f"{self.place}_figures"].append(figure)
            self.app.create_new_figure(self.place, figure)
        else:
            return