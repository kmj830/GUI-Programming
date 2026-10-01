import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox,
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 260)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
