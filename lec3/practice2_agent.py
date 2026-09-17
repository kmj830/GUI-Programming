import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class Practice2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.img_path = Path(__file__).parent.parent / "assets" / "image.png"
        self.init_ui()

    def init_ui(self):
        """화면에 필요한 위젯을 생성하고 시그널을 연결합니다."""
        self.setWindowTitle("실습 2 - 사용자 정보 입력")
        self.setFixedSize(450, 350)

        self.label1 = QLabel("환영합니다!", self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.resize(250, 30)
        self.label1.move(100, 70)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("이름을 입력하세요")
        self.line_edit.resize(250, 30)
        self.line_edit.move(100, 130)

        self.btn_ok = QPushButton("확인", self)
        self.btn_ok.resize(120, 35)
        self.btn_ok.move(95, 190)
        self.btn_ok.clicked.connect(self.on_click_ok)

        self.btn_clear = QPushButton("지우기", self)
        self.btn_clear.resize(120, 35)
        self.btn_clear.move(235, 190)
        self.btn_clear.clicked.connect(self.on_click_clear)

        self.image_label = QLabel(self)
        self.image_label.resize(100, 100)
        self.image_label.move(100, 240)
        self.image_label.hide()

    def on_click_ok(self):
        name = self.line_edit.text()

        if not name:
            self.label1.setText("이름을 입력해주세요!")
            return

        self.label1.setText(f"{name}님 환영합니다!")

        if name == "image":
            pixmap = QPixmap(str(self.img_path))
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            self.image_label.show()

    def on_click_clear(self):
        self.line_edit.clear()
        self.label1.setText("환영합니다!")
        self.image_label.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Practice2Window()
    window.show()
    sys.exit(app.exec_())
