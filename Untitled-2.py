correct_choice=False
while not correct_choice:
    choice=input('Введите число 1 или 2:')
    if choice =='1' or choice =='2':
        correct_choice=True
    else:
           print('Неправильно введено число,повторите введение')