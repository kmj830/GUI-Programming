import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

#from pathlib import Path
#img_path = Path(__file__).parent.parent / "assets" / "image.png"
#print(img_path)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)

label1 = QLabel("환영합니다!", window)
label1.setAlignment(Qt.AlignCenter)
label1.resize(250, 30)
label1.move(100, 70)

line_edit = QLineEdit(window)
line_edit.setPlaceholderText("이름을 입력하세요")
line_edit.resize(250, 30)
line_edit.move(100, 130)

def on_click_ok():
    name = line_edit.text()
    if name:
        label1.setText(f"{name}님 환영합니다!")
        if name == "image":
            pixmap = QPixmap("/Users/blue/Library/CloudStorage/GoogleDrive-bishalrswain@gmail.com/My Drive/South Korea/KIT/Lecture/2026-2 GUI_programming/workspace/assets/image.png")  # 이미지 파일 경로를 지정
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)  # 이미지 크기를 QLabel에 맞게 조정
            image_label.show()  # 이미지 라벨을 표시

    else:
        label1.setText("이름을 입력해주세요!")

def on_click_clear():
    line_edit.clear()
    label1.setText("환영합니다!")
    image_label.hide()  # 이미지 라벨을 숨김

btn_ok = QPushButton("확인", window)
btn_ok.resize(120, 35)
btn_ok.move(95, 190)
btn_ok.clicked.connect(on_click_ok)

btn_clear = QPushButton("지우기", window)
btn_clear.resize(120, 35)
btn_clear.move(235, 190)
btn_clear.clicked.connect(on_click_clear)

image_label = QLabel(window)
image_label.resize(100, 100)
image_label.move(100, 240)
image_label.hide()  # 초기에는 이미지 라벨을 숨김


window.show()
sys.exit(app.exec_())