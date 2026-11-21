from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

app = QApplication([])
okno = QWidget()
m1 = QVBoxLayout()
okno.setLayout(m1)
m2 = QHBoxLayout()
m1.addLayout(m2)

knopka1 = QPushButton('лох')
m2.addWidget(knopka1)
knopka1.setStyleSheet('color: red;')

def fcol():
    knopka1.setStyleSheet('color:yellow;background-color:green;')
knopka1.clicked.connect(fcol)

knopka2 = QPushButton('нищий')
m2.addWidget(knopka2)
knopka1.setStyleSheet('background-color: yellow;')

knopka3 = QPushButton('дурак')
m2.addWidget(knopka3)
knopka1.setStyleSheet('font-size: 50px;')

m3 = QHBoxLayout()
m1.addLayout(m3)
tx1 = QLineEdit()
tx2 = QTextEdit()
m3.addWidget(tx1)
m3.addWidget(tx2)

lw = QListWidget()
m3.addWidget(lw)
def asd():
    lw.addItem(tx1.text())
knopka2.clicked.connect(asd)

sl = QSlider(orientation = Qt.Horizontal)
m3.addWidget(sl)

knopka4 = QPushButton('окак')
m2.addWidget(knopka4)

def chtx():
    text, ok = QInputDialog().getText(okno, "Ась?", "Что?")
    if ok:
        knopka3.setText(text)

knopka3.clicked.connect(chtx)

def chcol():
    col = QColorDialog().getColor()
    new = "background-color:" + col.name()
    okno.setStyleSheet(new)
knopka4.clicked.connect(chcol)

okno.show()
app.exec()