n=int(input('ВВедите грузоподъемность рюкзака вора'))
c={"laptop": (3, 1500), "camera": (1, 800), "phone": (1, 600), "watch": (0.5, 300), "headphones": (0.2, 200), "tablet": (2, 900), "wallet": (0.1, 100)}
# Рассчитаем цену товара на единицу веса
list_rat=[] #Создадим список цен одного кило товара
for i in c:
    list_rat.append(c[i][1]/c[i][0]) #Заполняем список деля цену товара на его вес
dict_val=dict(zip(list(c.keys()), list_rat)) # Создаем словарь товаров с ценой килограмма
from operator import itemgetter
dict_val=sorted(dict_val.items(), key=itemgetter(1)) # Сортируем словарь по стоимости кило
