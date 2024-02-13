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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(759, 435)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.baseFrame = QFrame(Dialog)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setFrameShape(QFrame.StyledPanel)
        self.baseFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.baseFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SelectAnalyzersLabel = QLabel(self.baseFrame)
        self.SelectAnalyzersLabel.setObjectName(u"SelectAnalyzersLabel")
        self.SelectAnalyzersLabel.setMaximumSize(QSize(16777215, 30))
        self.SelectAnalyzersLabel.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.SelectAnalyzersLabel, 1, 0, 1, 1)

        self.modelSelectorLayout = QHBoxLayout()
        self.modelSelectorLayout.setObjectName(u"modelSelectorLayout")
        self.selectModelLine = QLineEdit(self.baseFrame)
        self.selectModelLine.setObjectName(u"selectModelLine")

        self.modelSelectorLayout.addWidget(self.selectModelLine)

        self.selectModelButton = QToolButton(self.baseFrame)
        self.selectModelButton.setObjectName(u"selectModelButton")

        self.modelSelectorLayout.addWidget(self.selectModelButton)


        self.gridLayout.addLayout(self.modelSelectorLayout, 0, 0, 1, 1)

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
        self.verticalLayout = QVBoxLayout(self.analyzerCheckboxFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_IG = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_IG.setObjectName(u"checkBox_IG")

        self.verticalLayout.addWidget(self.checkBox_IG)

        self.checkBox_LRP_Z = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_Z.setObjectName(u"checkBox_LRP_Z")

        self.verticalLayout.addWidget(self.checkBox_LRP_Z)

        self.checkBox_LRP_AB = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_AB.setObjectName(u"checkBox_LRP_AB")

        self.verticalLayout.addWidget(self.checkBox_LRP_AB)

        self.checkBox_LRP_Epsilon = QCheckBox(self.analyzerCheckboxFrame)
        self.checkBox_LRP_Epsilon.setObjectName(u"checkBox_LRP_Epsilon")

        self.verticalLayout.addWidget(self.checkBox_LRP_Epsilon)


        self.horizontalLayout_2.addWidget(self.analyzerCheckboxFrame)

        self.neuronSelectionFrame = QFrame(self.analyzersFrame)
        self.neuronSelectionFrame.setObjectName(u"neuronSelectionFrame")
        self.neuronSelectionFrame.setFrameShape(QFrame.StyledPanel)
        self.neuronSelectionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.neuronSelectionFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_IG = QComboBox(self.neuronSelectionFrame)
        self.comboBox_IG.addItem("")
        self.comboBox_IG.addItem("")
        self.comboBox_IG.addItem("")
        self.comboBox_IG.setObjectName(u"comboBox_IG")

        self.verticalLayout_2.addWidget(self.comboBox_IG)

        self.comboBox_LRP_Z = QComboBox(self.neuronSelectionFrame)
        self.comboBox_LRP_Z.addItem("")
        self.comboBox_LRP_Z.addItem("")
        self.comboBox_LRP_Z.addItem("")
        self.comboBox_LRP_Z.setObjectName(u"comboBox_LRP_Z")

        self.verticalLayout_2.addWidget(self.comboBox_LRP_Z)

        self.comboBox_LRP_AB = QComboBox(self.neuronSelectionFrame)
        self.comboBox_LRP_AB.addItem("")
        self.comboBox_LRP_AB.addItem("")
        self.comboBox_LRP_AB.addItem("")
        self.comboBox_LRP_AB.setObjectName(u"comboBox_LRP_AB")

        self.verticalLayout_2.addWidget(self.comboBox_LRP_AB)

        self.comboBox_LRP_Epsilon = QComboBox(self.neuronSelectionFrame)
        self.comboBox_LRP_Epsilon.addItem("")
        self.comboBox_LRP_Epsilon.addItem("")
        self.comboBox_LRP_Epsilon.addItem("")
        self.comboBox_LRP_Epsilon.setObjectName(u"comboBox_LRP_Epsilon")

        self.verticalLayout_2.addWidget(self.comboBox_LRP_Epsilon)


        self.horizontalLayout_2.addWidget(self.neuronSelectionFrame)

        self.paramsFrame = QFrame(self.analyzersFrame)
        self.paramsFrame.setObjectName(u"paramsFrame")
        self.paramsFrame.setMaximumSize(QSize(150, 16777215))
        self.paramsFrame.setFrameShape(QFrame.StyledPanel)
        self.paramsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.paramsFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.IG_Z_spacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.IG_Z_spacer)

        self.EpsilonInput = QLineEdit(self.paramsFrame)
        self.EpsilonInput.setObjectName(u"EpsilonInput")

        self.verticalLayout_3.addWidget(self.EpsilonInput)

        self.AlphaBetaComboBox = QComboBox(self.paramsFrame)
        self.AlphaBetaComboBox.addItem("")
        self.AlphaBetaComboBox.addItem("")
        self.AlphaBetaComboBox.setObjectName(u"AlphaBetaComboBox")

        self.verticalLayout_3.addWidget(self.AlphaBetaComboBox)


        self.horizontalLayout_2.addWidget(self.paramsFrame)


        self.gridLayout.addWidget(self.analyzersFrame, 2, 0, 1, 1)

        self.createButton = QPushButton(self.baseFrame)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.createButton, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.baseFrame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SelectAnalyzersLabel.setText(QCoreApplication.translate("Dialog", u"Select analyzers", None))
        self.selectModelLine.setText(QCoreApplication.translate("Dialog", u"Select model", None))
        self.selectModelButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.checkBox_IG.setText(QCoreApplication.translate("Dialog", u"Integrated Gradients", None))
        self.checkBox_LRP_Z.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - Z", None))
        self.checkBox_LRP_AB.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - ALPHA - BETA", None))
        self.checkBox_LRP_Epsilon.setText(QCoreApplication.translate("Dialog", u"Layer-wise relevance propagation - EPSILON", None))
        self.comboBox_IG.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_IG.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))
        self.comboBox_IG.setItemText(2, QCoreApplication.translate("Dialog", u"Index", None))

        self.comboBox_LRP_Z.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_Z.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))
        self.comboBox_LRP_Z.setItemText(2, QCoreApplication.translate("Dialog", u"Index", None))

        self.comboBox_LRP_AB.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_AB.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))
        self.comboBox_LRP_AB.setItemText(2, QCoreApplication.translate("Dialog", u"Index", None))

        self.comboBox_LRP_Epsilon.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_LRP_Epsilon.setItemText(1, QCoreApplication.translate("Dialog", u"Max activation", None))
        self.comboBox_LRP_Epsilon.setItemText(2, QCoreApplication.translate("Dialog", u"Index", None))

        self.EpsilonInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"epsilon", None))
        self.AlphaBetaComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Alpha_2, Beta_1", None))
        self.AlphaBetaComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Alpha_1, Beta_0", None))

        self.createButton.setText(QCoreApplication.translate("Dialog", u"Create Project", None))
    # retranslateUi

