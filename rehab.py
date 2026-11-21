from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()
vb = QVBoxLayout()
okno.setLayout(vb)



vtx = QLabel('Главный злодей в doomsday','Когда выйдет в россии мстители:Секретная война')
vb.addWidget(vtx)
from random import choice
hb1 = QHBoxLayout()
hb2 = QHBoxLayout()
vb.addLayout(hb1)
vb.addLayout(hb2)
rb1 = QRadioButton('Путин')
rb2 = QRadioButton('Альтрон')
rb3 = QRadioButton('Doom')
rb4 = QRadioButton('Железный человек')
hb1.addWidget(rb1)
hb1.addWidget(rb2)
hb2.addWidget(rb3)
hb2.addWidget(rb4)
line1 = QVBoxLayout()



b1 = QPushButton('Скачать майнер')
vb.addWidget(b1)
def poka():
    msg = ''
    if rb3.isChecked():
        msg = 'Красава марат'
        b1 = QMessageBox()
        b1.setText(msg)
        b1.exec()
        b1.setText(choice(vtx))
    else:
        msg = 'гуляй вась'
        b1 = QMessageBox()
        b1.setText(msg)
        b1.exec()
        app.quit()

b1.clicked.connect(poka)




okno.show()
app.exec()
