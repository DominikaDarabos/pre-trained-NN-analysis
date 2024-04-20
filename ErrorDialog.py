from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QPushButton
class ErrorDialog(QDialog):
    """
    Dialog for listing all the errors given as a parameter.
    """
    def __init__(self, error_message):
        super().__init__()
        self.setWindowTitle("Error")
        layout = QVBoxLayout()
        textArea = QTextBrowser()
        textArea.setFixedWidth(500)
        for message in error_message:
            textArea.append(message)
        layout.addWidget(textArea)
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)
        self.setLayout(layout)