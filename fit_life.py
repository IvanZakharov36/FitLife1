import sys
sys.stdout.reconfigure(encoding='utf-8')

print('Добро пожаловать')
# спрашиваем у пользователя имя и возраст
user_name = input('Как вас зовут?')
user_age = int(input('Сколько вам лет?'))
# запрашиваем вес (в кг) и рост (в метрах)
user_weight = float(input('Какой у вас вес? (в кг)'))
user_height = float(input('Какой у вас рост? (например 1.50)'))
# рассчитываем индекс массы тела
bmi = round(user_weight / (user_height ** 2), 1)
# рассчитываем норму воды в миллилитрах
water_ml = float(user_weight * 30)
water_l = float(water_ml / 1000)
print()
print(f'отчет для пользователя: {user_name} {user_age}')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} {'литров в день'}')
print()
print('Расчет окончен, будьте здоровы')
