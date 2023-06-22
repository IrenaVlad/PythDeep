# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def triangle(a, b, c):
    if (a == b) and (b == c):
        return 'Треугольник равносторонний'
    elif ((a == b) or (a == c) or (c == b) and (a + b > c) and (a + c > b) and (b + c > a)):
        return 'Треугольник равнобедренный'
    elif (a + b > c) and (a + c > b) and (b + c > a):
        return 'Треугольник существует'
    else:
        return 'Треугольник не существует'
    
def Main():
    print("Введите стороны треугольника a, b, c")
    a = int(input("a = "))
    b = int(input("b = "))
    c= int(input("c = "))
    print(triangle(a,b,c))

Main()
#3. Напишите код, который запрашивает число и сообщает является ли оно простым 
# или составным. Используйте правило для проверки: “Число является простым, 
# если делится нацело только на единицу и на себя”. Сделайте ограничение на 
# ввод отрицательных чисел и чисел больше 100 тысяч.

def prime(number):
    if number > 1 and number < 100000:
        for i in range(2, (number//2)+1):
            if number % i == 0:
                return 'Число составное'
            return 'Число простое'
    else:
        return 'На ввод принимаются числа от 1 до 100000'
    
def main():
    number = int(input('Введите число '))
    print(prime(number))

main()