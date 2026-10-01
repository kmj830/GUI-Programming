import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QVBoxLayout")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create vertical box layout
        layout = QHBoxLayout()
        inlayout = QVBoxLayout()

        for text, color in [
            ("horizontal 1", "red"),
        ]:
            label = QLabel(text, self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(
                f"background-color: {color}; color: black; font-size: 24px;"
            )
            layout.addWidget(label)


        for text, color in [
            ("vertical 1", "blue"),
            ("vertical 2", "green"),
            ("vertical 3", "yellow"),
            ("vertical 4", "orange")
        ]:
            label = QLabel(text, self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(
                f"background-color: {color}; color: black; font-size: 24px;"
            )
            inlayout.addWidget(label)

        layout.addLayout(inlayout)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
