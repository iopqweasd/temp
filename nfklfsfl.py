from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
QLabel, QMessageBox, QRadioButton)

def show_win():

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400,200)

question = QLabel('В каком году канал получил золотою кнопку от  от YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

layout_main = QVBoxLayout()
LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()

LayoutH1.addWidget(question)
LayoutH2.addWidget(btn_answer1)
LayoutH2.addWidget(btn_answer2) 
LayoutH3.addWidget(btn_answer3)
LayoutH3.addWidget (btn_answer4)

layout_main.addLayout(LayoutH1)
layout_main.addLayout(LayoutH2)
layout_main.addLayout(LayoutH3)

main_win.setLayout(layout_main)

main_win.show()
app.exec_()





