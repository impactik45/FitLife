# Проект FitLife - MVP версия 1.0
# Рекомендуемое значение для поддержания водного баланса, в мл.
WATER_ML_PER_KG = 30
ML_PER_LITER = 1000

# Узнаем имя и возраст пользователя
user_name = input('Как тебя зовут? ')
print('\nПриветствую,', user_name.title(), end=', ')
while True:
    try:
        user_age = int(input('Сколько Вам полных лет? '))
        if user_age <= 0:
            print('Ошибка: Значение должно быть положительным числом.')
            continue
        break
    except ValueError:
        print('Ошибка: возраст должен быть введен цифрами целым числом.')

# Узнаем вес пользователя
while True:
    try:
        user_weight = float(input('Укажите свой вес в кг: '))
        if user_weight <= 0:
            print('Ошибка: Значение должно быть положительным числом')
            continue
        break
    except ValueError:
        print('Ошибка: Вес должен быть числом (например, 50 или 84).')

# Узнаем рост пользователя
while True:
    try:
        user_height = float(input('Укажите свой рост в м (Например, 1.65): '))
        if user_height <= 0:
            print('Ошибка: Значение должно быть положительным числом')
            continue
        break
    except ValueError:
        print('Ошибка: Рост должен быть числом и указан через точку.')

# Рассчитываем индекс массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды и перевод в литры.
water_l = round(user_weight * WATER_ML_PER_KG / ML_PER_LITER, 1)

# Вывод результатов
print(f'\nПоздравляю, {user_name.title()}, отчёт готов:')
print(f'-Ваш возраст: {user_age} г.')
print(f'-Индекс Массы Тела: {bmi}')
print(f'-Рекомендуемая норма воды: {water_l} л. в день\n')
print('Расчет завершен. Пока.')
