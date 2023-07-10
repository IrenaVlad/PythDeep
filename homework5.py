# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# path = r'C:\Thecode\Media\статья.txt'


# def split_path(path: str) -> tuple():
#    list_path = path.split('\\')
#    list_last_elem = list_path[-1].split('.')
#    abpath = '\\'.join(list_path[0:-1])
#    name = list_last_elem[0]
#    expansion = list_last_elem[1]
#    return abpath, name, expansion

# print(split_path(path))

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, 
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой 
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии 

# names = ['Marisa', 'Jose', 'Luis', 'Paloma']
# salary = [2000, 1500, 2500, 5000]
# bonus = ['10.25%', '15.00%', '10.00%', '15.00']

# def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
#    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()


#print(*(salary_gen(names, salary, bonus)))

# Создайте функцию генератор чисел Фибоначчи

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fib(10)))