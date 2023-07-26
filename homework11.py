# Задача 1

# Создайте класс 'Моя Строка', где:
# будут доступны все возможности str,
# дополнительно хранятся имя автора строки и время создания (time.time).

# import time
# class MyString(str):
#
#     def __new__(cls, text, nameAuthor):
#         instance = super().__new__(cls, text)
#         instance.t = time.time()
#         instance.author = nameAuthor
#         return instance
#
# text = """Author comment"""
# d = MyString(text, "Alex")
# print(d.__dict__)

# Задача 2

# Создайте класс 'Архив', который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов,
# list-архивы также являются свойствами экземпляра.

# class Archive():
#     _flag = None
#     """Почему комментарии в самом классе? Потому что это документация ©Зухра"""
#
#
#     def __new__(cls, number, text):
#         """"Непонятная функция заполняет архив старыми значениями"""
#
#         if cls._flag == None:
#             cls._flag = super().__new__(cls)
#             cls._flag.archNumber = []
#             cls._flag.archText = []
#         elif cls._flag != None:
#             cls._flag.archText.append(cls._flag.text)
#             cls._flag.archNumber.append(cls._flag.number)
#         return cls._flag
#
#     def __init__(self, number, text):
#         self.number = number
#         self.text = text
#
#     def __str__(self):
#         return f'{"".join(x for x in self.archText)} - архив,  текущий номер {self.number}'
#
#     def __repr__(self):
#         return f'{self.text}'
#
#     def docs(self):
#         return self.__doc__
#
# t = Archive(12, "jksagdjsagdkjalhsdk aksjdhlka jahdk kjahs")
# t2 = Archive(12, "jksagdjsagdkjalhsdk sadqqqqq qqqq")
# print()
# print(t2)
# print(repr(t2))

# Задача 3

# Добавьте к задачам 1 и 2 строки документации для классов.

# Задача 4

# Доработаем класс 'Архив' из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Задача 5

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# class rectangle():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         c = self.a + other.a
#         d = self.b + other.b
#         return rectangle(c, d)
#
#     def __sub__(self, other):
#         p1 = 2 * (self.a+self.b)
#         p2 = 2 * (other.a + other.b)
#         if p1 > p2 :
#             c = self.a - other.a
#             d = self.b - other.b
#         else:
#             c = other.a - self.a
#             d = other.b - self.b
#         return rectangle(c,d)
#
#     def __str__(self):
#         return "x".join([str(self.a), str(self.b)])
#
#     def __eq__(self, other):
#         if self.a * self.b == other.a * other.b:
#             return True
#         else : return False
#
#     def __lt__(self, other):
#         if self.a * self.b < other.a * other.b:
#             return True
#         else: return False
#
#     def __le__(self, other):
#         if self.a * self.b > other.a * other.b: return True
#         else : False
#
#
# pr1 = rectangle(2, 4)
# pr2 = rectangle(4, 2)
# print(pr1-pr2, pr1+pr2)
# print(pr1==pr2)
# print(pr1<pr2)

# Задача 6

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

class Matrix:
    '''Класс матрица с инициализацией списка списков,с переопределенными
     методами сложения и умножения и строчного вывода.'''

    def __init__(self, list_of_lists: list[list[int]]):
        '''Инициализация инит с аргументом list[list[int]].'''
        self.list_of_lists = list_of_lists

    def __str__(self):
        'Вывод списка списков построчно.'
        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        '''Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент.'''
        return True if self.list_of_lists == other.list_of_lists else False

    def __add__(self, other):
        '''Переопределил метод поэлементного сложения матриц.
        Можно складывать матрицы одинаковой длины строки первой и столбца второй. '''
        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        '''Переопределенный метод умножения матриц.
        Можно складывать матрицы одинаковой длины строки первой и столбца второй.'''
        m = len(self.list_of_lists)
        n = len(other.list_of_lists)
        k = len(other.list_of_lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list_of_lists[i][k] * other.list_of_lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')