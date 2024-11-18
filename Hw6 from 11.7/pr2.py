import zipfile
import os
import dask.dataframe as dd
import matplotlib
matplotlib.use('Agg')  # Используем бэкенд Agg для работы без GUI
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Функция для разархивации ZIP файла
def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Файл {zip_path} был успешно разархивирован в {extract_to}")

# Путь к ZIP файлу
zip_file_path = 'recipes_full.zip'
# Определяем директорию нахождения архива
extract_directory = os.path.dirname(os.path.abspath(zip_file_path))
# Разархивируем файл
unzip_file(zip_file_path, extract_directory)

# Путь к распакованному архиву
csv_directory = os.path.join(extract_directory, 'recipes_full')

# Забираем все CSV файлы в Dask DataFrame с указанием типов данных
df = dd.read_csv(os.path.join(csv_directory, '*.csv'), dtype={'minutes': 'float64', 'n_steps': 'float64', 'submitted': 'str'})

# Выводим метаинформацию о Dask DataFrame
print(f"Число партий: {df.npartitions}")
print("Типы столбцов:\n", df.dtypes)

# Выводим первые 5 и последние 5 строк таблицы
print("Первые 5 строк:\n", df.head())
print("Последние 5 строк:\n", df.tail())

# Подсчёт строк в каждом блоке
for i in range(df.npartitions):
    print(f"Количество строк в блоке {i}: {df.get_partition(i).shape[0].compute()}")

# Находим максимум в столбце n_steps
max_n_steps = df['n_steps'].max()
print("Максимальное значение в n_steps:", max_n_steps.compute())

# Визуализируем граф вычислений максимального количества шагов
plt.figure(figsize=(8, 6))
plt.bar(['Max n_steps'], [max_n_steps.compute()], color='blue')
plt.title('Максимальное количество шагов (n_steps)')
plt.ylabel('Количество шагов')
plt.savefig('dask_max_steps_count.png')
plt.close()  # Закрываем фигуру

# Подсчёт количества отзывов с группировкой по месяцам добавления
df['time'] = dd.to_datetime(df['submitted'])  # Преобразуем дату подачи в формат даты
reviews_per_month = df.groupby(df['time'].dt.to_period('M')).size().compute()
print(reviews_per_month)  # Выводим количество по месяцам

# Находим пользователя, отправлявшего рецепты чаще всех
top_user = df['contributor_id'].value_counts().idxmax().compute()
print(f"Пользователь, отправлявший рецепты чаще всех: {top_user}")

# Первый и последний рецепт
last_rec = df.nlargest(1, 'time').compute()
print(f'Последний по дате рецепт: \n{last_rec}')
first_rec = df.loc[df['time'] == df['time'].min()].compute()
print(f'Первые по дате подачи рецепты: \n{first_rec}')

#Загружаем рецепты в базу данных SQLite
engine = create_engine('sqlite:///recipes.db')  # Устанавливаем подключение 
to_sql = df.to_delayed()  # Итерация по партиям с помощью to_delayed
for part in to_sql:
    part.to_sql('recipes', engine, if_exists='append', index=False)

print("Данные успешно загружены в SQLite.")
median_time = df['minutes'].median_approximate().compute()  # Вычисляем медиану времени приготовления
mean_steps = df['n_steps'].mean().compute()      # Вычисляем среднее количество шагов
# Загрузка данных из таблицы recipes, используя строку подключения
loaded_df = dd.read_sql_table('recipes', 'sqlite:///recipes.db', index_col='id')
# Фильтрация данных
filtered_df = loaded_df[(loaded_df['minutes'] < median_time) & (loaded_df['n_steps'] < mean_steps)]
# Сохраняем отфильтрованные данные в один CSV-файл
filtered_df.to_csv('filtered_recepts.csv', single_file=True, index=False)  
print("Отфильтрованные рецепты сохранены в filtered_recepts.csv.")