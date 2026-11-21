from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

app = QApplication([])
okno = QWidget()

line1 = QVBoxLayout()

okno.setLayout(line1)
hb1 = QHBoxLayout()
hb2 = QHBoxLayout()
hb3 = QHBoxLayout()
line1.addLayout(hb1)
line1.addLayout(hb2)
line1.addLayout(hb3)

for i in range(6):
    globals()['b'+str(i+1)]= QPushButton(str(i+1))

hb1.addWidget(b1,stretch = 1)
hb1.addWidget(b2, stretch= 10)
hb2.addWidget(b3, alignment = Qt.AlignLeft)
hb2.addWidget(b4, alignment = Qt.AlignRight)
hb3.addWidget(b5, alignment = Qt.AlignCenter)
hb3.addWidget(b5, alignment = Qt.AlignCenter)
hb3.addWidget(b6, alignment = Qt.AlignCenter)









okno.show()
app.exec()
