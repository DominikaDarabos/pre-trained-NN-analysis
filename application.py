#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore

from utils import main, new_model

class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        # open in full screen
        self.showMaximized()

        self.setWindowTitle("Analyzer application")
        self.populate_list_widget()
        self.effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.set_shadow_effect(enabled=True)

    # add elements to side menu bar
    def populate_list_widget(self):
        sideMenuElements = ["Integrated Gradients", "LRP-z"]
        self.listWidget.addItems(sideMenuElements)

    def set_shadow_effect(self, enabled=True):
        if enabled:
            self.effect.setEnabled(True)
            self.effect.setOpacity(0.3)
            self.setGraphicsEffect(self.effect)
        else:
            self.effect.setEnabled(False)


class NewModelDialog(QtWidgets.QDialog):
    def __init__(self,main,  parent=None):
        super().__init__(parent)
        self.ui = new_model.Ui_Dialog()
        self.ui.setupUi(self)
        self.activateWindow()
        self.main_window = main
        self.ui.createButton.clicked.connect(self.show_main_window)

    # Slot to show the main window
    def show_main_window(self):
        self.hide()  # Hide the dialog
        #self.main_window.showMaximized()  # Show the main window
        self.main_window.set_shadow_effect(enabled=False)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_dialog = NewModelDialog(qt_app)
    qt_dialog.show()
    #qt_app.show()
    app.exec_()