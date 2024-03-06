# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_options_widget_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(376, 194)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.baseFrame = QFrame(Form)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.baseFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.channelsFrame = QFrame(self.baseFrame)
        self.channelsFrame.setObjectName(u"channelsFrame")
        self.channelsFrame.setFrameShape(QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.channelsFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.channelsTitle = QLabel(self.channelsFrame)
        self.channelsTitle.setObjectName(u"channelsTitle")
        self.channelsTitle.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.channelsTitle, 0, 0, 1, 1)

        self.singleSampleCheckbox = QCheckBox(self.channelsFrame)
        self.singleSampleCheckbox.setObjectName(u"singleSampleCheckbox")

        self.gridLayout_2.addWidget(self.singleSampleCheckbox, 1, 0, 1, 1)

        self.averageSampleCheckbox = QCheckBox(self.channelsFrame)
        self.averageSampleCheckbox.setObjectName(u"averageSampleCheckbox")

        self.gridLayout_2.addWidget(self.averageSampleCheckbox, 2, 0, 1, 1)

        self.singleAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.singleAnalyzerCheckbox.setObjectName(u"singleAnalyzerCheckbox")

        self.gridLayout_2.addWidget(self.singleAnalyzerCheckbox, 3, 0, 1, 1)

        self.averageAnalyzerCheckbox = QCheckBox(self.channelsFrame)
        self.averageAnalyzerCheckbox.setObjectName(u"averageAnalyzerCheckbox")

        self.gridLayout_2.addWidget(self.averageAnalyzerCheckbox, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.channelsFrame, 0, 0, 1, 1)

        self.scatterFrame = QFrame(self.baseFrame)
        self.scatterFrame.setObjectName(u"scatterFrame")
        self.scatterFrame.setFrameShape(QFrame.StyledPanel)
        self.scatterFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.scatterFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scatterTitle = QLabel(self.scatterFrame)
        self.scatterTitle.setObjectName(u"scatterTitle")
        self.scatterTitle.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.scatterTitle, 0, 0, 1, 1)

        self.singleSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.singleSampleScatterRadio.setObjectName(u"singleSampleScatterRadio")

        self.gridLayout_3.addWidget(self.singleSampleScatterRadio, 1, 0, 1, 1)

        self.averageSampleScatterRadio = QRadioButton(self.scatterFrame)
        self.averageSampleScatterRadio.setObjectName(u"averageSampleScatterRadio")

        self.gridLayout_3.addWidget(self.averageSampleScatterRadio, 2, 0, 1, 1)

        self.singleAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.singleAnalyzerScatterRadio.setObjectName(u"singleAnalyzerScatterRadio")

        self.gridLayout_3.addWidget(self.singleAnalyzerScatterRadio, 3, 0, 1, 1)

        self.averageAnalyzerScatterRadio = QRadioButton(self.scatterFrame)
        self.averageAnalyzerScatterRadio.setObjectName(u"averageAnalyzerScatterRadio")

        self.gridLayout_3.addWidget(self.averageAnalyzerScatterRadio, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.scatterFrame, 0, 1, 1, 1)

        self.LineFrame = QFrame(self.baseFrame)
        self.LineFrame.setObjectName(u"LineFrame")
        self.LineFrame.setFrameShape(QFrame.StyledPanel)
        self.LineFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.LineFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.linetitle = QLabel(self.LineFrame)
        self.linetitle.setObjectName(u"linetitle")
        self.linetitle.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.linetitle, 0, 0, 1, 1)

        self.singleSampleLineRadio = QRadioButton(self.LineFrame)
        self.singleSampleLineRadio.setObjectName(u"singleSampleLineRadio")

        self.gridLayout_4.addWidget(self.singleSampleLineRadio, 1, 0, 1, 1)

        self.averageSampleLineRadio = QRadioButton(self.LineFrame)
        self.averageSampleLineRadio.setObjectName(u"averageSampleLineRadio")

        self.gridLayout_4.addWidget(self.averageSampleLineRadio, 2, 0, 1, 1)

        self.singleAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.singleAnalyzerLineRadio.setObjectName(u"singleAnalyzerLineRadio")

        self.gridLayout_4.addWidget(self.singleAnalyzerLineRadio, 3, 0, 1, 1)

        self.averageAnalyzerLineRadio = QRadioButton(self.LineFrame)
        self.averageAnalyzerLineRadio.setObjectName(u"averageAnalyzerLineRadio")

        self.gridLayout_4.addWidget(self.averageAnalyzerLineRadio, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.LineFrame, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.baseFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.channelsTitle.setText(QCoreApplication.translate("Form", u"Channels", None))
        self.singleSampleCheckbox.setText(QCoreApplication.translate("Form", u"Single sample", None))
        self.averageSampleCheckbox.setText(QCoreApplication.translate("Form", u"Avarage sample over class", None))
        self.singleAnalyzerCheckbox.setText(QCoreApplication.translate("Form", u"Single analyzer score", None))
        self.averageAnalyzerCheckbox.setText(QCoreApplication.translate("Form", u"Avarage analyzer score", None))
        self.scatterTitle.setText(QCoreApplication.translate("Form", u"Scatter", None))
        self.singleSampleScatterRadio.setText("")
        self.averageSampleScatterRadio.setText("")
        self.singleAnalyzerScatterRadio.setText("")
        self.averageAnalyzerScatterRadio.setText("")
        self.linetitle.setText(QCoreApplication.translate("Form", u"Line", None))
        self.singleSampleLineRadio.setText("")
        self.averageSampleLineRadio.setText("")
        self.singleAnalyzerLineRadio.setText("")
        self.averageAnalyzerLineRadio.setText("")
    # retranslateUi

