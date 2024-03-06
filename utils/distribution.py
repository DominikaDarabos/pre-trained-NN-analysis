# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_dist_widget_UI.ui'
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
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QWidget)

class Ui_baseLayout(object):
    def setupUi(self, baseLayout):
        if not baseLayout.objectName():
            baseLayout.setObjectName(u"baseLayout")
        baseLayout.resize(385, 271)
        self.gridLayout_5 = QGridLayout(baseLayout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.baseFrame = QFrame(baseLayout)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.baseFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.figureTypeTitle = QLabel(self.baseFrame)
        self.figureTypeTitle.setObjectName(u"figureTypeTitle")
        self.figureTypeTitle.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.figureTypeTitle, 0, 0, 1, 1)

        self.boxFrame = QFrame(self.baseFrame)
        self.boxFrame.setObjectName(u"boxFrame")
        self.boxFrame.setFrameShape(QFrame.StyledPanel)
        self.boxFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.boxFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.boxRadio = QRadioButton(self.boxFrame)
        self.boxRadio.setObjectName(u"boxRadio")

        self.gridLayout_2.addWidget(self.boxRadio, 0, 0, 1, 1)

        self.numOfBinsInput = QLineEdit(self.boxFrame)
        self.numOfBinsInput.setObjectName(u"numOfBinsInput")

        self.gridLayout_2.addWidget(self.numOfBinsInput, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.boxFrame, 1, 0, 1, 1)

        self.histFrame = QFrame(self.baseFrame)
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
        self.gridLayout = QGridLayout(self.histDetailesFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AnalyzerCheckbow = QCheckBox(self.histDetailesFrame)
        self.AnalyzerCheckbow.setObjectName(u"AnalyzerCheckbow")

        self.gridLayout.addWidget(self.AnalyzerCheckbow, 0, 0, 1, 1)

        self.analyzerRadio = QRadioButton(self.histDetailesFrame)
        self.analyzerRadio.setObjectName(u"analyzerRadio")

        self.gridLayout.addWidget(self.analyzerRadio, 0, 1, 1, 1)

        self.inputCheckbox = QCheckBox(self.histDetailesFrame)
        self.inputCheckbox.setObjectName(u"inputCheckbox")

        self.gridLayout.addWidget(self.inputCheckbox, 1, 0, 1, 1)

        self.inputRadio = QRadioButton(self.histDetailesFrame)
        self.inputRadio.setObjectName(u"inputRadio")

        self.gridLayout.addWidget(self.inputRadio, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.histDetailesFrame, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.histFrame, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.baseFrame, 0, 0, 1, 1)


        self.retranslateUi(baseLayout)

        QMetaObject.connectSlotsByName(baseLayout)
    # setupUi

    def retranslateUi(self, baseLayout):
        baseLayout.setWindowTitle(QCoreApplication.translate("baseLayout", u"Form", None))
        self.figureTypeTitle.setText(QCoreApplication.translate("baseLayout", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("baseLayout", u"Box plot", None))
        self.numOfBinsInput.setText(QCoreApplication.translate("baseLayout", u"Number of bins", None))
        self.histRadio.setText(QCoreApplication.translate("baseLayout", u"Histogram", None))
        self.AnalyzerCheckbow.setText(QCoreApplication.translate("baseLayout", u"Analyzer relevance scores", None))
        self.analyzerRadio.setText(QCoreApplication.translate("baseLayout", u"Show all class", None))
        self.inputCheckbox.setText(QCoreApplication.translate("baseLayout", u"Input", None))
        self.inputRadio.setText(QCoreApplication.translate("baseLayout", u"Show all class", None))
    # retranslateUi

