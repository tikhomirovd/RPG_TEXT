def check_int(text):
    num = input(text)
    if num.isdigit():
        return int(num)
    else:
        print("Ошибка. Введено не целое число. Введите ещё раз")
        return check_int(text)

def check_float(text):
    num = input(text)
    try:
        num = float(num)
        return num
    except ValueError:
        print("Ошибка. Введено не число. Введите ещё раз")
        return check_float(text)