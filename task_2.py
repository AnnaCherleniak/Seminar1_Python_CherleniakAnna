# 2. Напишите код, который запрашивает число и сообщает является
# ли оно простым или составным.
# Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = 99999
START = 2
STOP = number
count = 0
min_border = 0
max_border = 100000
if number < min_border or number > max_border:
    print('Введите число от 1 до 100 000')
if number == 1 or number == 0:
    print('Числа 0 и 1 не являются ни простым, ни сложным')
else:
    for num in range(START, STOP):
        if number % num == 0:
            print('Число составное')
            count += 1
            break
    if count == 0:
        print('Число простое')