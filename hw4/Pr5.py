import random
n=int(input('Введите требуемую длину пароля'))
password='' # Создаем пароль как строку
for i in range(n): #
    password+=chr(random.randrange(256)) # Добавляем к паролю случайный символ,  преобразуя его  из сл числа от 0 до 255
print( password) # Выводим итоговый пароль для проверки