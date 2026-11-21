from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()

line1 = QVBoxLayout()
okno.setLayout(line1)
btn1 = QPushButton('1')
lineddWidget(btn1)
btn2 = QPushButton('2')
line1.addWidget(btn2)
btn3 = QPushButton('3')
line1.addWidget(btn3)

line2 = QHBoxLayout()
line1.addLayout(line2)
for i in range(5):
    b = QPushButton(str(i+1))
    line2.addWidget(b)
    b.clicked.connect(lambda: line2.addWidget(QPushButton("okak")))line2 = QHBoxLayout()

line1 = QVBoxLayout()
okno.setLayout(line1)
btn1 = QPushButton('Это кнопка')
line1.addWidget(btn1)
btn2 = QPushButton('Ещё кнопка')












okno.show()
app.exec()