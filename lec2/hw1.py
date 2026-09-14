import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("실습1")

window.resize(500,400)
window.setStyleSheet("background-color:lightgreen")

lbl= QLabel("안녕하세요, PyQt5", window).move(200,100)
btn= QPushButton("클릭", window).resize(120,40)


window.show()
sys.exit(app.exec_())