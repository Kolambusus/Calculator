## |---------------------------------------|
## | :by Kolambus    <(* ^ ω ^)>           | 
## |                                       |    
## | :The simplest calculator in Python    |
## |                                       |
## | :Total 61 lines                       |
## |---------------------------------------| 


## start
def calculator():

    operation = ['+', '-', '/', '*', '//', '%', '**']
    print('Привет, я калькулятор!')
    print('')
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    print('')
    print('Выберите операцию - ', operation)
    operat = input()

    if operat == '+':
        result = number_1 + number_2
        print('Итог => ', result)
    elif operat == '-':
        result = number_1 - number_2
        print('Итог => ', result)
    elif operat == '/':
        if number_1 != 0 and number_2 != 0:
            result = number_1 / number_2
            print('Итог => ', result)
        else:
            print('На ноль делить нельзя!')
            print('Попробуйте еще раз :)')
            return calculator()
    elif operat == '*':
        result = number_1 * number_2
        print('Итог => ', result)
    elif operat == '//':
        if number_1 != 0 and number_2 != 0:
            result = number_1 // number_2
            print('Итог => ', result)
        else:
            print('На ноль делить нельзя!')
            print('Попробуйте еще раз :)')
            return calculator()
    elif operat == '%':
        if number_1 != 0 and number_2 != 0:
            result = number_1 % number_2
            print('Итог => ', result)
        else:
            print('На ноль делить нельзя!')
            print('Попробуйте еще раз :)')
            return calculator()
    elif operat == '**':
        result = number_1**number_2
        print('Итог => ', result)
    else:
        print('[Ошибка] Нужно было выбрать операцию!')
        print('Попробуйте еще раз :)')
        return calculator()
    
calculator()
## finish
