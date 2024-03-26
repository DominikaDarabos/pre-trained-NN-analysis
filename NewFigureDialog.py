from PySide6 import QtWidgets
from utils import create_new_figure
from PySide6.QtWidgets import  QLabel, QFrame, QVBoxLayout, QGridLayout, QCheckBox, QRadioButton, QLineEdit
from PySide6.QtCore import QSize, QCoreApplication

from Figure import Figure_


class NewFigureDialog(QtWidgets.QDialog, create_new_figure.Ui_Dialog):
    def __init__(self, main, place, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.setup_widgets_for_comparison()
        self.activateWindow()
        self.app = main
        self.place = place
        self.plotTypeCombo.currentIndexChanged.connect(self.on_combobox_selection_change)
        self.createButton.clicked.connect(self.create_figure)
        self.cancelButton.clicked.connect(self.close_window)
        self.load_classes()

    def on_combobox_selection_change(self):
        selected_option = self.plotTypeCombo.currentText()

        if selected_option == "Comparison":
            self.setup_widgets_for_comparison()
        elif selected_option == "Distribution":
            self.setup_widgets_for_distribution()
    
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            if child.layout():
                self.clear_layout(child.layout())
    
    def clear_frame(self, frame):
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
        num_of_classes = self.app.project.number_of_classes
        for num in range(num_of_classes):
            self.classCombo.addItem("")
            self.classCombo.setItemText(num, QCoreApplication.translate("Dialog", str(num), None))



    def close_window(self):
        self.close()
    
    def create_figure(self):
        figure = Figure_()
        figure.config["class"] = self.classCombo.currentText()
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
            if self.singleAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["activated"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["scatter"] = self.singleAnalyzerScatterRadio.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["line"] = self.singleAnalyzerLineRadio.isChecked()
            if self.averageAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] = self.averageAnalyzerScatterRadio.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] = self.averageAnalyzerLineRadio.isChecked()
        elif self.plotTypeCombo.currentText() == "Distribution":
            figure.add_default_distribution()
            if self.boxRadio.isChecked():
                figure.config["plot_type"]["distribution"]["box_plot"]["activated"] = True
                if self.boxEveryN.text().isnumeric():
                    figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] = int(self.boxEveryN.text())
                else:
                    figure.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"] = 4
            if self.histRadio.isChecked():
                print(figure.config["plot_type"]["distribution"]["histogram"]["activated"])
                figure.config["plot_type"]["distribution"]["histogram"]["activated"] = True
                if self.histNumOfBins.text().isnumeric():
                    figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] = int(self.histNumOfBins.text())
                else:
                    figure.config["plot_type"]["distribution"]["histogram"]["num_of_bins"] = 30
                if self.analyzerRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["show_all_class"] = self.showAllAnalyzerRadio.isChecked()
                if self.inputRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["show_all_class"] = self.showAllInputRadio.isChecked()
                print(figure.config["plot_type"]["distribution"]["histogram"]["activated"])
        if self.place == 0:
            analyzer = self.app.get_current_analyzer()
            self.app.project.analyzers[analyzer].ui_elements_config[f"upper_figures"].append(figure)
            self.app.create_new_comparison_figure("upper", figure)
        
            currentcount = self.app.project.analyzers[analyzer].ui_elements_config[f"upper_plot_count"]
            print(self.app.project.analyzers[analyzer].ui_elements_config[f"upper_figures"][currentcount-1])
        elif self.place == 1:
            analyzer = self.app.get_current_analyzer()
            self.app.project.analyzers[analyzer].ui_elements_config[f"bottom_figures"].append(figure)
            self.app.create_new_comparison_figure("bottom", figure)

            currentcount = self.app.project.analyzers[analyzer].ui_elements_config[f"bottom_plot_count"]
            print(self.app.project.analyzers[analyzer].ui_elements_config[f"bottom_figures"][currentcount-1])
        self.accept()


    def setup_widgets_for_comparison(self):
        # Clear the layout if it's not empty
        self.clear_frame(self.baseFrame_2)

        self.channelsFrame = QFrame(self.baseFrame_2)
        self.channelsFrame.setObjectName(u"channelsFrame")
        self.channelsFrame.setFrameShape(QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.channelsFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.channelsTitle = QLabel(self.channelsFrame)
        self.channelsTitle.setObjectName(u"channelsTitle")
        self.channelsTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_3.addWidget(self.channelsTitle, 0, 0, 1, 1)
        self.singleSampleCheckbox = QCheckBox(self.channelsFrame)
        self.singleSampleCheckbox.setObjectName(u"singleSampleCheckbox")
        self.gridLayout_3.addWidget(self.singleSampleCheckbox, 1, 0, 1, 1)
        self.averageSampleCheckbox = QCheckBox(self.channelsFrame)
        self.averageSampleCheckbox.setObjectName(u"averageSampleCheckbox")
        self.gridLayout_3.addWidget(self.averageSampleCheckbox, 2, 0, 1, 1)
        self.singleAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.singleAnalyzerCheckbox.setObjectName(u"singleAnalyzerCheckbox")
        self.gridLayout_3.addWidget(self.singleAnalyzerCheckbox, 3, 0, 1, 1)
        self.averageAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.averageAnalyzerCheckbox.setObjectName(u"averageAnalyzerCheckbox")
        self.gridLayout_3.addWidget(self.averageAnalyzerCheckbox, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.channelsFrame, 0, 0, 1, 1)
        self.radioFrame = QFrame(self.baseFrame_2)
        self.radioFrame.setObjectName(u"radioFrame")
        self.radioFrame.setFrameShape(QFrame.StyledPanel)
        self.radioFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.radioFrame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.averageSampleFrame = QFrame(self.radioFrame)
        self.averageSampleFrame.setObjectName(u"averageSampleFrame")
        self.averageSampleFrame.setFrameShape(QFrame.StyledPanel)
        self.averageSampleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.averageSampleFrame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.averageSampleScatterRadio = QRadioButton(self.averageSampleFrame)
        self.averageSampleScatterRadio.setObjectName(u"averageSampleScatterRadio")
        self.gridLayout_8.addWidget(self.averageSampleScatterRadio, 0, 0, 1, 1)
        self.averageSampleLineRadio = QRadioButton(self.averageSampleFrame)
        self.averageSampleLineRadio.setObjectName(u"averageSampleLineRadio")
        self.gridLayout_8.addWidget(self.averageSampleLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageSampleFrame, 2, 0, 1, 1)
        self.singleAnalyzerFrame = QFrame(self.radioFrame)
        self.singleAnalyzerFrame.setObjectName(u"singleAnalyzerFrame")
        self.singleAnalyzerFrame.setFrameShape(QFrame.StyledPanel)
        self.singleAnalyzerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.singleAnalyzerFrame)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.singleAnalyzerScatterRadio = QRadioButton(self.singleAnalyzerFrame)
        self.singleAnalyzerScatterRadio.setObjectName(u"singleAnalyzerScatterRadio")
        self.gridLayout_9.addWidget(self.singleAnalyzerScatterRadio, 0, 0, 1, 1)
        self.singleAnalyzerLineRadio = QRadioButton(self.singleAnalyzerFrame)
        self.singleAnalyzerLineRadio.setObjectName(u"singleAnalyzerLineRadio")
        self.gridLayout_9.addWidget(self.singleAnalyzerLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.singleAnalyzerFrame, 3, 0, 1, 1)
        self.singleSampleFrame = QFrame(self.radioFrame)
        self.singleSampleFrame.setObjectName(u"singleSampleFrame")
        self.singleSampleFrame.setFrameShape(QFrame.StyledPanel)
        self.singleSampleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.singleSampleFrame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.singleSampleScatterRadio = QRadioButton(self.singleSampleFrame)
        self.singleSampleScatterRadio.setObjectName(u"singleSampleScatterRadio")
        self.gridLayout_7.addWidget(self.singleSampleScatterRadio, 0, 0, 1, 1)
        self.singleSampleLineRadio = QRadioButton(self.singleSampleFrame)
        self.singleSampleLineRadio.setObjectName(u"singleSampleLineRadio")
        self.gridLayout_7.addWidget(self.singleSampleLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.singleSampleFrame, 1, 0, 1, 1)
        self.labelFrame = QFrame(self.radioFrame)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.labelFrame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scatterTitle_2 = QLabel(self.labelFrame)
        self.scatterTitle_2.setObjectName(u"scatterTitle_2")
        self.scatterTitle_2.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.scatterTitle_2, 0, 0, 1, 1)
        self.linetitle_2 = QLabel(self.labelFrame)
        self.linetitle_2.setObjectName(u"linetitle_2")
        self.linetitle_2.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.linetitle_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.labelFrame, 0, 0, 1, 1)
        self.averageAnalyzerFrame = QFrame(self.radioFrame)
        self.averageAnalyzerFrame.setObjectName(u"averageAnalyzerFrame")
        self.averageAnalyzerFrame.setFrameShape(QFrame.StyledPanel)
        self.averageAnalyzerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.averageAnalyzerFrame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.averageAnalyzerScatterRadio = QRadioButton(self.averageAnalyzerFrame)
        self.averageAnalyzerScatterRadio.setObjectName(u"averageAnalyzerScatterRadio")
        self.gridLayout_10.addWidget(self.averageAnalyzerScatterRadio, 0, 0, 1, 1)
        self.averageAnalyzerLineRadio = QRadioButton(self.averageAnalyzerFrame)
        self.averageAnalyzerLineRadio.setObjectName(u"averageAnalyzerLineRadio")
        self.gridLayout_10.addWidget(self.averageAnalyzerLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageAnalyzerFrame, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.radioFrame, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)



        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Average sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Average analyzer score", None))
        self.averageSampleScatterRadio.setText("")
        self.averageSampleLineRadio.setText("")
        self.singleAnalyzerScatterRadio.setText("")
        self.singleAnalyzerLineRadio.setText("")
        self.singleSampleScatterRadio.setText("")
        self.singleSampleLineRadio.setText("")
        self.scatterTitle_2.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.linetitle_2.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.averageAnalyzerScatterRadio.setText("")
        self.averageAnalyzerLineRadio.setText("")
    
    def setup_widgets_for_distribution(self):
        self.clear_frame(self.baseFrame_2)
    
        self.figureTypeTitle = QLabel(self.baseFrame_2)
        self.figureTypeTitle.setObjectName(u"figureTypeTitle")
        self.figureTypeTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_2.addWidget(self.figureTypeTitle, 0, 0, 1, 1)
        self.boxFrame = QFrame(self.baseFrame_2)
        self.boxFrame.setObjectName(u"boxFrame")
        self.boxFrame.setFrameShape(QFrame.StyledPanel)
        self.boxFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.boxFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.boxRadio = QRadioButton(self.boxFrame)
        self.boxRadio.setObjectName(u"boxRadio")
        self.gridLayout_6.addWidget(self.boxRadio, 0, 0, 1, 1)
        self.boxEveryN = QLineEdit(self.boxFrame)
        self.boxEveryN.setObjectName(u"boxEveryN")
        self.gridLayout_6.addWidget(self.boxEveryN, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.boxFrame, 1, 0, 1, 1)
        self.histFrame = QFrame(self.baseFrame_2)
        self.histFrame.setObjectName(u"histFrame")
        self.histFrame.setFrameShape(QFrame.StyledPanel)
        self.histFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.histFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.histDetailesFrame = QFrame(self.histFrame)
        self.histDetailesFrame.setObjectName(u"histDetailesFrame")
        self.histDetailesFrame.setFrameShape(QFrame.StyledPanel)
        self.histDetailesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.histDetailesFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.histDetailesFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.analyzerRadio = QRadioButton(self.frame)
        self.analyzerRadio.setObjectName(u"analyzerRadio")
        self.verticalLayout.addWidget(self.analyzerRadio)
        self.inputRadio = QRadioButton(self.frame)
        self.inputRadio.setObjectName(u"inputRadio")
        self.verticalLayout.addWidget(self.inputRadio)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QFrame(self.histDetailesFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.showAllAnalyzerRadio = QRadioButton(self.frame_2)
        self.showAllAnalyzerRadio.setObjectName(u"showAllAnalyzerRadio")
        self.verticalLayout_2.addWidget(self.showAllAnalyzerRadio)
        self.showAllInputRadio = QRadioButton(self.frame_2)
        self.showAllInputRadio.setObjectName(u"showAllInputRadio")
        self.verticalLayout_2.addWidget(self.showAllInputRadio)
        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.histDetailesFrame, 2, 0, 1, 1)
        self.histRadio = QRadioButton(self.histFrame)
        self.histRadio.setObjectName(u"histRadio")

        self.gridLayout_3.addWidget(self.histRadio, 0, 0, 1, 1)

        self.histNumOfBins = QLineEdit(self.histFrame)
        self.histNumOfBins.setObjectName(u"histNumOfBins")

        self.gridLayout_3.addWidget(self.histNumOfBins, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.histFrame, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)
        self.figureTypeTitle.setText(QCoreApplication.translate("Dialog", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("Dialog", u"Box plot", None))
        self.boxEveryN.setText(QCoreApplication.translate("Dialog", u"Sample frequency", None))
        self.histRadio.setText(QCoreApplication.translate("Dialog", u"Histogram", None))
        self.analyzerRadio.setText(QCoreApplication.translate("Dialog", u"Analyzer relevance scores", None))
        self.showAllAnalyzerRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.inputRadio.setText(QCoreApplication.translate("Dialog", u"Input", None))
        self.showAllInputRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.histNumOfBins.setText(QCoreApplication.translate("baseLayout", u"Number of bins", None))