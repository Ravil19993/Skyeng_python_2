import math
def square(side):
    result = side * side
    if type(result) == float:
        print('Square = ', math.ceil(result))
    else:
        print('Square = ', result)


square(10.0)