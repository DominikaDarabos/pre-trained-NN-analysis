# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_figure_dialog_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QVBoxLayout, QButtonGroup, QLineEdit)
"""
Setting up the default UI elements for NewFigureDialog.
"""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(589, 292)
        self.gridLayout_6 = QGridLayout(Dialog)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.baseFrame = QFrame(Dialog)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.baseFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.baseFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 200))
        self.frame_2.setMaximumSize(QSize(150, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.classLayout = QVBoxLayout()
        self.classLayout.setSpacing(0)
        self.classLayout.setObjectName(u"classLayout")
        self.classTitle = QLabel(self.frame_2)
        self.classTitle.setObjectName(u"classTitle")
        self.classTitle.setMaximumSize(QSize(16777215, 25))
        self.classLayout.addWidget(self.classTitle)
        self.classCombo = QComboBox(self.frame_2)
        self.classCombo.setObjectName(u"classCombo")
        self.classLayout.addWidget(self.classCombo)
        self.verticalLayout.addLayout(self.classLayout)
        self.predQualLayout = QVBoxLayout()
        self.predQualLayout.setObjectName(u"predQualLayout")
        self.predQualTitle = QLabel(self.frame_2)
        self.predQualTitle.setObjectName(u"predQualTitle")
        self.predQualTitle.setMaximumSize(QSize(16777215, 25))
        self.predQualLayout.addWidget(self.predQualTitle)
        self.predQualCombo = QComboBox(self.frame_2)
        self.predQualCombo.addItem("")
        self.predQualCombo.addItem("")
        self.predQualCombo.addItem("")
        self.predQualCombo.addItem("")
        self.predQualCombo.setObjectName(u"predQualCombo")
        self.predQualLayout.addWidget(self.predQualCombo)
        self.verticalLayout.addLayout(self.predQualLayout)
        self.plotTypeLayout = QVBoxLayout()
        self.plotTypeLayout.setObjectName(u"plotTypeLayout")
        self.plotTypeTitle = QLabel(self.frame_2)
        self.plotTypeTitle.setObjectName(u"plotTypeTitle")
        self.plotTypeTitle.setMaximumSize(QSize(16777215, 25))
        self.plotTypeLayout.addWidget(self.plotTypeTitle)
        self.plotTypeCombo = QComboBox(self.frame_2)
        self.plotTypeCombo.addItem("")
        self.plotTypeCombo.addItem("")
        self.plotTypeCombo.setObjectName(u"plotTypeCombo")
        self.plotTypeLayout.addWidget(self.plotTypeCombo)
        self.verticalLayout.addLayout(self.plotTypeLayout)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.cancelButton = QPushButton(self.baseFrame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.createButton = QPushButton(self.baseFrame)
        self.createButton.setObjectName(u"createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.baseFrame_2 = QFrame(self.baseFrame)
        self.baseFrame_2.setMinimumSize(400, 300)
        self.baseFrame_2.setMaximumSize(400, 300)
        self.baseFrame_2.setObjectName(u"baseFrame_2")
        self.baseFrame_2.setFrameShape(QFrame.StyledPanel)
        self.baseFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.baseFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_6.addWidget(self.baseFrame, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create new figure", None))
        self.classTitle.setText(QCoreApplication.translate("Dialog", u"Class", None))
        self.predQualTitle.setText(QCoreApplication.translate("Dialog", u"Prediction quality", None))
        self.predQualCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Correct", None))
        self.predQualCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Incorrect", None))
        self.predQualCombo.setItemText(2, QCoreApplication.translate("Dialog", u"False positive", None))
        self.predQualCombo.setItemText(3, QCoreApplication.translate("Dialog", u"False negative", None))
        self.plotTypeTitle.setText(QCoreApplication.translate("Dialog", u"Plot type", None))
        self.plotTypeCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Comparison", None))
        self.plotTypeCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Distribution", None))
        self.plotTypeCombo.setItemText(2, "")
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.createButton.setText(QCoreApplication.translate("Dialog", u"Create", None))

    def setup_widgets_for_comparison(self):
        """
        Necessary UI object for the comparison figures.
        """
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
        self.singleSampleCheckbox.setToolTip("One randomized input")
        self.singleSampleCheckbox.setObjectName(u"singleSampleCheckbox")
        self.gridLayout_3.addWidget(self.singleSampleCheckbox, 1, 0, 1, 1)
        self.averageSampleCheckbox = QCheckBox(self.channelsFrame)
        self.averageSampleCheckbox.setToolTip("All input is averaged into one representative")
        self.averageSampleCheckbox.setObjectName(u"averageSampleCheckbox")
        self.gridLayout_3.addWidget(self.averageSampleCheckbox, 2, 0, 1, 1)
        self.averageAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.averageAnalyzerCheckbox.setToolTip("All analyzer relevance scores is averaged into one representative")
        self.averageAnalyzerCheckbox.setObjectName(u"averageAnalyzerCheckbox")
        self.gridLayout_3.addWidget(self.averageAnalyzerCheckbox, 3, 0, 1, 1)
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
        self.averageSampleLineRadio.setChecked(True)
        self.gridLayout_8.addWidget(self.averageSampleLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageSampleFrame, 2, 0, 1, 1)
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
        self.singleSampleLineRadio.setChecked(True)
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
        self.averageAnalyzerLineRadio.setChecked(True)
        self.gridLayout_10.addWidget(self.averageAnalyzerLineRadio, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.averageAnalyzerFrame, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.radioFrame, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)
        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single input", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Average input over class", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Average analyzer score", None))
        self.averageSampleScatterRadio.setText("")
        self.averageSampleLineRadio.setText("")
        self.singleSampleScatterRadio.setText("")
        self.singleSampleLineRadio.setText("")
        self.scatterTitle_2.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.linetitle_2.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.averageAnalyzerScatterRadio.setText("")
        self.averageAnalyzerLineRadio.setText("")

        if self.predQualCombo.count() == 5:
            self.predQualCombo.removeItem(4)
    
    def setup_widgets_for_distribution(self):
        """
        Necessary UI object for the distribution figures.
        """
        self.buttonGroup = QButtonGroup(self)
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
        self.buttonGroup.addButton(self.boxRadio)
        self.gridLayout_6.addWidget(self.boxRadio, 0, 0, 1, 1)
        self.boxEveryN = QLineEdit(self.boxFrame)
        self.boxEveryN.setToolTip("Every which element should be plotted.")
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
        self.buttonGroup.addButton(self.histRadio)
        self.gridLayout_3.addWidget(self.histRadio, 0, 0, 1, 1)
        self.histNumOfBins = QLineEdit(self.histFrame)
        self.histNumOfBins.setObjectName(u"histNumOfBins")
        self.gridLayout_3.addWidget(self.histNumOfBins, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.histFrame, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)
        self.figureTypeTitle.setText(QCoreApplication.translate("Dialog", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("Dialog", u"Box plot", None))
        self.boxEveryN.setText(QCoreApplication.translate("Dialog", u"Recording frequency (default 50)", None))
        self.histRadio.setText(QCoreApplication.translate("Dialog", u"Histogram", None))
        self.analyzerRadio.setText(QCoreApplication.translate("Dialog", u"Analyzer relevance scores", None))
        self.showAllAnalyzerRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.inputRadio.setText(QCoreApplication.translate("Dialog", u"Input", None))
        self.showAllInputRadio.setText(QCoreApplication.translate("Dialog", u"Show all class", None))
        self.histNumOfBins.setText(QCoreApplication.translate("baseLayout", u"Number of bins (default 30)", None))
        self.predQualCombo.insertItem(4, "Ground truth")


