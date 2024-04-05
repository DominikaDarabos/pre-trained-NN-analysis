# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_model_ui.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(759, 486)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.baseFrame = QFrame(Dialog)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.baseFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout_2.addWidget(self.baseFrame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def add_analyzer_frame(self):
        self.analyzersFrame = QFrame(self.baseFrame)
        self.analyzersFrame.setObjectName(u"analyzersFrame")
        self.analyzersFrame.setMinimumSize(QSize(0, 300))
        self.analyzersFrame.setFrameShape(QFrame.StyledPanel)
        self.analyzersFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.analyzersFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analyzerCheckboxFrame = QFrame(self.analyzersFrame)
        self.analyzerCheckboxFrame.setObjectName(u"analyzerCheckboxFrame")
        self.analyzerCheckboxFrame.setFrameShape(QFrame.StyledPanel)
        self.analyzerCheckboxFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.analyzerCheckboxFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_IG = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_IG.setObjectName(u"checkBox_IG")
        self.checkBox_IG.setMinimumSize(QSize(350, 0))
        self.checkBox_IG.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout.addWidget(self.checkBox_IG)

        self.comboBox_IG = QComboBox(self.analyzerCheckboxFrame)
        self.comboBox_IG.addItem("")
        self.comboBox_IG.addItem("")
        self.comboBox_IG.setObjectName(u"comboBox_IG")
        self.comboBox_IG.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.comboBox_IG)

        self.referenceLine = QLineEdit(self.analyzerCheckboxFrame)
        self.referenceLine.setObjectName(u"referenceLine")
        self.referenceLine.setToolTip("Baseline for abscence values")
        self.referenceLine.setMaximumWidth(100)

        self.horizontalLayout.addWidget(self.referenceLine)

        self.stepLine = QLineEdit(self.analyzerCheckboxFrame)
        self.stepLine.setObjectName(u"stepLine")
        self.stepLine.setToolTip(" Number of steps to use average along integration path.")
        self.stepLine.setMaximumWidth(100)

        self.horizontalLayout.addWidget(self.stepLine)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_LRP_Z = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_Z.setObjectName(u"checkBox_LRP_Z")
        self.checkBox_LRP_Z.setMinimumSize(QSize(350, 0))
        self.checkBox_LRP_Z.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_3.addWidget(self.checkBox_LRP_Z)

        self.comboBox_LRP_Z = QComboBox(self.analyzerCheckboxFrame)
        self.comboBox_LRP_Z.addItem("")
        self.comboBox_LRP_Z.addItem("")
        self.comboBox_LRP_Z.setObjectName(u"comboBox_LRP_Z")
        self.comboBox_LRP_Z.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_LRP_Z)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_LRP_AB = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_AB.setObjectName(u"checkBox_LRP_AB")
        self.checkBox_LRP_AB.setMinimumSize(QSize(350, 0))
        self.checkBox_LRP_AB.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.checkBox_LRP_AB, 0, 0, 1, 1)

        self.comboBox_LRP_AB = QComboBox(self.analyzerCheckboxFrame)
        self.comboBox_LRP_AB.addItem("")
        self.comboBox_LRP_AB.addItem("")
        self.comboBox_LRP_AB.setObjectName(u"comboBox_LRP_AB")
        self.comboBox_LRP_AB.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.comboBox_LRP_AB, 0, 1, 1, 1)

        self.AlphaBetaComboBox = QComboBox(self.analyzerCheckboxFrame)
        self.AlphaBetaComboBox.addItem("")
        self.AlphaBetaComboBox.addItem("")
        self.AlphaBetaComboBox.setObjectName(u"AlphaBetaComboBox")
        self.AlphaBetaComboBox.setMinimumSize(QSize(150, 0))
        self.AlphaBetaComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.AlphaBetaComboBox, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_LRP_Epsilon = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_Epsilon.setObjectName(u"checkBox_LRP_Epsilon")
        self.checkBox_LRP_Epsilon.setMinimumSize(QSize(350, 0))
        self.checkBox_LRP_Epsilon.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.checkBox_LRP_Epsilon, 0, 0, 1, 1)

        self.comboBox_LRP_Epsilon = QComboBox(self.analyzerCheckboxFrame)
        self.comboBox_LRP_Epsilon.addItem("")
        self.comboBox_LRP_Epsilon.addItem("")
        self.comboBox_LRP_Epsilon.setObjectName(u"comboBox_LRP_Epsilon")
        self.comboBox_LRP_Epsilon.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.comboBox_LRP_Epsilon, 0, 1, 1, 1)

        self.EpsilonInput = QLineEdit(self.analyzerCheckboxFrame)
        self.EpsilonInput.setObjectName(u"EpsilonInput")
        self.EpsilonInput.setMinimumSize(QSize(150, 0))
        self.EpsilonInput.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.EpsilonInput, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.analyzerCheckboxFrame)


        self.verticalLayout_4.addWidget(self.analyzersFrame)

        self.checkBox_IG.setText(QCoreApplication.translate("Dialog", u"Integrated Gradients", None))
        self.comboBox_IG.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_IG.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))

        self.referenceLine.setText("")
        self.referenceLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Reference input", None))
        self.stepLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Steps", None))
        self.checkBox_LRP_Z.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - Z", None))
        self.comboBox_LRP_Z.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_Z.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))

        self.checkBox_LRP_AB.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - ALPHA - BETA", None))
        self.comboBox_LRP_AB.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_AB.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))

        self.AlphaBetaComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Alpha_2, Beta_1", None))
        self.AlphaBetaComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Alpha_1, Beta_0", None))

        self.checkBox_LRP_Epsilon.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - EPSILON", None))
        self.comboBox_LRP_Epsilon.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_Epsilon.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))

        self.EpsilonInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"epsilon", None))
    
    def add_input_frame(self):
        self.modelSelectorLayout = QHBoxLayout()
        self.modelSelectorLayout.setObjectName(u"modelSelectorLayout")
        self.selectModelLine = QLineEdit(self.baseFrame)
        self.selectModelLine.setObjectName(u"selectModelLine")
        self.modelSelectorLayout.addWidget(self.selectModelLine)
        self.selectModelButton = QToolButton(self.baseFrame)
        self.selectModelButton.setObjectName(u"selectModelButton")
        self.modelSelectorLayout.addWidget(self.selectModelButton)
        self.verticalLayout_4.addLayout(self.modelSelectorLayout)

        self.modelSelectorLayout_2 = QHBoxLayout()
        self.modelSelectorLayout_2.setObjectName(u"modelSelectorLayout_2")
        self.selectCustomLine = QLineEdit(self.baseFrame)
        self.selectCustomLine.setObjectName(u"selectCustomLine")
        self.modelSelectorLayout_2.addWidget(self.selectCustomLine)
        self.selectCustomButton = QToolButton(self.baseFrame)
        self.selectCustomButton.setObjectName(u"selectCustomButton")
        self.modelSelectorLayout_2.addWidget(self.selectCustomButton)
        self.verticalLayout_4.addLayout(self.modelSelectorLayout_2)

        self.modelSelectorLayout_3 = QHBoxLayout()
        self.modelSelectorLayout_3.setObjectName(u"modelSelectorLayout_3")
        self.selectInputLine = QLineEdit(self.baseFrame)
        self.selectInputLine.setObjectName(u"selectInputLine")
        self.modelSelectorLayout_3.addWidget(self.selectInputLine)
        self.selectInputButton = QToolButton(self.baseFrame)
        self.selectInputButton.setObjectName(u"selectInputButton")
        self.modelSelectorLayout_3.addWidget(self.selectInputButton)
        self.verticalLayout_4.addLayout(self.modelSelectorLayout_3)

        self.selectModelLine.setText(QCoreApplication.translate("Dialog", u"Select model", None))
        self.selectModelButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.selectCustomLine.setText(QCoreApplication.translate("Dialog", u"Select custom object python file", None))
        self.selectCustomButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.selectInputLine.setText(QCoreApplication.translate("Dialog", u"Select input file", None))
        self.selectInputButton.setText(QCoreApplication.translate("Dialog", u"...", None))

    def add_create_button(self):
        self.createButton = QPushButton(self.baseFrame)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.createButton)

        self.createButton.setText(QCoreApplication.translate("Dialog", u"Create Project", None))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        
    # retranslateUi

