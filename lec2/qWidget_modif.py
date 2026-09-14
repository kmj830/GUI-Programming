import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5 Window")
window.resize(400, 320)
window.setStyleSheet("background-color: red;")

window.show()
sys.exit(app.exec_())