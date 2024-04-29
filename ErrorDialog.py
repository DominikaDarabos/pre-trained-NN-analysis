from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QPushButton
from PySide6.QtGui import QIcon
import os, sys
class ErrorDialog(QDialog):
    """
    Dialog for listing all the errors given as a parameter.
    """
    def __init__(self, error_message):
        super().__init__()
        self.setWindowTitle("Error")
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        logo_path = find_file(script_dir, 'logo.png')
        self.setWindowIcon(QIcon(logo_path))
        layout = QVBoxLayout()
        textArea = QTextBrowser()
        textArea.setFixedWidth(500)
        textArea.setFixedHeight(150)
        for message in error_message:
            textArea.append(message)
        layout.addWidget(textArea)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

def find_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None