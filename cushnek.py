from PyQt5.QtWidgets import*
app = QApplication([])
win = QWidget()


main = QHBoxLayout()
win.setLayout(main)
qtxt = QLabel('&&&&&&&&&&&&&&&&&&&&&&')
main.addWidget(qtxt)




exe1 = QHBoxLayout()
exe2 =QHBoxLayout()
main.addLayout(exe1)
main.addLayout(exe2)



left = QGroupBox()
right = QGroupBox()
setka = QGridLayout()
left.setLayout(setka)
r1 = QRadioButton('Пантера')
r2 = QRadioButton('ds')
r3 = QRadioButton('fds')
r4 = QRadioButton('gta6')
setka.addWidget(r1,1,1)
setka.addWidget(r2,1,3)
setka.addWidget(r3,2,1)
setka.addWidget(r4,2,3)
ansb = QPushButton('Отвечай')
setka.addWidget(ansb,3,2)

line3 = QVBoxLayout()
right.setLayout(line3)
restxt = QLabel('apple')
nextb = QPushButton('гуляй')
line3.addWidget(restxt)
line3.addWidget(nextb)

right.hide()

from random import*
qbase = [
['Главный злодей в doomsday', 'Путин', ' Альтрон', 'Doom', 'Железный человек'],
['Когда выйдет в россии мстители:Секретная война', 'никогда', ' завтра', 'зимой', 'через два года'],
['Главный герой в doomsday', 'тор', ' Трамп', 'Били Бутчер', 'железное сердце']

]

fq = choice(qbase)
qtxt.setText(fq[0])
r1.setText(fq[1])
r2.setText(fq[2])
r3.setText(fq[3])
r4.setText(fq[4])
restxt.setText(fq[1])
    



def toright():
    right.show()
    left.hide()
ansb.clicked.connect(toright)

def toleft():
    sp = [r1,r2,r3,r4]
    shuffle(sp)
    setka.addWidget(sp[0])
    setka.addWidget(sp[1],1,3)
    setka.addWidget(sp[2],2,1)
    setka.addWidget(sp[3],2,3)
    fq = choice(qbase)
    qtxt.setText(fq[0])
    r1.setText(fq[1])
    r2.setText(fq[2])
    r3.setText(fq[3])
    r4.setText(fq[4])
    restxt.setText(fq[1])
    
    
    right.hide()
    restxt.setText(fq[1])
    left.show()
nextb.clicked.connect(toleft)






exe1.addWidget(left)
exe2.addWidget(right)

















win.show()
app.exec_()