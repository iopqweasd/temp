from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()
main = QVBoxLayout()
okno.setLayout(main)

btn1 = QPushButton('ОТкрыть')
btn2 = QPushButton('Сохранить')
txin = QTextEdit()
main.addWidget(btn1)
main.addWidget(btn2)
main.addWidget(txin)

#f = open('worl.txt', 'w')

def sav():
    f = open('worl.txt', 'w')
    f.write(txin.toPlainText())
btn2.clicked.connect(sav)
def opn():
    f = open('worl.txt', 'r')
    txin.setText(f.read())
btn1.clicked.connect(opn)











okno.show()
app.exec_()