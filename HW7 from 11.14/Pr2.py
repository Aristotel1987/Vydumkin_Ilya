
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Считывание данных из CSV файлов
X = pd.read_csv('6_x.csv')
y = pd.read_csv('6_y.csv')
# Убедимся, что данные правильно считаны
print("X:\n", X.head())
print("y:\n", y.head())
# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2 , random_state=42) # Зафиксируем разбиение, для повторяемости результатов при повторных запусках
#Создадим  функцию для оценки модели
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test) # Рассчитываем предсказанные значения
    mse = mean_squared_error(y_test, y_pred) #
    r2 = r2_score(y_test, y_pred)
    return mse, r2
# Линейная регрессия по каждому из признаков
metrics_linear = {} # Создаем словарь, для хранения результатов
for column in X.columns: # создаем цикл по столбцам датафрейма
    model = LinearRegression()
    model.fit(X_train[[column]], y_train)
    mse, r2 = evaluate_model(model, X_test[[column]], y_test)
    metrics_linear [column] = [mse, r2] # Записываем параметры модели в словарь результатов
# Множественная регрессия по всем признакам
multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)
mse, r2= evaluate_model(multiple_model, X_test, y_test)
metrics_linear['Multiple'] =[mse, r2] # Записываем данные модели в словарь результатов
print(f"Коэффициенты модели: {multiple_model.coef_}")
print(f"Свободный член (intercept): {multiple_model.intercept_}")
# Построение полиномиальных регрессий
for column in X.columns:
    # Полином степени 2
    poly_features = PolynomialFeatures(degree=2)
    X_poly_train = poly_features.fit_transform(X_train[[column]])
    X_poly_test = poly_features.transform(X_test[[column]]) # преобразуем тренировочную и тестовую выборки
    poly_model = LinearRegression()
    poly_model.fit(X_poly_train, y_train)
    mse, r2 = evaluate_model(poly_model, X_poly_test, y_test)
    metrics_linear[column+'^2'] =[mse, r2] # Записываем данные модели в словарь результатов
# Полином степени 3
for column in X.columns:
    poly_features = PolynomialFeatures(degree=3)
    X_poly_train = poly_features.fit_transform(X_train[[column]])
    X_poly_test = poly_features.transform(X_test[[column]]) # преобразуем тренировочную и тестовую выборки
    poly_model = LinearRegression()
    poly_model.fit(X_poly_train, y_train)
    mse, r2 = evaluate_model(poly_model, X_poly_test, y_test)
    metrics_linear[column+'^3'] =[mse, r2] 
#Сводная таблица результатов
pivot=pd.DataFrame(metrics_linear).T # преобразуем словарь результатов в dataframe, транспонируем, для удобства чтения
pivot.columns = ['MSE', 'R^2'] # добавляем заголовки к столбцам
print(pivot) # Выводим сводную таблицу по всем регрессиям
# В результате анализа таблицы было решено построить полиномиальную регрессию 2 го порядка с x2 и x3
X_test=X_test.drop(columns='X1')
X_train=X_train.drop(columns='X1')
poly_features = PolynomialFeatures(degree=2)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test) # преобразуем тренировочную и тестовую выборки
poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
mse, r2 = evaluate_model(poly_model, X_poly_test, y_test)
metrics_linear['multiple^2'] =[mse, r2] # Записываем данные модели в словарь результатов
pivot=pd.DataFrame(metrics_linear).T # преобразуем словарь результатов в dataframe, транспонируем, для удобства чтения
pivot.columns = ['MSE', 'R^2'] # добавляем заголовки к столбцам
print(pivot) # Выводим сводную таблицу по всем регрессиям
