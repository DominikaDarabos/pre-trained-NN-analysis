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
        self.gridLayout_10 = QGridLayout(self.plotPanelFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.upperPlotTabWidget = QTabWidget(self.plotPanelFrame)
        self.upperPlotTabWidget.setObjectName(u"upperPlotTabWidget")
        

        self.gridLayout_10.addWidget(self.upperPlotTabWidget, 0, 0, 1, 1)

        self.upper_new_plot_button = QPushButton(self.plotPanelFrame)
        self.upper_new_plot_button.setObjectName(u"upper_new_plot_button")

        self.gridLayout_10.addWidget(self.upper_new_plot_button, 1, 0, 1, 1, Qt.AlignRight)

        self.bottomPlotTabWidget = QTabWidget(self.plotPanelFrame)
        self.bottomPlotTabWidget.setObjectName(u"bottomPlotTabWidget")


        self.gridLayout_10.addWidget(self.bottomPlotTabWidget, 2, 0, 1, 1)

        self.bottom_new_plot_button = QPushButton(self.plotPanelFrame)
        self.bottom_new_plot_button.setObjectName(u"bottom_new_plot_button")

        self.gridLayout_10.addWidget(self.bottom_new_plot_button, 3, 0, 1, 1, Qt.AlignRight)


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
        self.outputDataTitle.setText(QCoreApplication.translate("MainWindow", u"Output Data", None))
        self.validationTitle.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.modelDataTitle.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.dynamicTitle.setText(QCoreApplication.translate("MainWindow", u"Model graph", None))
        self.upper_new_plot_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bottom_new_plot_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.modelArea.setTabText(self.modelArea.indexOf(self.model_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
    # retranslateUi

