a, b, c=float(input('ВВедите коэффициенты квадратного уравнения, последовательно, через  Enter')), float(input()), float(input())
D=b**2-4*a*c
if D<0:# Проверяем дискриминант на наличие корней
    print('Действительных корней у уравнения нет')
elif D==0:
    print('Единственный корень уравнения равен',b/(2*a))
else:
    print('Корни уравнения равны:', (b-D**0.5)/(2*a), 'и', (b+D**0.5)/(2*a))
  
