from PyQt5.QtWidgets import*


app = QApplication([])
okno = QWidget()
okno.setWindowTitle('не моя программа')

btn = QPushButton(okno)
btn.setText('пока')
btn.resize(100,100)
okno.resize(500,500)
btn.move(200,150)


sp = ['z', 'o','p', 'a', 'and ', 'banana', 'mineons']
from random import choice

tx = QLabel(okno)
tx.setText('мяу')
tx.resize(300,25)
tx.move(200,250)

def test():
    tx.resize(300,25)
    tx.setText('текст есть и я тут')
    tx.setText(choice(sp))




btn.clicked.connect(test)


































okno.show()
app.exec()
