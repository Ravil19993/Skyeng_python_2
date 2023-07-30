def months_to_season(n):
    if n in range (1, 3) or n == 12:
        print('Зима')

    if n in range (3, 6):
        print('Весна')

    if n in range (6, 9):
        print('Лето')

    if n in range (9, 12):
        print('Осень')

n = 11
months_to_season(n)