import numpy as np
import random
matrix_1=np.array( [[random.randrange(-100, 100) for i in range(10)] for j in range(10)]) # генерируем матрицу 10 на 10
determ=np.linalg.det(matrix_1) #считаем определитель
rang1=np. linalg. matrix_rank(matrix_1, tol=None) # определяем ранг матрицы
matrix_1tr=np.transpose(matrix_1) # Транспонируем матрицу
sobs=np. linalg.eig(matrix_1) # Считаем собственные числа и векторы
print('Определитель и ранг матрицы равны', determ, rang1) #выведем для проверки определитель и ранг матрицы на экран
print(sobs) # Выведем собственные вектора длясамопроверки
matrix_2=np.array( [[random.randrange(-100, 100) for i in range(10)] for j in range(10)]) # генерируем 2ю матрицу 10 на 10
sum=matrix_1+matrix_2 #Сложим матрицы
mult=matrix_1.dot(matrix_2) #Перемножим матрицы
print(sum, mult)