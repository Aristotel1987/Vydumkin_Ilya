
import zipfile
import os
import dask.dataframe as dd
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

# Путь к распакованномуархиву
csv_directory = os.path.join(extract_directory, 'recipes_full')

# Забираем все CSV файлы в Dask DataFrame с указанием типов данных
df = dd.read_csv(os.path.join(csv_directory, '*.csv'), dtype={'minutes': 'float64', 'n_steps': 'float64'})

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

# Подсчёт количества отзывов с группировкой по месяцам добавления
# преобразуем дату подачи в формат даты
#df['time'] = dd.to_datetime(df['date'])
# Создаем новый столбец с месяцем
df['month'] = df['time'].dt.to_period('M')
# Агрегируем данные по месяцам, 
# monthly_agg_sorted = monthly_agg.sort_value_by('month') 
#print(monthly_agg_sorted)


#reviews_per_month = df.groupby(df['submitted'].dt.to_period('M')).size().compute()
#print("Количество отзывов по месяцам:\n", reviews_per_month)

# Находим пользователя, отправлявшего рецепты чаще всех
top_user = df['contributor_id'].value_counts().idxmax().compute()
print(f"Пользователь, отправлявший рецепты чаще всех: {top_user}")

