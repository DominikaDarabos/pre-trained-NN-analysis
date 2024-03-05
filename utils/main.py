# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyzer_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 785)
        self.baseWidget = QWidget(MainWindow)
        self.baseWidget.setObjectName(u"baseWidget")
        self.gridLayout = QGridLayout(self.baseWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.baseFrame = QFrame(self.baseWidget)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.baseFrame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.baseFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenuFrame = QFrame(self.baseFrame)
        self.sideMenuFrame.setObjectName(u"sideMenuFrame")
        self.sideMenuFrame.setMinimumSize(QSize(150, 0))
        self.sideMenuFrame.setMaximumSize(QSize(250, 16777215))
        self.sideMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.sideMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sideMenuFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.sideMenuFrame)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(150, 0))
        self.menuButton.setMaximumSize(QSize(250, 25))

        self.verticalLayout.addWidget(self.menuButton)

        self.listWidget = QListWidget(self.sideMenuFrame)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.sideMenuFrame)

        self.modelArea = QTabWidget(self.baseFrame)
        self.modelArea.setObjectName(u"modelArea")
        self.modelArea.setMinimumSize(QSize(400, 0))
        self.modelArea.setMaximumSize(QSize(2000, 16777215))
        self.model_1 = QWidget()
        self.model_1.setObjectName(u"model_1")
        self.model_1.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.model_1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoPanelFrame = QFrame(self.model_1)
        self.infoPanelFrame.setObjectName(u"infoPanelFrame")
        self.infoPanelFrame.setMinimumSize(QSize(300, 0))
        self.infoPanelFrame.setMaximumSize(QSize(800, 16777215))
        self.infoPanelFrame.setAutoFillBackground(False)
        self.infoPanelFrame.setFrameShape(QFrame.StyledPanel)
        self.infoPanelFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.infoPanelFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.inputOutputInfoFrame = QFrame(self.infoPanelFrame)
        self.inputOutputInfoFrame.setObjectName(u"inputOutputInfoFrame")
        self.inputOutputInfoFrame.setMaximumSize(QSize(16777215, 150))
        self.inputOutputInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.inputOutputInfoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.inputOutputInfoFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.InputInfoFrame = QFrame(self.inputOutputInfoFrame)
        self.InputInfoFrame.setObjectName(u"InputInfoFrame")
        self.InputInfoFrame.setMinimumSize(QSize(0, 0))
        self.InputInfoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.InputInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.InputInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.InputInfoFrame)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.inputDataTitle = QLabel(self.InputInfoFrame)
        self.inputDataTitle.setObjectName(u"inputDataTitle")

        self.verticalLayout_9.addWidget(self.inputDataTitle)

        self.inputDataInfo = QTextBrowser(self.InputInfoFrame)
        self.inputDataInfo.setObjectName(u"inputDataInfo")
        self.inputDataInfo.setMinimumSize(QSize(0, 0))
        self.inputDataInfo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.inputDataInfo)


        self.gridLayout_9.addWidget(self.InputInfoFrame, 0, 0, 1, 1)

        self.OutputInfoFrame = QFrame(self.inputOutputInfoFrame)
        self.OutputInfoFrame.setObjectName(u"OutputInfoFrame")
        self.OutputInfoFrame.setMinimumSize(QSize(0, 0))
        self.OutputInfoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.OutputInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.OutputInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.OutputInfoFrame)
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.outputDataTitle = QLabel(self.OutputInfoFrame)
        self.outputDataTitle.setObjectName(u"outputDataTitle")

        self.verticalLayout_10.addWidget(self.outputDataTitle)

        self.outputDataInfo = QTextBrowser(self.OutputInfoFrame)
        self.outputDataInfo.setObjectName(u"outputDataInfo")
        self.outputDataInfo.setMinimumSize(QSize(0, 0))
        self.outputDataInfo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_10.addWidget(self.outputDataInfo)


        self.gridLayout_9.addWidget(self.OutputInfoFrame, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.inputOutputInfoFrame, 0, 0, 1, 1)

        self.modelValidationInfoFrame = QFrame(self.infoPanelFrame)
        self.modelValidationInfoFrame.setObjectName(u"modelValidationInfoFrame")
        self.modelValidationInfoFrame.setMaximumSize(QSize(16777215, 150))
        self.modelValidationInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.modelValidationInfoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.modelValidationInfoFrame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.validationInfoFrame = QFrame(self.modelValidationInfoFrame)
        self.validationInfoFrame.setObjectName(u"validationInfoFrame")
        self.validationInfoFrame.setMinimumSize(QSize(0, 0))
        self.validationInfoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.validationInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.validationInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.validationInfoFrame)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.validationTitle = QLabel(self.validationInfoFrame)
        self.validationTitle.setObjectName(u"validationTitle")

        self.verticalLayout_8.addWidget(self.validationTitle)

        self.validationInfo = QTextBrowser(self.validationInfoFrame)
        self.validationInfo.setObjectName(u"validationInfo")
        self.validationInfo.setMinimumSize(QSize(0, 0))
        self.validationInfo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.validationInfo)


        self.gridLayout_8.addWidget(self.validationInfoFrame, 0, 0, 1, 1)

        self.modelInfoFrame = QFrame(self.modelValidationInfoFrame)
        self.modelInfoFrame.setObjectName(u"modelInfoFrame")
        self.modelInfoFrame.setMinimumSize(QSize(0, 0))
        self.modelInfoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.modelInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.modelInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.modelInfoFrame)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.modelDataTitle = QLabel(self.modelInfoFrame)
        self.modelDataTitle.setObjectName(u"modelDataTitle")

        self.verticalLayout_11.addWidget(self.modelDataTitle)

        self.modelInfo = QTextBrowser(self.modelInfoFrame)
        self.modelInfo.setObjectName(u"modelInfo")
        self.modelInfo.setMinimumSize(QSize(0, 0))
        self.modelInfo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_11.addWidget(self.modelInfo)


        self.gridLayout_8.addWidget(self.modelInfoFrame, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.modelValidationInfoFrame, 1, 0, 1, 1)

        self.dynamicFrame = QFrame(self.infoPanelFrame)
        self.dynamicFrame.setObjectName(u"dynamicFrame")
        self.dynamicFrame.setMinimumSize(QSize(0, 370))
        self.dynamicFrame.setFrameShape(QFrame.StyledPanel)
        self.dynamicFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dynamicFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dynamicTitle = QLabel(self.dynamicFrame)
        self.dynamicTitle.setObjectName(u"dynamicTitle")
        self.dynamicTitle.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.dynamicTitle)

        self.graphicsView = QGraphicsView(self.dynamicFrame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)


        self.gridLayout_7.addWidget(self.dynamicFrame, 2, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.infoPanelFrame, 0, 1, 1, 1)

        self.plotPanelFrame = QFrame(self.model_1)
        self.plotPanelFrame.setObjectName(u"plotPanelFrame")
        self.plotPanelFrame.setMinimumSize(QSize(600, 0))
        self.plotPanelFrame.setMaximumSize(QSize(1200, 16777215))
        self.plotPanelFrame.setFrameShape(QFrame.StyledPanel)
        self.plotPanelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.plotPanelFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.upperPlotTabWidget = QTabWidget(self.plotPanelFrame)
        self.upperPlotTabWidget.setObjectName(u"upperPlotTabWidget")
        self.upperPlotTab_1 = QWidget()
        self.upperPlotTab_1.setObjectName(u"upperPlotTab_1")
        self.gridLayout_3 = QGridLayout(self.upperPlotTab_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.upperFigureInfoFrame_1 = QFrame(self.upperPlotTab_1)
        self.upperFigureInfoFrame_1.setObjectName(u"upperFigureInfoFrame_1")
        self.upperFigureInfoFrame_1.setMinimumSize(QSize(100, 0))
        self.upperFigureInfoFrame_1.setMaximumSize(QSize(200, 16777215))
        self.upperFigureInfoFrame_1.setFrameShape(QFrame.StyledPanel)
        self.upperFigureInfoFrame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.upperFigureInfoFrame_1)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.upperFigureAttributes_1 = QTextBrowser(self.upperFigureInfoFrame_1)
        self.upperFigureAttributes_1.setObjectName(u"upperFigureAttributes_1")
        self.upperFigureAttributes_1.setMinimumSize(QSize(100, 100))
        self.upperFigureAttributes_1.setMaximumSize(QSize(200, 250))

        self.gridLayout_5.addWidget(self.upperFigureAttributes_1, 0, 0, 1, 1)

        self.upperChannelsFrame_1 = QFrame(self.upperFigureInfoFrame_1)
        self.upperChannelsFrame_1.setObjectName(u"upperChannelsFrame_1")
        self.upperChannelsFrame_1.setMinimumSize(QSize(100, 100))
        self.upperChannelsFrame_1.setMaximumSize(QSize(200, 250))
        self.upperChannelsFrame_1.setFrameShape(QFrame.StyledPanel)
        self.upperChannelsFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.upperChannelsFrame_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.UpperPlot_1_Channel_1 = QCheckBox(self.upperChannelsFrame_1)
        self.UpperPlot_1_Channel_1.setObjectName(u"UpperPlot_1_Channel_1")

        self.verticalLayout_3.addWidget(self.UpperPlot_1_Channel_1)

        self.UpperPlot_1_Channel_2 = QCheckBox(self.upperChannelsFrame_1)
        self.UpperPlot_1_Channel_2.setObjectName(u"UpperPlot_1_Channel_2")

        self.verticalLayout_3.addWidget(self.UpperPlot_1_Channel_2)

        self.UpperPlot_1_Channel_3 = QCheckBox(self.upperChannelsFrame_1)
        self.UpperPlot_1_Channel_3.setObjectName(u"UpperPlot_1_Channel_3")

        self.verticalLayout_3.addWidget(self.UpperPlot_1_Channel_3)

        self.UpperPlot_1_Channel_4 = QCheckBox(self.upperChannelsFrame_1)
        self.UpperPlot_1_Channel_4.setObjectName(u"UpperPlot_1_Channel_4")

        self.verticalLayout_3.addWidget(self.UpperPlot_1_Channel_4)

        self.UpperPlot_1_Channel_5 = QCheckBox(self.upperChannelsFrame_1)
        self.UpperPlot_1_Channel_5.setObjectName(u"UpperPlot_1_Channel_5")

        self.verticalLayout_3.addWidget(self.UpperPlot_1_Channel_5)


        self.gridLayout_5.addWidget(self.upperChannelsFrame_1, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.upperFigureInfoFrame_1, 0, 2, 1, 1)

        self.upperPlot_1 = QGraphicsView(self.upperPlotTab_1)
        self.upperPlot_1.setObjectName(u"upperPlot_1")
        self.upperPlot_1.setMinimumSize(QSize(400, 0))

        self.gridLayout_3.addWidget(self.upperPlot_1, 0, 1, 1, 1)

        self.upperPlotTabWidget.addTab(self.upperPlotTab_1, "")

        self.verticalLayout_12.addWidget(self.upperPlotTabWidget)

        self.upper_new_plot_button = QPushButton(self.plotPanelFrame)
        self.upper_new_plot_button.setObjectName(u"upper_new_plot_button")

        self.verticalLayout_12.addWidget(self.upper_new_plot_button, 0, Qt.AlignRight)

        self.bottomPlotTabWidget = QTabWidget(self.plotPanelFrame)
        self.bottomPlotTabWidget.setObjectName(u"bottomPlotTabWidget")
        self.bottomPlotTab_1 = QWidget()
        self.bottomPlotTab_1.setObjectName(u"bottomPlotTab_1")
        self.gridLayout_4 = QGridLayout(self.bottomPlotTab_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.bottomPlot_1 = QGraphicsView(self.bottomPlotTab_1)
        self.bottomPlot_1.setObjectName(u"bottomPlot_1")
        self.bottomPlot_1.setMinimumSize(QSize(400, 0))

        self.gridLayout_4.addWidget(self.bottomPlot_1, 0, 0, 1, 1)

        self.bottomFigureInfoFrame_1 = QFrame(self.bottomPlotTab_1)
        self.bottomFigureInfoFrame_1.setObjectName(u"bottomFigureInfoFrame_1")
        self.bottomFigureInfoFrame_1.setMinimumSize(QSize(100, 0))
        self.bottomFigureInfoFrame_1.setMaximumSize(QSize(200, 16777215))
        self.bottomFigureInfoFrame_1.setFrameShape(QFrame.StyledPanel)
        self.bottomFigureInfoFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bottomFigureInfoFrame_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.bottomFigureAttributes_1 = QTextBrowser(self.bottomFigureInfoFrame_1)
        self.bottomFigureAttributes_1.setObjectName(u"bottomFigureAttributes_1")
        self.bottomFigureAttributes_1.setMinimumSize(QSize(100, 100))
        self.bottomFigureAttributes_1.setMaximumSize(QSize(200, 250))

        self.verticalLayout_5.addWidget(self.bottomFigureAttributes_1)

        self.bottomChannelsFrame_1 = QFrame(self.bottomFigureInfoFrame_1)
        self.bottomChannelsFrame_1.setObjectName(u"bottomChannelsFrame_1")
        self.bottomChannelsFrame_1.setMinimumSize(QSize(100, 100))
        self.bottomChannelsFrame_1.setMaximumSize(QSize(200, 250))
        self.bottomChannelsFrame_1.setFrameShape(QFrame.StyledPanel)
        self.bottomChannelsFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottomChannelsFrame_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bottomPlot_1_Channel_1 = QCheckBox(self.bottomChannelsFrame_1)
        self.bottomPlot_1_Channel_1.setObjectName(u"bottomPlot_1_Channel_1")

        self.verticalLayout_4.addWidget(self.bottomPlot_1_Channel_1)

        self.bottomPlot_1_Channel_2 = QCheckBox(self.bottomChannelsFrame_1)
        self.bottomPlot_1_Channel_2.setObjectName(u"bottomPlot_1_Channel_2")

        self.verticalLayout_4.addWidget(self.bottomPlot_1_Channel_2)

        self.bottomPlot_1_Channel_3 = QCheckBox(self.bottomChannelsFrame_1)
        self.bottomPlot_1_Channel_3.setObjectName(u"bottomPlot_1_Channel_3")

        self.verticalLayout_4.addWidget(self.bottomPlot_1_Channel_3)

        self.bottomPlot_1_Channel_4 = QCheckBox(self.bottomChannelsFrame_1)
        self.bottomPlot_1_Channel_4.setObjectName(u"bottomPlot_1_Channel_4")

        self.verticalLayout_4.addWidget(self.bottomPlot_1_Channel_4)

        self.bottomPlot_1_Channel_5 = QCheckBox(self.bottomChannelsFrame_1)
        self.bottomPlot_1_Channel_5.setObjectName(u"bottomPlot_1_Channel_5")

        self.verticalLayout_4.addWidget(self.bottomPlot_1_Channel_5)


        self.verticalLayout_5.addWidget(self.bottomChannelsFrame_1)


        self.gridLayout_4.addWidget(self.bottomFigureInfoFrame_1, 0, 1, 1, 1)

        self.bottomPlotTabWidget.addTab(self.bottomPlotTab_1, "")
        self.bottomPlotTab_2 = QWidget()
        self.bottomPlotTab_2.setObjectName(u"bottomPlotTab_2")
        self.gridLayout_6 = QGridLayout(self.bottomPlotTab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.bottomPlot_2 = QGraphicsView(self.bottomPlotTab_2)
        self.bottomPlot_2.setObjectName(u"bottomPlot_2")
        self.bottomPlot_2.setMinimumSize(QSize(400, 0))

        self.gridLayout_6.addWidget(self.bottomPlot_2, 0, 0, 1, 1)

        self.bottomFigureInfoFrame_2 = QFrame(self.bottomPlotTab_2)
        self.bottomFigureInfoFrame_2.setObjectName(u"bottomFigureInfoFrame_2")
        self.bottomFigureInfoFrame_2.setMinimumSize(QSize(100, 0))
        self.bottomFigureInfoFrame_2.setMaximumSize(QSize(200, 16777215))
        self.bottomFigureInfoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.bottomFigureInfoFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottomFigureInfoFrame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.bottomFigureAttributes_2 = QTextBrowser(self.bottomFigureInfoFrame_2)
        self.bottomFigureAttributes_2.setObjectName(u"bottomFigureAttributes_2")
        self.bottomFigureAttributes_2.setMinimumSize(QSize(100, 100))
        self.bottomFigureAttributes_2.setMaximumSize(QSize(200, 250))

        self.verticalLayout_6.addWidget(self.bottomFigureAttributes_2)

        self.bottomChannelsFrame_2 = QFrame(self.bottomFigureInfoFrame_2)
        self.bottomChannelsFrame_2.setObjectName(u"bottomChannelsFrame_2")
        self.bottomChannelsFrame_2.setMinimumSize(QSize(100, 100))
        self.bottomChannelsFrame_2.setMaximumSize(QSize(200, 250))
        self.bottomChannelsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.bottomChannelsFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.bottomChannelsFrame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bottomPlot_2_Channel_1 = QCheckBox(self.bottomChannelsFrame_2)
        self.bottomPlot_2_Channel_1.setObjectName(u"bottomPlot_2_Channel_1")

        self.verticalLayout_7.addWidget(self.bottomPlot_2_Channel_1)

        self.bottomPlot_2_Channel_2 = QCheckBox(self.bottomChannelsFrame_2)
        self.bottomPlot_2_Channel_2.setObjectName(u"bottomPlot_2_Channel_2")

        self.verticalLayout_7.addWidget(self.bottomPlot_2_Channel_2)

        self.bottomPlot_2_Channel_3 = QCheckBox(self.bottomChannelsFrame_2)
        self.bottomPlot_2_Channel_3.setObjectName(u"bottomPlot_2_Channel_3")

        self.verticalLayout_7.addWidget(self.bottomPlot_2_Channel_3)

        self.bottomPlot_2_Channel_4 = QCheckBox(self.bottomChannelsFrame_2)
        self.bottomPlot_2_Channel_4.setObjectName(u"bottomPlot_2_Channel_4")

        self.verticalLayout_7.addWidget(self.bottomPlot_2_Channel_4)

        self.bottomPlot_2_Channel_5 = QCheckBox(self.bottomChannelsFrame_2)
        self.bottomPlot_2_Channel_5.setObjectName(u"bottomPlot_2_Channel_5")

        self.verticalLayout_7.addWidget(self.bottomPlot_2_Channel_5)


        self.verticalLayout_6.addWidget(self.bottomChannelsFrame_2)


        self.gridLayout_6.addWidget(self.bottomFigureInfoFrame_2, 0, 1, 1, 1)

        self.bottomPlotTabWidget.addTab(self.bottomPlotTab_2, "")

        self.verticalLayout_12.addWidget(self.bottomPlotTabWidget)

        self.bottom_new_plot_button = QPushButton(self.plotPanelFrame)
        self.bottom_new_plot_button.setObjectName(u"bottom_new_plot_button")

        self.verticalLayout_12.addWidget(self.bottom_new_plot_button, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.plotPanelFrame, 0, 0, 1, 1)

        self.modelArea.addTab(self.model_1, "")

        self.horizontalLayout.addWidget(self.modelArea)


        self.gridLayout.addWidget(self.baseFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.baseWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.modelArea.setCurrentIndex(0)
        self.upperPlotTabWidget.setCurrentIndex(0)
        self.bottomPlotTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.inputDataTitle.setText(QCoreApplication.translate("MainWindow", u"Input Data", None))
        self.inputDataInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SIze</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shape</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">first and last x element</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><br /></p></body></html>", None))
        self.outputDataTitle.setText(QCoreApplication.translate("MainWindow", u"Output Data", None))
        self.outputDataInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SIze</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shape</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">first and last x element</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><br /></p></body></html>", None))
        self.validationTitle.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.validationInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">compare the output and the gorund truth labels</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.modelDataTitle.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.modelInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">layer infos</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.dynamicTitle.setText(QCoreApplication.translate("MainWindow", u"Model graph", None))
        self.upperFigureAttributes_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Figure attributes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\""
                        "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.UpperPlot_1_Channel_1.setText(QCoreApplication.translate("MainWindow", u"Channel_1", None))
        self.UpperPlot_1_Channel_2.setText(QCoreApplication.translate("MainWindow", u"Channel_2", None))
        self.UpperPlot_1_Channel_3.setText(QCoreApplication.translate("MainWindow", u"Channel_3", None))
        self.UpperPlot_1_Channel_4.setText(QCoreApplication.translate("MainWindow", u"Channel_4", None))
        self.UpperPlot_1_Channel_5.setText(QCoreApplication.translate("MainWindow", u"Channel_5", None))
        self.upperPlotTabWidget.setTabText(self.upperPlotTabWidget.indexOf(self.upperPlotTab_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.upper_new_plot_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bottomFigureAttributes_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Figure attributes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\""
                        "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bottomPlot_1_Channel_1.setText(QCoreApplication.translate("MainWindow", u"Channel_1", None))
        self.bottomPlot_1_Channel_2.setText(QCoreApplication.translate("MainWindow", u"Channel_2", None))
        self.bottomPlot_1_Channel_3.setText(QCoreApplication.translate("MainWindow", u"Channel_3", None))
        self.bottomPlot_1_Channel_4.setText(QCoreApplication.translate("MainWindow", u"Channel_4", None))
        self.bottomPlot_1_Channel_5.setText(QCoreApplication.translate("MainWindow", u"Channel_5", None))
        self.bottomPlotTabWidget.setTabText(self.bottomPlotTabWidget.indexOf(self.bottomPlotTab_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.bottomFigureAttributes_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Figure attributes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\""
                        "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bottomPlot_2_Channel_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.bottomPlot_2_Channel_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.bottomPlot_2_Channel_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.bottomPlot_2_Channel_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.bottomPlot_2_Channel_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.bottomPlotTabWidget.setTabText(self.bottomPlotTabWidget.indexOf(self.bottomPlotTab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.bottom_new_plot_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.modelArea.setTabText(self.modelArea.indexOf(self.model_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
    # retranslateUi

