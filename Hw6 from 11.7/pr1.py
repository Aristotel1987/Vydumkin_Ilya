import zipfile
import sqlite3
import os
import pandas as pd
import sqlalchemy
def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Файл {zip_path} был успешно разархивирован в {extract_to}")
zip_file_path = 'recipes_full.zip'  # Путь к ZIP файлу
extract_directory =os.path.dirname(os.path.abspath(__file__)) # Папка, куда будет разархивирован файл
unzip_file(zip_file_path, extract_directory)
first_file_path = os.path.join(os.path.join(os.getcwd(), 'recipes_full'), 'recipes_full_1.csv' )
df = pd.read_csv(first_file_path)
# Проверяем типы данных столбцов
print(df.dtypes)
# Находим максимальное значение в столбце n_steps
max_n_steps = df['n_steps'].max()
print(f"Максимальное количество шагов: {max_n_steps}")
df['date'] = pd.to_datetime(df['submitted']) # преобразуем дату подачи в формат даты
reviews_per_month = df.groupby(df['date'].dt.to_period('M')).size()
print("Количество отзывов по месяцам:\n", reviews_per_month)
# Находим пользователя, который отправлял рецепты чаще всех
top_user = df['contributor_id'].value_counts().idxmax()
print(f"Пользователь, отправлявший рецепты чаще всех: {top_user}")

# Находим самый первый и самый последний рецепт 
first_recipe = df.loc[df['date'].idxmin()], False
last_recipe = df.loc[df['date'].idxmax()]
print(f"Самый первый рецепт:\n{first_recipe}\n")
print(f"Самый последний рецепт:\n{last_recipe}\n")

# Определяем медианы по количеству ингредиентов и по времени приготовления
medians = df[['n_ingredients', 'minutes']].median()
print(f"Медианы по количеству ингредиентов и времени приготовления:\n{medians}\n")
# Находим самый простой рецепт 
simplest_recipe = df.sort_values(by=['n_ingredients', 'minutes', 'n_steps'], ascending=[True, True, True]).iloc[0]
print("Самый простой рецепт:")
print(simplest_recipe)
# Загружаем рецепты в базу данных SQLite
conn = sqlite3.connect('recipes.db')  # Создаем или открываем базу данных SQLite
df.to_sql('recipes', conn, if_exists='replace', index=False)  # Заменяем таблицу, если она существует

# Проверяем загружены ли данные из таблицы, скачивая их по sql запросу для следующего вопроса
median_time = df['minutes'].median()  # Вычисляем медиану времени приготовления
mean_steps = df['n_steps'].mean()      # Вычисляем среднее количество шагов
query = f'SELECT * FROM recipes WHERE minutes < {median_time} AND n_steps < {mean_steps}'
loaded_df = pd.read_sql_query(query, conn)
#print("Данные, загруженные из базы данных:\n", loaded_df)
conn.close()  # Закрываем соединение с базой данных
loaded_df.to_csv('loaded_recipes.csv', index=False) # сохраняем результаты sql запроса в csv файл
print(f'Данные успешно загружены, отобрано {len(loaded_df)} рецептов.')
