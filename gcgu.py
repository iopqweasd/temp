from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from random import choice

app = QApplication([])
win = QWidget()
line1 = QVBoxLayout()
win.setLayout(line1)
upb = QGroupBox()
dnb = QGroupBox()
line1.addWidget(upb)
line1.addWidget(dnb)
win.setFixedSize(250,310)
upb.setFixedHeight(60)

leftN = QLCDNumber()
rightN = QLCDNumber()
resb = QPushButton()
line2 = QHBoxLayout()
upb.setLayout(line2)
line2.addWidget(leftN)
line2.addWidget(resb)
line2.addWidget(rightN)
leftN.display(10)

leftN.setStyleSheet('background: black;')
rightN.setStyleSheet('background: black;')
pal = leftN.palette()
pal.setColor(QPalette.WindowText, QColor(255,0,0))
pal.setColor(QPalette.Light, Qt.red)
pal.setColor(QPalette.Dark, Qt.darkRed)
leftN.setPalette(pal)
rightN.setPalette(pal)
resb.setFixedSize(QSize(42,42))
resb.setIcon(QIcon('pngtree-smile-vector-template-design-illustration-png-image_555090.jpg'))
resb.setIconSize(QSize(36,36))

cells = []
bombs = []
gr = QGridLayout()
dnb.setLayout(gr)

for y in range(9):
    for x in range(9):
        b1 = QPushButton()
        b1.setFixedSize(26,26)
        gr.addWidget(b1,x,y)
        cells.append(b1)

for i in range(10):
    newb = choice(cells)
    bombs.append(newb)
    cells.remove(newb)
    #newb.setStyleSheet('background: green;')

    def test (bm):
        bm.setStyleSheet('background: red;')

for bm in bombs:
    bm.clicked.connect(lambda checked=False, bm=bm : test(bm))

win.show()
app.exec_()