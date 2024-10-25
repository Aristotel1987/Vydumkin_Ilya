words=['tree', 'mountain', 'river', 'cloud', 'book', 'chair', 'light', 'window', 'phone', 'mirror', 'sky', 'dream', 'road', 'smile', 'shadow']
def convert( word): # напишем функцию перевода слов в числовой код
    code=0
    for i in word:
        code+=ord(i)
    return code
numbers=[] # Создадим список чисел, соотносящийся со словами
for i in words:
    numbers.append(convert(i))
dict_1=dict(zip(words, numbers)) # Соберем оба списка в словарь
value=convert(input('ВВедите искомое слово.'))
dict_1=sorted(dict_1.items(), key=lambda j: j[1])
# индексы первого элемента, последнего и среднего
low = 0
high = len(dict_1) - 1
mid = len(dict_1) // 2

while dict_1[mid][1] != value and low <= high:
    if value > dict_1[mid][1]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('No such word.')
else:
    print(*dict_1[mid])
#print(dict_1)