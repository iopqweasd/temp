from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.setFixedSize(300, 400)

layout = QVBoxLayout()

display = QLineEdit()
display.setReadOnly(True)
display.setStyleSheet("font-size: 20px; padding: 5px;")
layout.addWidget(display)

grid = QGridLayout()


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]
def press():
    button = window.sender()
    text = button.text()
    current = display.text()
    
    if text == 'C':
        display.clear()
    elif text == '=':
        try:
            res = str(eval(current))
            display.setText(res[:-2] if res.endswith('.0') else res)
        except:
            display.setText("Ошибка")
    else:
        if text in '+-*/' and current and current[-1] in '+-*/':
            display.setText(current[:-1] + text)
        else:
            display.setText(current + text)

row, col = 0, 0
for text in buttons:
    btn = QPushButton(text)
    btn.setStyleSheet("font-size: 18px; min-height: 45px;")
    btn.clicked.connect(press)

    btn.setStyleSheet("""
        QPushButton {
            font-size: 18px; 
            font-weight: bold;
            min-height: 45px;
            background-color: #ef4444; /* Красный цвет */
            color: white;              /* Белый текст */
            border-radius: 5px;        /* Закругленные углы */
        }
        QPushButton:pressed {
            background-color: red; /* Темно-красный цвет при клике */
        }
    """)
    
    if text == '=':
        grid.addWidget(btn, row, col, 1, 5) 
    else:
        grid.addWidget(btn, row, col)
        
    col += 1
    if col > 3:
        col = 0
        row += 1

layout.addLayout(grid)
window.setLayout(layout)

window.show()
app.exec()