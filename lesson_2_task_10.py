def bank(x, y):
    sum = x
    for i in range(1, y + 1):
        sum = sum + sum * 0.1
        print('На конец', i, '-го года сумма: ', end = '')
        print(sum, 'руб')
    return sum

x = 100000
y = 10

sum_up = round(bank(x,y))
print('Общая сумма на конец', y, '-го года: ', end = '')
print(sum_up, 'руб')