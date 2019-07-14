def myfunc2(number):
    if number == 34:
        raise ArithmeticError('Number is thirty four')
    print(number)

def myfunc(number):
    try:
        myfunc2(number)
    except Exception:
        print("error")

myfunc(22)
myfunc(34)

