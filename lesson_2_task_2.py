def is_year_leap(year):
    if year % 4 == 0:
        result = True
    else:
        result = False
    return result   

year = 2016

print('Год ', year, end = ': ')
print(is_year_leap(year))