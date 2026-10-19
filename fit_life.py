# Проект FitLife - MVP версия 1.0
# Рекомендуемое значение для поддержания водного баланса, в мл.
WATER_ML_PER_KG = 30

# Узнаем имя и возраст пользователя
user_name = input('Как тебя зовут? ')
print('\nПриветствую,', user_name.title(), end=", ")
user_age = int(input('сколько Вам полных лет? '))

# Узнаем вес и рост пользователя
user_weight = float(input('Укажите свой вес в кг: '))
user_height = float(input('Укажите свой рост в м (Например, 1.65): '))

# Рассчитываем индекс массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды и перевод в литры.
water_l = round(((user_weight * WATER_ML_PER_KG) / 1000), 1)

# Вывод результатов
print(f'\n*Поздравляю, {user_name.title()} , отчёт готов:*')
print(f'-Ваш возраст: {user_age} г.')
print(f'-Индекс Массы Тела: {bmi}')
print(f'-Рекомендуемая норма воды: {water_l} л. в день\n')
print('Расчет завершен. Пока.')
