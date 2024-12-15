# Отчет по кластеризации данных во встроенной базе по вину в библиотеке sklearn в Python

На основе проведенной ранее классификации было принято решение оценить, насколько данные о химических показателях напитка хорошо поддаются кластеризации и насколько эта кластеризация совпадает с регионом происхождения вина.

Предварительно данные были проверены на отсутствие пропусков, существенных выбросов (более 2,56 стандартных отклонений), отнормализованы к Гауссовскому распределению со средним 0 и дисперсией 1.

Для кластеризации применялись следующие модели:
- KMeans
- Agglomerative Clustering         
- DBSCAN                            
- Mean Shift                    
- Spectral Clustering
- Birch                            

Для сравнения моделей кластеризации применялись следующие метрики:
- **Silhouette score** - коэффициент, позволяющий оценить плотность кластера, насколько близко точка находится к точкам своего кластера и насколько далеко от точек из других кластеров.
- **Adjusted Rand Index** - коэффициент, отражающий меру схожести двух разбиений, модифицированный коэффициент Ранда. В нашем случае сравнивает целевую функцию региона с предсказанными метками модели кластеризации.
- **Confusion Matrix** - матрица ошибок, наиболее понятный способ сопоставить два разбиения данных.

Программа также подсчитывает остальные показатели, которые обычно используются для проверки точности классификации, но в данном отчете мы их использовать не будем. 

# Сравнение моделей

Силуэтный коэффициент и модифицированный показатель Ранда для всех моделей представлены ниже:

| Модель                      | Silhouette Score | Adjusted Rand Index |
|-----------------------------|------------------|----------------------|
| KMeans                      | 0.284859         | 0.897495             |
| Agglomerative Clustering    | 0.277444         | 0.789933             |
| DBSCAN                      | None             | None                 |
| Mean Shift                  | 0.224476         | -0.006424            |
| Spectral Clustering         | 0.28285          | 0.8804               |
| Birch                       | 0.277444         | 0.789933             |

Матрицы ошибок также представлены ниже:

**KMeans:**

[[ 0  0 59]
 [65  3  3]
 [ 0 48  0]]

**Agglomerative Clustering:**

[[ 0  0 59]
 [58  8  5]
 [ 0 48  0]]

**Mean Shift:**

[[59  0  0]
 [67  4  0]
 [48  0  0]]

**Spectral Clustering:**

[[ 0 59  0]
 [ 3  4 64]
 [48  0  0]]

**Birch:**

[[ 0  0 59]
 [58  8  5]
 [ 0 48  0]]

Как мы видим из всех показателей, лучшие 2 модели кластеризации, это:
- KMeans
- Spectral Clustering   

Причем первая немного лучше, допускает всего лишь 6 ошибок из 178 наблюдений. При этом кластеризация на достаточно низком уровне, силуэтный коэффициент всего 0.285, существенно ниже 1. Удивительно, как при такой кластеризации модель достаточно точно предсказывает регион происхождения вин, допуская ошибки только во втором регионе, и не более 10% от вин из этого региона.

Для улучшения модели KMeans, так как ее результаты сильно зависят от первоначального выбора точек-центроидов в оптимизационной модели, была предпринята попытка использовать метод K-Means++, который позволяет выбирать начальные центроиды более сбалансированным образом и не дает алгоритму зависнуть в локальном минимуме. 

Однако его применение не дало существенных результатов, не изменило ни силуэтный коэффициент, ни модифицированный коэффициент Ранда, ни матрицу ошибок.

Таким образом, лучшей моделью кластеризации следует принять - KMeans. Ее параметры, включая центроиды кластеров, все метки наблюдений, количество итераций, метод инициализации и др., есть в выводе программы.