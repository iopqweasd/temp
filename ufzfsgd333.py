from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()
okno.setWindowTitle("Это моё окно!")
okno.resize(500,500)

btn =  QPushButton(okno)
btn.setText('okak')
btn.resize(100,100)
okno.resize(500,500)
btn.move(200,150)

tx = QLabel(okno)
tx.setText('отказано')
tx.resize(300,25)
tx.move(200,250)

def cht():
    tx.resize(300,25)
    tx.setText('текст есть и я тут')

btn.clicked.connect(cht)

btn2 = QPushButton(okno)
btn2.setText('okak')
btn2.resize(100,100)
btn2.move(200,150)

from random import randint

btn2.clicked.connect(lambda: btn2.move(randint(0,400), randint(0,450)))


okno.show()
app.exec()