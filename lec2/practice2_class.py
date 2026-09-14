import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton

def on_click():
    user_message=le1.text()
    lbl2.setText(user_message)
    window2.show()

def on_click2():
    le1.setText("")
    lbl2.setText("")
    window2.close()


app = QApplication(sys.argv)


window = QWidget()

window2=QWidget()
window2.setFixedSize(200,100)
window2.setStyleSheet('background-color: lightgreen')
lbl2 = QLabel(window2)


window.setWindowTitle("Window 1")
window.setStyleSheet('background-color: lightblue')
window.setFixedSize(450,350)


lbl = QLabel("9월 14일 월요일입니다.", window)
lbl.setStyleSheet("font-size: 10px; font-weight: bold; color: darkblue")
lbl.resize(300,100)
lbl.setAlignment(Qt.AlignCenter)

le1 = QLineEdit(window)
le1.setStyleSheet("color: lightblue; font-size: 10px; font-weight: bold; color: darkblue")
le1.resize(200,30)
le1.move(100,150)
le1.setPlaceholderText("이름을 적어주세요")

btn1 = QPushButton("입력", window)
btn1.setStyleSheet('background-color: lightgreen; font-size: 10px; font-weight:bold; color: darkgreen;')
btn1.resize(100, 50)
btn1.move(100, 200)

btn2 = QPushButton("지우기", window)
btn2.setStyleSheet('background-color: lightgreen; font-size: 10px; font-weight:bold; color: darkgreen;')
btn2.resize(100, 50)
btn2.move(250, 200)



btn1.clicked.connect(on_click)
btn2.clicked.connect(on_click2)
window.show()
sys.exit(app.exec_())