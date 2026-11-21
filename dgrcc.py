class Widget():
    def __init__(self, text,x_num, y_num):
        self.text = text
        self.x_num = x_num
        self.y_num = y_num

    def print_info(self):
        print('Надпись:', self.text)
        print('Расположение:', self.x_num, self.y_num)

class Button(Widget):
    def __init__(self, text,x_num, y_num, is_clicked_boll):
        super().__init__(text,x_num, y_num)

        self.is_clicked_boll = is_clicked_boll

    def click(self):
        self.is_clicked = True
        print('Вы зарегистрированы')

button = Button('Участвовать', 100, 100, False)
button.print_info()
