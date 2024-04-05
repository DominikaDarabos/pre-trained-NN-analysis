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
    # setupUi

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
    # retranslateUi

