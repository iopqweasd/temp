from PyQt5.QtWidgets import*
from random import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

app = QApplication([])
okno = QWidget()
okno.setFixedSize(250, 350)
okno.setWindowTitle('Standoff2')
okno.setWindowIcon(QIcon('stand.webp'))
mv = QVBoxLayout()
okno.setLayout(mv)
upper = QGroupBox()
downb = QGroupBox()
mv.addWidget(upper)
mv.addWidget(downb)
dsd = QHBoxLayout()
upper.setLayout(dsd)
icd1 = QLCDNumber(3)
icd2 = QLCDNumber(3)
smile = QPushButton()
dsd.addWidget(icd1)
dsd.addWidget(smile)
dsd.addWidget(icd2)
upper.setFixedHeight(60)
smile.setFixedSize(40,40)

smile.setIcon(QIcon('ver.jpg'))
smile.setIconSize(QSize(40,40))

pal = icd1.palette()
pal.setColor(QPalette.WindowText, Qt.red)
icd1.setStyleSheet('background: black')
icd2.setStyleSheet('background: black')
pal.setColor(QPalette.Dark, QColor(200,0,0));
icd1.setPalette(pal)
icd2.setPalette(pal)



gr = QGridLayout()
downb.setLayout(gr)

cells = []


for y in range(9):
    for x in range(9):
        b1 = QPushButton()
        b.setFixedSize(26,28)
        cells.append(b1)
        gr.addWidget(b1,x,y)
bombs = []
icd1.display(10)
for i in range(10)
    bmb = choice(cells)
    bombs.append(bmb)
    sells.remove(bmb)


for b1 in range(len(bombs)):
    bombs[b1].clicked.connect(lambda: bombs[b1].setStyleSheet('background: red'))












okno.show()
app.exec_()