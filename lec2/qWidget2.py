import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 GUI")
window.resize(400, 320)
window.setStyleSheet("background-color:lightblue")

lbl = QLabel("문구 입력", window)
lbl.move(160,90)

le = QLineEdit(window)
le.setPlaceholderText("문구를 입력하세요")



btn= QPushButton("확인", window)
btn.resize(100, 40)
btn.move(150, 140)

btn.clicked()

window.show()
sys.exit(app.exec_())
