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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_baseLayout(object):
    def setupUi(self, baseLayout):
        if not baseLayout.objectName():
            baseLayout.setObjectName(u"baseLayout")
        baseLayout.resize(450, 325)
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

        self.boxEveryN = QLineEdit(self.boxFrame)
        self.boxEveryN.setObjectName(u"boxEveryN")

        self.gridLayout_2.addWidget(self.boxEveryN, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.boxFrame, 1, 0, 1, 1)

        self.histFrame = QFrame(self.baseFrame)
        self.histFrame.setObjectName(u"histFrame")
        self.histFrame.setFrameShape(QFrame.StyledPanel)
        self.histFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.histFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.histDetailesFrame = QFrame(self.histFrame)
        self.histDetailesFrame.setObjectName(u"histDetailesFrame")
        self.histDetailesFrame.setFrameShape(QFrame.StyledPanel)
        self.histDetailesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.histDetailesFrame)
        self.gridLayout.setObjectName(u"gridLayout")
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


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

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


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.histDetailesFrame, 2, 0, 1, 1)

        self.histRadio = QRadioButton(self.histFrame)
        self.histRadio.setObjectName(u"histRadio")

        self.gridLayout_3.addWidget(self.histRadio, 0, 0, 1, 1)

        self.histNumOfBins = QLineEdit(self.histFrame)
        self.histNumOfBins.setObjectName(u"histNumOfBins")

        self.gridLayout_3.addWidget(self.histNumOfBins, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.histFrame, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.baseFrame, 0, 0, 1, 1)


        self.retranslateUi(baseLayout)

        QMetaObject.connectSlotsByName(baseLayout)
    # setupUi

    def retranslateUi(self, baseLayout):
        baseLayout.setWindowTitle(QCoreApplication.translate("baseLayout", u"Form", None))
        self.figureTypeTitle.setText(QCoreApplication.translate("baseLayout", u"Figure type", None))
        self.boxRadio.setText(QCoreApplication.translate("baseLayout", u"Box plot", None))
        self.boxEveryN.setText(QCoreApplication.translate("baseLayout", u"Sample frequency", None))
        self.analyzerRadio.setText(QCoreApplication.translate("baseLayout", u"Analyzer relevance scores", None))
        self.inputRadio.setText(QCoreApplication.translate("baseLayout", u"Input", None))
        self.showAllAnalyzerRadio.setText(QCoreApplication.translate("baseLayout", u"Show all class", None))
        self.showAllInputRadio.setText(QCoreApplication.translate("baseLayout", u"Show all class", None))
        self.histRadio.setText(QCoreApplication.translate("baseLayout", u"Histogram", None))
        self.histNumOfBins.setText(QCoreApplication.translate("baseLayout", u"Number of bins", None))
    # retranslateUi

