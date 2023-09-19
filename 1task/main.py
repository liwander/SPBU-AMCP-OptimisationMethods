import math
from general import func, deriv
from newton import newton
from tangent import tangent

def main():
    # res_p = passive_search(func, 0.0, math.pi)
    # print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_p[0], float.hex(res_p[1]), float.hex(res_p[2])))
    # count = 0

    # res_d = dichotomy(func, 0.0, math.pi)
    # print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_d[0], float.hex(res_d[1]), float.hex(res_d[2])))
    # count = 0

    # res_g = golden_ratio(f=func, a=0.0, b=math.pi)
    # print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_g[0], float.hex(res_g[1]), float.hex(res_g[2])))
    # count = 0

    # res_t = tangent(func, 0.0, math.pi)
    # print("calls_number: {}, min__aprox: {:.7}, f(min__aprox): {:.9}".format(res_t[0], float.hex(res_t[1]), float.hex(res_t[2])))
    # count = 0

    res_n = newton(func, 0.0, math.pi)
    print("min_aprox: {:.7}, f(min_aprox): {:.9}".format(float.hex(res_n[0]), float.hex(res_n[1])))
    count = 0
    # print(deriv(0))
	


if (__name__ == '__main__'):
  main()
