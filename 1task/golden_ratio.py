import math
from general import acc


def golden_ratio(f, a, b, eps=1e-3):
    ratio_for_d = (math.sqrt(5) - 1) / 2
    ratio_for_c = (3 - math.sqrt(5)) / 2

    rp_cached = True
    d = a + (b - a) * ratio_for_d
    f_d = f(d)
    c = a + (b - a) * ratio_for_c
    f_c = f(c)

    k = 0

    print("iter   a    c    d    b    f(c)    f(d)")
    while not (abs((b - a) / 2) < acc( (a + b) / 2)):
        k += 1
        from general import count


        if (rp_cached):
            c = a + (b - a) * (ratio_for_c)
            f_c = f(c)
        else:
            d = a + (b - a) * ratio_for_d
            f_d = f(d)

        
        print("{}, {}, {}, {}, {}".format(
            k, float.hex(a), float.hex(c), float.hex(d),
            float.hex(b)),
              end='   ')
        print("{}    {}".format(float.hex(f_c), float.hex(f_d)), count)
        print(f"{float.hex(d -a)}   {float.hex(math.pi)}  {float.hex(f_c - f_d)}")    

        if f_c < f_d:
            b = d
            d = c
            f_d = f_c
            rp_cached = True
        else:
            a = c
            c = d
            f_c = f_d
            rp_cached = False



    return count, (a + b) / 2, f((a + b) / 2)
