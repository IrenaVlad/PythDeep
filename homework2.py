# 2.Напишите программу, которая получает целое число и возвращает его 
#шестнадцатеричное строковое представление. Функцию hex используйте для 
#проверки своего результата.
#def conv_number(num_dec, ss):
#    digits = "0123456789ABCDEFGHI"
#    num_conv = ""
#    while (num_dec > 0):
#        k = num_dec % ss
#        num_conv = digits[k] + num_conv
#        num_dec = num_dec // ss
#    return num_conv

#def Main():
#    number = int(input('Введите число в десятичной системе '))
#    for i in range(2, 17):
#        print(f'Ответ в {i}-ой СС:', conv_number(number, i))

#Main()

# Напишите программу, которая принимает две строки вида “a/b” - дробь с 
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
#  дробей. Для проверки своего кода используйте модуль fractions.

#import fractions

#str1 = str(input('Введите первую дробь вида a/b: '))
#str2 = str(input('Введите вторую: '))
#first = str1.split('/')
#second = str2.split('/')
# summa = str(int(first[0])*int(second[1]) + int(first[1])*int(second[0]))+ '/' + str(int(second[1])*int(first[1]))
#mult = str(int(first[0])*int(second[0])) +'/' + str(int(first[1])*int(second[1]))
#print(f'Сумма = {summa}, Произведение = {mult}')
#f1 = fractions.Fraction(int(first[0]), int(first[1]))
#f2 = fractions.Fraction(int(second[0]), int(second[1]))
#print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')