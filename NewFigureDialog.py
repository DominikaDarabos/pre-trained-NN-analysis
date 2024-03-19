from PySide6 import QtWidgets
from utils import create_new_figure
from PySide6.QtWidgets import  QLabel, QFrame, QGridLayout, QCheckBox, QRadioButton, QLineEdit
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
    
    def create_figure(self):
        figure = Figure_()
        figure.config["class"] = self.classCombo.currentText().lower()
        figure.config["prediction_quality"] = self.predQualCombo.currentText().lower().replace(" ", "_")
        if self.plotTypeCombo.currentText() == "Comparison":
            figure.add_default_comparison()
            if self.singleSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"] = self.singleAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"] = self.singleSampleLineRadio_2.isChecked()
            if self.averageSampleCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"] = self.averageSampleScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"] = self.averageSampleLineRadio_2.isChecked()
            if self.singleAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["scatter"] = self.singleAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["line"] = self.singleAnalyzerLineRadio_2.isChecked()
            if self.averageAnalyzerCheckbox.isChecked():
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activation"] = True
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"] = self.averageAnalyzerScatterRadio_2.isChecked()
                figure.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"] = self.averageAnalyzerLineRadio_2.isChecked()
        elif self.plotTypeCombo.currentText() == "Distribution":
            figure.add_default_distribution()
            if self.boxRadio.isChecked():
                figure.config["plot_type"]["distribution"]["box_plot"]["avtivated"] = True
                if self.numOfBinsInput.text().isnumeric():
                    figure.config["plot_type"]["distribution"]["box_plot"]["num_of_bins"] = int(self.numOfBinsInput.text())
                else:
                    figure.config["plot_type"]["distribution"]["box_plot"]["num_of_bins"] = 30
            if self.histRadio.isChecked():
                figure.config["plot_type"]["distribution"]["histogram"]["avtivated"] = True
                if self.analyzerRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["show_all_class"] = self.analyzerRadio.isChecked()
                if self.inputRadio.isChecked():
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["activated"] = True
                    figure.config["plot_type"]["distribution"]["histogram"]["input"]["show_all_class"] = self.inputRadio.isChecked()
        
        if self.place == 0:
            self.app.create_new_comparison_figure("upper", figure)
            analyzer = self.app.get_current_analyzer()
            self.app.projects[0].config["analyzers"][analyzer][f"upper_figures"].append(figure)

            currentcount = self.app.projects[0].config["analyzers"][analyzer][f"upper_plot_count"]
            print(self.app.projects[0].config["analyzers"][analyzer][f"upper_figures"][currentcount-1])
        elif self.place == 1:
            self.app.create_new_comparison_figure("bottom", figure)
            analyzer = self.app.get_current_analyzer()
            self.app.projects[0].config["analyzers"][analyzer][f"bottom_figures"].append(figure)

            currentcount = self.app.projects[0].config["analyzers"][analyzer][f"bottom_plot_count"]
            print(self.app.projects[0].config["analyzers"][analyzer][f"bottom_figures"][currentcount-1])
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
        self.singleAnalyzerLineRadio_2 = QRadioButton(self.averageSampleFrame)
        self.singleAnalyzerLineRadio_2.setObjectName(u"singleAnalyzerLineRadio_2")
        self.gridLayout_8.addWidget(self.singleAnalyzerLineRadio_2, 0, 0, 1, 1)
        self.singleAnalyzerScatterRadio_2 = QRadioButton(self.averageSampleFrame)
        self.singleAnalyzerScatterRadio_2.setObjectName(u"singleAnalyzerScatterRadio_2")
        self.gridLayout_8.addWidget(self.singleAnalyzerScatterRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageSampleFrame, 2, 0, 1, 1)
        self.singleAnalyzerFrame = QFrame(self.radioFrame)
        self.singleAnalyzerFrame.setObjectName(u"singleAnalyzerFrame")
        self.singleAnalyzerFrame.setFrameShape(QFrame.StyledPanel)
        self.singleAnalyzerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.singleAnalyzerFrame)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.averageAnalyzerScatterRadio_2 = QRadioButton(self.singleAnalyzerFrame)
        self.averageAnalyzerScatterRadio_2.setObjectName(u"averageAnalyzerScatterRadio_2")
        self.gridLayout_9.addWidget(self.averageAnalyzerScatterRadio_2, 0, 0, 1, 1)
        self.averageAnalyzerLineRadio_2 = QRadioButton(self.singleAnalyzerFrame)
        self.averageAnalyzerLineRadio_2.setObjectName(u"averageAnalyzerLineRadio_2")
        self.gridLayout_9.addWidget(self.averageAnalyzerLineRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.singleAnalyzerFrame, 3, 0, 1, 1)
        self.singleSampleFrame = QFrame(self.radioFrame)
        self.singleSampleFrame.setObjectName(u"singleSampleFrame")
        self.singleSampleFrame.setFrameShape(QFrame.StyledPanel)
        self.singleSampleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.singleSampleFrame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.singleSampleLineRadio_2 = QRadioButton(self.singleSampleFrame)
        self.singleSampleLineRadio_2.setObjectName(u"singleSampleLineRadio_2")
        self.gridLayout_7.addWidget(self.singleSampleLineRadio_2, 0, 0, 1, 1)
        self.singleSampleScatterRadio_2 = QRadioButton(self.singleSampleFrame)
        self.singleSampleScatterRadio_2.setObjectName(u"singleSampleScatterRadio_2")
        self.gridLayout_7.addWidget(self.singleSampleScatterRadio_2, 0, 1, 1, 1)
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
        self.averageSampleLineRadio_2 = QRadioButton(self.averageAnalyzerFrame)
        self.averageSampleLineRadio_2.setObjectName(u"averageSampleLineRadio_2")
        self.gridLayout_10.addWidget(self.averageSampleLineRadio_2, 0, 0, 1, 1)
        self.averageSampleScatterRadio_2 = QRadioButton(self.averageAnalyzerFrame)
        self.averageSampleScatterRadio_2.setObjectName(u"averageSampleScatterRadio_2")
        self.gridLayout_10.addWidget(self.averageSampleScatterRadio_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageAnalyzerFrame, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.radioFrame, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)



        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Average sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Average analyzer score", None))
        self.singleAnalyzerLineRadio_2.setText("")
        self.singleAnalyzerScatterRadio_2.setText("")
        self.averageAnalyzerScatterRadio_2.setText("")
        self.averageAnalyzerLineRadio_2.setText("")
        self.singleSampleLineRadio_2.setText("")
        self.singleSampleScatterRadio_2.setText("")
        self.scatterTitle_2.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.linetitle_2.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.averageSampleLineRadio_2.setText("")
        self.averageSampleScatterRadio_2.setText("")
    
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
        self.numOfBinsInput = QLineEdit(self.boxFrame)
        self.numOfBinsInput.setObjectName(u"numOfBinsInput")
        self.gridLayout_6.addWidget(self.numOfBinsInput, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.boxFrame, 1, 0, 1, 1)
        self.histFrame = QFrame(self.baseFrame_2)
        self.histFrame.setObjectName(u"histFrame")
        self.histFrame.setFrameShape(QFrame.StyledPanel)
        self.histFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.histFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.histRadio = QRadioButton(self.histFrame)
        self.histRadio.setObjectName(u"histRadio")
        self.gridLayout_3.addWidget(self.histRadio, 0, 0, 1, 1)
        self.histDetailesFrame = QFrame(self.histFrame)
        self.histDetailesFrame.setObjectName(u"histDetailesFrame")
        self.histDetailesFrame.setFrameShape(QFrame.StyledPanel)
        self.histDetailesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.histDetailesFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.analyzerRadio = QRadioButton(self.histDetailesFrame)
        self.analyzerRadio.setObjectName(u"analyzerRadio")
        self.gridLayout_5.addWidget(self.analyzerRadio, 0, 0, 1, 1)
        #self.analyzerRadio = QRadioButton(self.histDetailesFrame)
        #self.analyzerRadio.setObjectName(u"analyzerRadio")
        #self.gridLayout_5.addWidget(self.analyzerRadio, 0, 1, 1, 1)
        self.inputRadio = QRadioButton(self.histDetailesFrame)
        self.inputRadio.setObjectName(u"inputRadio")
        self.gridLayout_5.addWidget(self.inputRadio, 1, 0, 1, 1)
        #self.inputRadio = QRadioButton(self.histDetailesFrame)
        #self.inputRadio.setObjectName(u"inputRadio")
        #self.gridLayout_5.addWidget(self.inputRadio, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.histDetailesFrame, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.histFrame, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)

        self.figureTypeTitle.setText(QCoreApplication.translate("Dialog", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("Dialog", u"Box plot", None))
        self.numOfBinsInput.setText(QCoreApplication.translate("Dialog", u"Number of bins", None))
        self.histRadio.setText(QCoreApplication.translate("Dialog", u"Histogram", None))
        self.analyzerRadio.setText(QCoreApplication.translate("Dialog", u"Analyzer relevance scores", None))
        #self.analyzerRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.inputRadio.setText(QCoreApplication.translate("Dialog", u"Input", None))
        #self.inputRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))