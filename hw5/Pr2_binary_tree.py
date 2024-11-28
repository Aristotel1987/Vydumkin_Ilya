class TreeNode:
    def __init__(self, value):
        # Инициализация узла дерева с заданным значением
        self.value = value      # Хранит значение узла
        self.left = None       # Указатель на левого потомка
        self.right = None      # Указатель на правого потомка
        self.parent = None     # Указатель на родительский узел

class BinarySearchTree:
    def __init__(self):
        # Инициализация бинарного дерева
        self.root = None       # Корень дерева, по умолчанию равен None

    def add(self, value):
        # Метод для добавления нового узла в дерево
        new_node = TreeNode(value)  # Создаем новый узел с данным значением
        if self.root is None:
            # Если дерево пустое, новый узел становится корнем
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                # Если значение меньше, идем в левое поддерево
                if current.left is None:
                    # Если нет левого потомка, добавляем новый узел
                    current.left = new_node
                    new_node.parent = current  # Устанавливаем родителя
                    return
                current = current.left  # Переходим к левому потомку
            else:
                # Если значение больше или равно, идем в правое поддерево
                if current.right is None:
                    # Если нет правого потомка, добавляем новый узел
                    current.right = new_node
                    new_node.parent = current  # Устанавливаем родителя
                    return
                current = current.right  # Переходим к правому потомку

    def find(self, value):
        # Метод для поиска узла с заданным значением
        current = self.root
        while current:
            if value == current.value:
                return current  # Возвращаем узел, если найдено значение
            elif value < current.value:
                current = current.left  # Идем в левое поддерево
            else:
                current = current.right  # Идем в правое поддерево
        return None  # Возвращаем None, если значение не найдено

    def delete(self, value):
        # Метод для удаления узла с заданным значением
        node_to_delete = self.find(value)  # Находим узел для удаления
        if node_to_delete is None:
            print(f'Значение {value} не найдено.')  # Если узел не найден
            return

        # Случай 1: Удаляемый узел не имеет потомков (лист)
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent:
                # Обновляем родительский узел
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            else:
                self.root = None  # Если удаляемый узел - корень

        # Случай 2: Удаляемый узел имеет обоих потомков
        elif node_to_delete.left and node_to_delete.right:
            # Находим минимальный узел в правом поддереве для замены
            successor = self._find_min(node_to_delete.right)
            node_to_delete.value = successor.value  # Копируем значение
            self.delete(successor.value)  # Удаляем узел-последователь

        # Случай 3: Удаляемый узел имеет одного потомка
        else:

            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if node_to_delete.parent:
                # Обновляем родительский узел для одного потомка
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                if child:
                    child.parent = node_to_delete.parent
            else:
                # Если удаляемый узел - корень, обновляем его
                self.root = child
                if child:
                    child.parent = None

    def _find_min(self, node):
        # Помощник для нахождения минимального узла в поддереве
        while node.left:
            node = node.left
        return node  # Возвращаем минимум из поддерева

    def _print_tree(self, node, level=0, prefix="Root: "):
        # Рекурсивный метод для печати дерева
        if node is not None:
            print(' ' * (level * 4) + prefix + str(node.value))  # Печатаем узел
            if node.left:
                self._print_tree(node.left, level + 1, 'Left ')  # Печатаем левое поддерево
            if node.right:
                self._print_tree(node.right, level + 1, 'Right ')  # Печатаем правое поддерево

    def print_tree(self):
        # Метод для начала печати дерева
        if self.root is None:
            print('Невозможно вывести дерево на экран: дерево пустое.')
        else:
            self._print_tree(self.root)  # Вызываем рекурсивный метод

# Создаем экземпляр бинарного дерева и запускаем интерфейс командной строки
bst = BinarySearchTree()
while True:
    # Интерфейс для взаимодействия с пользователем
    command = input('Бинарное дерево\nВведите 1 для добавления значения в дерево\n 2 для поиска значения в дереве\n3 для удаления значения из дерева\n4 для печати дерева на экран.\nВведите ваш выбор (0- выход):')
    if command == '1':
        value = int(input('Введите значение для добавления: '))
        bst.add(value)  # Добавление значения
    elif command == '2':
        value = int(input('Введите значение для поиска: '))
        result = bst.find(value)  # Поиск значения
        if result:
            print(f'Значение {value} найдено.')  # Если найдено
        else:
            print('Такое значение в дереве отсутствует')  # Если не найдено
    elif command == '3':
        value = int(input('Введите значение для удаления: '))
        bst.delete(value)  # Удаление значения
    elif command == '4':
        bst.print_tree()  # Печать дерева
    elif command == '0':
        break  # Выход из программы
    else:
        print('Неизвестная команда, Попробуйте ввести ваш выбор еще раз.')  # Если введена неизвестная команда

### Основное назначение кода:
#Этот код реализует структуру данных "бинарное дерево поиска" (Binary Search Tree, BST) с базовыми операциями, такими как добавление, поиск, удаление и печать узлов. Интерфейс командной строки позволяет пользователю взаимодействовать с деревом, выполнять различные операции и выходить из программы.
