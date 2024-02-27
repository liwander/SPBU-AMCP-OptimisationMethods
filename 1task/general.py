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

# count0 = 0
# count1 = 0
# count2 = 0

def hex(
        f: float,
        n=4
) -> str:
    
    h = float.hex(float(f))
    a, B = h.split(".")
    B = B.split("p")
    end = ""
    if len(B) > 1:
        end = "p" + B[1]
    B[0] += "00000"
    return a + "." + B[0][:n] + end

default_accuracy = 16**(-6)

def acc(num):
    order = int(m.log(num, 16))
    return 16 ** (order - 3)


def counted(function):
    '''
    Decorator for counting function calls 
    '''
    def func_wrapper(*args, **kvargs):
        func_wrapper.callsNumber += 1
        return function(*args, **kvargs)
    
    func_wrapper.callsNumber = 0
    return func_wrapper

@counted
def func(x):
    # global count0
    # count0 += 1
    return m.e**(name_len * x) + m.e**(patr_len * x) + m.e**(surname_len *
                                                             x) - D * m.sin(x)
    # return - D*m.sin(x)
@counted
def deriv(x):
    # global count1
    # count1 += 1
    return a*m.e**(a * x)  + b*m.e**(b * x) + c*m.e**(c * x) - D * m.cos(x) 
    
@counted
def deriv2(x):
    # global count2
    # count2 += 1
    return (a**2)*m.e**(a * x) + (b**2)*m.e**(b * x) + (c**2)*m.e**(c *x) + D * m.sin(x) 

