# Отчет по регрессионному анализу зависимостей представленных данных

Анализировалась зависимость Y от X1, X2, X3, представленных в соответствующих файлах. Предварительно в CSV файлы были добавлены заголовки переменных. Было решено использовать случайное разбиение на тренировочную и тестовую выборки; для повторяемости результата случайность выборки была зафиксирована параметром `random_state`.

В результате анализа было первоначально построено 10 регрессионных моделей. По значению R-квадрат были отобраны 4 модели, объясняющие более 85% вариации в предсказываемой переменной. Это:

- линейная модель с X2,
- линейная модель со всеми тремя факторами,
- квадратичная модель с X2,
- полиномиальная третьей степени также с X2.

Лучшей была линейная множественная регрессия, ее предсказательная сила (R-квадрат) составляла 98,8%. Как видно из таблицы, представленной ниже, и по значению стандартизованной средней ошибки, она была лучше всех (150, против 1409 у ближайшей наилучшей модели).

Из анализа стандартных линейных моделей видно, что наибольшую долю вариации объясняет X2, в то время как X1 не может объяснить даже 10% наблюдаемой дисперсии. Также видно, что полином второй степени с X2 чуть лучше предсказывает Y, потому была предпринята попытка построить полиномиальную множественную регрессию с X2 и X3. Увеличивать число факторов, включая туда все переменные в различных степенях, не позволяет малое число наблюдений. Однако такая множественная квадратичная регрессия оказалась все равно хуже простой линейной множественной модели.

Окончательный вывод о характере зависимости следует делать из теоретических моделей и понимания источника данных. Лучшая из рассмотренных моделей выглядит следующим образом:


Y_predicted = -0.576 + 1.101 * X1 + 97.450 * X2 + 47.475 * X3 + eps


где:

- `Y_predicted` - предсказанное значение,
- `X1, X2, X3` - факторы из матрицы X,
- `eps` - ошибка наблюдения.

## Приложение

Сводная таблица сравнения всех построенных моделей.

| Модель      | MSE            | R²         |
|-------------|----------------|------------|
| X1          | 15487.659621   | -0.145934  |
| X2          | 1469.053383    | 0.891305   |
| X3          | 12940.468578   | 0.042533   |
| Multiple     | 150.127095     | 0.988892   |
| X1²        | 14719.875724   | -0.089126  |
| X2²        | 1408.589759    | 0.895778   |
| X3²        | 12909.890875   | 0.044795   |
| X1³        | 14596.593654   | -0.080004  |
| X2³        | 1769.670686    | 0.869062   |
| X3³        | 13013.449569   | 0.037133   |
| Multiple²   | 206.002950     | 0.984758   |
