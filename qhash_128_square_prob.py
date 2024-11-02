# решение коллизий квадратичным пробированием
def insert():
    while True:  # цикл для добавления значений
        input_value = input('Введите значение для добавления в таблицу или "стоп" для окончания добавлений: ')
        if input_value != 'стоп':
            values_list = []  # список для хранения значений, добавляемых в таблицу
            current_key = calculate_hash(input_value)  # вычисление хэш-ключа для input_value
            
            # Проверка на существование ключа в хэш-таблице
            attempt = 1
            while True:
                if hash_table.get(current_key) is None:
                    values_list.append(input_value)
                    hash_table[current_key] = values_list  # добавляем пару ключ-значение в таблицу
                    attempt = 1
                    print(current_key)
                    break
                else:
                    current_key = current_key + attempt**2  # решаем коллизию добавлением к ключю номера попытки в квадрате (квадратичным пробированием)
                    attempt = attempt + 1
        else:
            break # завершаем цикл