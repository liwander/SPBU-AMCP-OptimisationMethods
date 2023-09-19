from general import acc


def dichotomy(f, a, b, eps=1e-6):
    k = 0
    print("iter\ta\tc  d    b  delta f(c)  f(d)  трудоемкость")
    while not (abs((b - a) / 2) < acc((a + b)/ 2)):
        from general import count
        k += 1
        delta = (b - a) / 16
        c = (a + b - delta) / 2
        d = (a + b + delta) / 2

        print("{}, {:.8}, {:.8}, {:.8}, {:.8}  {}    ".format(k, float.hex(a), float.hex(c), float.hex(d), float.hex(b), float.hex(delta)), end='  ')

        f_c, f_d = f(c), f(d)
        if f_c <= f_d:
            b = d
        else:
            a = c
        print("{:.9}, {:.9}  {}".format(float.hex(f_c), float.hex(f_d), count))

    return count, (a + b) / 2, f((a + b) / 2)



