from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()
vb = QVBoxLayout()
okno.setLayout(vb)



vtx = QLabel('Кто здесь?')
vb.addWidget(vtx)
hb1 = QHBoxLayout()
hb2 = QHBoxLayout()
vb.addLayout(hb1)
vb.addLayout(hb2)
rb1 = QRadioButton('нет')
rb2 = QRadioButton('Россия , Путин ,Победа')
rb3 = QRadioButton('Жирный дед')
rb4 = QRadioButton('Linux')
hb1.addWidget(rb1)
hb1.addWidget(rb2)
hb2.addWidget(rb3)
hb2.addWidget(rb4)
line1 = QVBoxLayout()



b1 = QPushButton('Скачать майнер')
vb.addWidget(b1)
def poka():
    msg = ''
    if rb2.isChecked():
        msg = 'Красава марат'
    else:
        msg = 'гуляй вась'
    b1 = QMessageBox()
    b1.setText(msg)
    b1.exec()
    quit()

b1.clicked.connect(poka)




okno.show()
app.exec()
