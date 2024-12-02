import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV
# Загрузим данные о вине
data = load_wine()   
# Преобразуем данные в DataFrame для удобства работы
df = pd.DataFrame(data.data, columns=data.feature_names)
# Добавим целевую переменную в DataFrame
df['target'] = data.target 
reviews_per_region= df.groupby(df['target']).size()
print("Количество вин по регионам происхождения\n", reviews_per_region)
# Выводим описательную статистику
statistics = df.describe()
print('Описательная статистика факторов \n', statistics)
# Выводим первые 5 строк
print(df.head())
print(f'Количество прпусков в данных:{df.isnull().sum().sum()}')   #Проверяем  данные на пропуски
 #Вводим переменные для моделей
X= df.drop('target', axis=1)  # Убираем целевую переменную из датасета
y = df['target']  # Сохраняем целевую переменную
# Стандартизация данных
scaler = StandardScaler()  # используем нормальное распределение для стандартизации
X_scaled = scaler.fit_transform(X)  # Применяем стандартизацию
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
#Построение различных моделей 
log_reg = LogisticRegression(max_iter=10000)  # Увеличим количество итераций для сходимости
log_reg.fit(X_train, y_train)  # Обучаем модель
y_pred_log_reg = log_reg.predict(X_test)  # Предсказание на тестовой выборке

# SVM (машина наименьших квадратов)
svm_model = SVC()  # Создание модели SVM
svm_model.fit(X_train, y_train)  # Обучаем модель
y_pred_svm = svm_model.predict(X_test)  # Предсказание на тестовой выборке

#  KNN (к-ближайших соседей)
knn_model = KNeighborsClassifier(n_neighbors=5)  # Создание модели KNN
knn_model.fit(X_train, y_train)  # Обучаем модель
y_pred_knn = knn_model.predict(X_test)  # Предсказание на тестовой выборке


#  Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # Создание модели Random Forest
rf_model.fit(X_train, y_train)  # Обучаем модель
y_pred_rf = rf_model.predict(X_test)  # Предсказание на тестовой выборке
#Оценка моделей
models = ['Logistic Regression', 'SVM', 'KNN', 'Random Forest']
predictions = [y_pred_log_reg, y_pred_svm, y_pred_knn, y_pred_rf]

for model_name, preds in zip(models, predictions):
    print(f"\n{model_name}:\n")
    print("Точность:", accuracy_score(y_test, preds))  # Точность
    print("Отчет по классификации:\n", classification_report(y_test, preds))  # Отчет по классификации

    print("Матрица ошибок:\n", confusion_matrix(y_test, preds))  # Матрица ошибок
# Подбор параметров для логистической регрессии
param_grid_log_reg = {
    'penalty': ['l1', 'l2', 'elasticnet', 'none'],  # Тип регуляризации
    'C': [0.001, 0.01, 0.1, 1, 10, 100],  # Обратная величина регуляризации
    'solver': ['lbfgs', 'liblinear', 'saga'],  # Алгоритмы оптимизации
    'max_iter': [100, 1000]  # Максимальное количество итераций
}

grid_search_log_reg = GridSearchCV(LogisticRegression(), param_grid_log_reg, 
                                    scoring='accuracy', cv=5, n_jobs=-1, verbose=1)

grid_search_log_reg.fit(X_train, y_train)  # Обучаем модель с настройкой гиперпараметров

# Лучшие параметры
best_params_log_reg = grid_search_log_reg.best_params_
print("Лучшие параметры для логистической регрессии:", best_params_log_reg)

# Оценка модели с лучшими параметрами
best_log_reg_model = grid_search_log_reg.best_estimator_
y_pred_best_log_reg = best_log_reg_model.predict(X_test)

# Оценка точности
print("\nЛогистическая Регрессия с лучшими параметрами:\n")
print("Точность:", accuracy_score(y_test, y_pred_best_log_reg))  # Точность
print("Отчет по классификации:\n", classification_report(y_test, y_pred_best_log_reg))  # Отчет по классификации
print("Матрица ошибок:\n", confusion_matrix(y_test, y_pred_best_log_reg))  


# Выводим параметры лучшей модели
#print(rf_model.get_params())

