f = open('мой файл.txt', 'a')
f.write('''
Меняем содержимое
''')
data4 = f.readlines()
print(data4)
