## |---------------------------------------|
## | :by Kolambus    <(* ^ ω ^)>           | 
## |                                       |    
## | :The simplest calculator in Python    |
## |                                       |
## | :Version 1.0.0                        |
## |                                       |
## | :Total lines 55                       |
## |---------------------------------------| 

## start
def calculator(x, y):
    # проверка на деление на ноль отдельно от всех операций
    if (operation in ['/', '//', '%']) and (y == 0 or x == 0):
        print("Ошибка! Деление на ноль невозможно.")
        return None
    
    # выполнение нужной операции
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '/':  
        result = x / y
    elif operation == '*':
        result = x * y
    elif operation == '//':
        result = x // y
    elif operation == '%':
        result = x % y
    elif operation == '**':
        result = x ** y
    else:
        print("[Ошибка] Неправильная операция!")
        return None
        
    # вывод итогового результата
    print(f"Результат: {x} {operation} {y} => ", result)
    return result


# считывание чисел и операции
try:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
except ValueError:
    print("Ошибка ввода. Пожалуйста введите действительные числа.")
    exit()

print('Доступные операции: *, +, -, /, //, %, **')
operation = input('Введите нужную операцию: ')

# вызов функции калькулятора
result = calculator(num_1, num_2)
## finish
