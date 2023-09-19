import math as m

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# patronymic = input('Введите отчество: ')

name = 'Анвер'
surname = 'Гаджиев'
patronymic = 'Пулатович'


# name = '1'
# surname = '1'
# patronymic = '1'

name_len = len(name)
surname_len = len(surname)
patr_len = len(patronymic)

D = name_len + surname_len + patr_len

name_len *= 10**(-name_len)
patr_len *= 10**(-patr_len)
surname_len *= 10**(-surname_len)

a = name_len
b = patr_len
c = surname_len 

count0 = 0
count1 = 1
count2 = 2

default_accuracy = 16**(-6)

def acc(num):
    order = int(m.log(num, 16))
    return 16 ** (order - 3)

def func(x):
    global count0
    count0 += 1
    return m.e**(name_len * x) + m.e**(patr_len * x) + m.e**(surname_len *
                                                             x) - D * m.sin(x)
    # return - D*m.sin(x)

def deriv(x):
    global count1
    count1 += 1
    return a*m.e**(a * x)  + b*m.e**(b * x) + c*m.e**(c * x) - D * m.cos(x) 
    

def deriv2(x):
    global count2
    count2 += 1
    return (a**2)*m.e**(a * x) + (b**2)*m.e**(b * x) + (c**2)*m.e**(c *x) + D * m.sin(x) 