import math

# from general import count0, count1, count2
from golden_ratio import golden_ratio
from dichotomy import dichotomy
from passive_search import passive_search
from general import func, deriv, deriv2
from newton import newton
from tangent import tangent

def main():
    print('Passive search')
    res_p = passive_search(func, 0.0, math.pi)
    print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_p[0], float.hex(res_p[1]), float.hex(res_p[2])))
    func.callsNumber = 0
    print('-' * 20)
  
    print('Dichotomy')
    res_d = dichotomy(func, 0.0, math.pi)
    print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_d[0], float.hex(res_d[1]), float.hex(res_d[2])))
    func.callsNumber = 0
    print('-' * 20)

    print('Golden Ratio')
    res_g = golden_ratio(f=func, a=0.0, b=math.pi)
    print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_g[0], float.hex(res_g[1]), float.hex(res_g[2])))
    func.callsNumber = 0
    print('-' * 20)

    print('Tangent')
    res_t = tangent(func,deriv, 0.0, math.pi)
    print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_t[0], float.hex(res_t[1]), float.hex(res_t[2])))
    func.callsNumber = 0
    print('-' * 20)

    print('Newton')
    res_n = newton(func, deriv, deriv2, 0.0, math.pi)
    print("min_aprox: {:.7}, f(min_aprox): {:.9}".format(float.hex(res_n[0]), float.hex(res_n[1])))
    deriv.callsNumber = 0
    deriv2.callsNumber = 0
	


if (__name__ == '__main__'):
  main()
