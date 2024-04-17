from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPuchButton, QLabel, QVBoxLayout
app = QApplication([])
my_win = QWidget(500,500)
my_win.setWindowTitle('Моё первое приложение')
v_line = QVBoxLayout()
h_line = QHBoxLayout()
winner = QLabel('Победитель')
v_line.addWidget(title, aligment = Qt.AligCenter)
ny_win.setLayout(v_line)
my_win.show()
app.exec_()