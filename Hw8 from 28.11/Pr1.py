import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift, SpectralClustering, Birch
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.datasets import load_wine
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Загрузим данные о вине
data = load_wine()   
# Преобразуем данные в DataFrame для удобства работы
df = pd.DataFrame(data.data, columns=data.feature_names)
# Выводим описательную статистику
statistics = df.describe()
print('Описательная статистика\n', statistics)
# Выводим первые 5 строк
print(df.head())
print(f'Количество пропусков в данных: {df.isnull().sum().sum()}')   # Проверяем данные на пропуски

# Стандартизуем данные
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

n_clusters = 3  # число кластеров, в нашем случае 3 региона 

# Кластеризация с использованием различных алгоритмов

# KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans_labels = kmeans.fit_predict(df_scaled)

# Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=n_clusters)
agglo_labels = agglo.fit_predict(df_scaled)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(df_scaled)

# Mean Shift
mean_shift = MeanShift()
mean_shift_labels = mean_shift.fit_predict(df_scaled)

# Spectral Clustering
spectral_clustering = SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors', random_state=42)
spectral_labels = spectral_clustering.fit_predict(df_scaled)

# Birch
birch = Birch(n_clusters=n_clusters)
birch_labels = birch.fit_predict(df_scaled)

# Оценка качества кластеризации

# Словарь для хранения результатов
results = {}

# Функция для оценки и хранения результатов
def evaluate_model(model_name, labels):
    if len(set(labels)) > 1:  # Проверяем, есть ли более одной метки
        silhouette = silhouette_score(df_scaled, labels)  # Силуэтный коэффициент
        adjusted_rand = adjusted_rand_score(data.target, labels) if np.max(labels) >= 0 else None  # ARI, если метки доступны
        
        # Оценка метрик классификации
        print(f"\nМетрики для модели {model_name}:")
        print("Confusion Matrix:\n", confusion_matrix(data.target, labels))
        print("Classification Report:\n", classification_report(data.target, labels))
        accuracy = accuracy_score(data.target, labels)
        print("Accuracy Score:", accuracy)
        
    else:
        silhouette = None
        adjusted_rand = None
    
    results[model_name] = {
        'Silhouette Score': silhouette,
        'Adjusted Rand Index': adjusted_rand,
        'Accuracy Score': accuracy if 'accuracy' in locals() else None,
    }

# Оценка моделей
evaluate_model('KMeans', kmeans_labels)
evaluate_model('Agglomerative Clustering', agglo_labels)
evaluate_model('DBSCAN', dbscan_labels)
evaluate_model('Mean Shift', mean_shift_labels)
evaluate_model('Spectral Clustering', spectral_labels)
evaluate_model('Birch', birch_labels)

# Вывод результатов
results_df = pd.DataFrame(results).T
print("\nРезультаты оценки кластеризации:")
print(results_df)
# Используем K-means++ для инициализации
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
kmeans_labels = kmeans.fit_predict(df_scaled)

# Оценим качество кластеризации
silhouette = silhouette_score(df_scaled, kmeans_labels)
adjusted_rand = adjusted_rand_score(data.target, kmeans_labels)
# Выводим параметры модели
print("Параметры K-Means:")
print("--------------------------------")
print(f"Количество кластеров (n_clusters): {kmeans.n_clusters}")
print(f"Центры кластеров (centroids):\n{kmeans.cluster_centers_}")
print(f"Количество итераций (n_iter): {kmeans.n_iter_}")
print(f"Сумма квадратов ошибок (inertia): {kmeans.inertia_}")
print(f"Методы инициализации (init): {kmeans.init}")
print(f"Состояние рандома (random_state): {kmeans.random_state}")
print(f"Признаки кластеров (labels):\n{kmeans.labels_}")


print(f'Silhouette Score: {silhouette}')
print(f'Adjusted Rand Index: {adjusted_rand}')
