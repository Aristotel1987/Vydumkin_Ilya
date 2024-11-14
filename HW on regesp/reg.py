import re
# Открываем файл для чтения
with open('prust.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    text = file.read()
# Регулярное выражение для поиска всех слов, начинающихся на "Прус"
pattern_prust = r'\bПрус\w*'
# Регулярное выражение для поиска слов более 17 букв
pattern_long_words = r'\b\w{17,}\b'
# Регулярное выражение для поиска слов, оканчивающихся на "!" или "?"
pattern_exclamation = r'\b\w+[!?]\b'

# Находим все совпадения
matches_prust = re.findall(pattern_prust, text)
matches_long_words = re.findall(pattern_long_words, text)
matches_exclamation = re.findall(pattern_exclamation, text)

# Выводим найденные слова
print("Слова, начинающиеся на 'Прус':")
for word in matches_prust:
    print(word)

print("\nСлова, состоящие более чем из 17 букв:")
for word in matches_long_words:
    print(word)

print("\nСлова, оканчивающиеся на '!' или '?':")
for word in matches_exclamation:
    print(word)
