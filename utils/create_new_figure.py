# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_figure_dialog_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(559, 280)
        self.baseFrame = QFrame(Dialog)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setGeometry(QRect(0, 0, 561, 281))
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.baseFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resetButton = QPushButton(self.baseFrame)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)

        self.cancelButton = QPushButton(self.baseFrame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.createButton = QPushButton(self.baseFrame)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout.addWidget(self.createButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.baseFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(100, 100))
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
        self.classCombo.addItem("")
        self.classCombo.addItem("")
        self.classCombo.addItem("")
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
        self.plotTypeCombo.addItem("")
        self.plotTypeCombo.setObjectName(u"plotTypeCombo")

        self.plotTypeLayout.addWidget(self.plotTypeCombo)


        self.verticalLayout.addLayout(self.plotTypeLayout)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        
        self.baseFrame_2 = QFrame(self.baseFrame)
        self.baseFrame_2.setObjectName(u"baseFrame_2")
        self.baseFrame_2.setFrameShape(QFrame.StyledPanel)
        self.baseFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.baseFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.channelsFrame = QFrame(self.baseFrame_2)
        self.channelsFrame.setObjectName(u"channelsFrame")
        self.channelsFrame.setFrameShape(QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.channelsFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.scatterFrame = QFrame(self.baseFrame_2)
        self.scatterFrame.setObjectName(u"scatterFrame")
        self.scatterFrame.setFrameShape(QFrame.StyledPanel)
        self.scatterFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.scatterFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scatterTitle = QLabel(self.scatterFrame)
        self.scatterTitle.setObjectName(u"scatterTitle")
        self.scatterTitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4.addWidget(self.scatterTitle, 0, 0, 1, 1)
        self.singleSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.singleSampleScatterRadio.setObjectName(u"singleSampleScatterRadio")
        self.gridLayout_4.addWidget(self.singleSampleScatterRadio, 1, 0, 1, 1)
        self.averageSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.averageSampleScatterRadio.setObjectName(u"averageSampleScatterRadio")
        self.gridLayout_4.addWidget(self.averageSampleScatterRadio, 2, 0, 1, 1)
        self.singleAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.singleAnalyzerScatterRadio.setObjectName(u"singleAnalyzerScatterRadio")
        self.gridLayout_4.addWidget(self.singleAnalyzerScatterRadio, 3, 0, 1, 1)
        self.averageAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.averageAnalyzerScatterRadio.setObjectName(u"averageAnalyzerScatterRadio")
        self.gridLayout_4.addWidget(self.averageAnalyzerScatterRadio, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.scatterFrame, 0, 1, 1, 1)
        self.LineFrame = QFrame(self.baseFrame_2)
        self.LineFrame.setObjectName(u"LineFrame")
        self.LineFrame.setFrameShape(QFrame.StyledPanel)
        self.LineFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.LineFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.linetitle = QLabel(self.LineFrame)
        self.linetitle.setObjectName(u"linetitle")
        self.linetitle.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5.addWidget(self.linetitle, 0, 0, 1, 1)
        self.singleSampleLineRadio = QRadioButton(self.LineFrame)
        self.singleSampleLineRadio.setObjectName(u"singleSampleLineRadio")
        self.gridLayout_5.addWidget(self.singleSampleLineRadio, 1, 0, 1, 1)
        self.averageSampleLineRadio = QRadioButton(self.LineFrame)
        self.averageSampleLineRadio.setObjectName(u"averageSampleLineRadio")
        self.gridLayout_5.addWidget(self.averageSampleLineRadio, 2, 0, 1, 1)
        self.singleAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.singleAnalyzerLineRadio.setObjectName(u"singleAnalyzerLineRadio")
        self.gridLayout_5.addWidget(self.singleAnalyzerLineRadio, 3, 0, 1, 1)
        self.averageAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.averageAnalyzerLineRadio.setObjectName(u"averageAnalyzerLineRadio")
        self.gridLayout_5.addWidget(self.averageAnalyzerLineRadio, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.LineFrame, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.baseFrame_2, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create new figure", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.createButton.setText(QCoreApplication.translate("Dialog", u"Create", None))
        self.classTitle.setText(QCoreApplication.translate("Dialog", u"Class", None))
        self.classCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Normal", None))
        self.classCombo.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))
        self.classCombo.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))

        self.predQualTitle.setText(QCoreApplication.translate("Dialog", u"Prediction quality", None))
        self.predQualCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Correct", None))
        self.predQualCombo.setItemText(1, QCoreApplication.translate("Dialog", u"All", None))
        self.predQualCombo.setItemText(2, QCoreApplication.translate("Dialog", u"Incorrect", None))
        self.predQualCombo.setItemText(3, QCoreApplication.translate("Dialog", u"False positive", None))
        self.predQualCombo.setItemText(4, QCoreApplication.translate("Dialog", u"False negative", None))

        self.plotTypeTitle.setText(QCoreApplication.translate("Dialog", u"Plot type", None))
        self.plotTypeCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Comparison", None))
        self.plotTypeCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Distribution", None))
        self.plotTypeCombo.setItemText(2, "")

        self.channelsTitle.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Dialog", u"Avarage sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Dialog", u"Avarage analyzer score", None))
        self.scatterTitle.setText(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.singleSampleScatterRadio.setText("")
        self.averageSampleScatterRadio.setText("")
        self.singleAnalyzerScatterRadio.setText("")
        self.averageAnalyzerScatterRadio.setText("")
        self.linetitle.setText(QCoreApplication.translate("Dialog", u"Line", None))
        self.singleSampleLineRadio.setText("")
        self.averageSampleLineRadio.setText("")
        self.singleAnalyzerLineRadio.setText("")
        self.averageAnalyzerLineRadio.setText("")
    # retranslateUi

