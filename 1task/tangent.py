import general as g

def tangent(f, a, b):
    k = 0
    rp_memed = False
    f_a = f(a)
    ka = g.deriv(a)
    f_b = f(b)
    kb = g.deriv(b)

    while not (b - a < g.acc((a + b) / 2)):
        k += 1

        c = (ka * a - kb * b - f_a + f_b) / (ka - kb)
        kc = g.deriv(c)
        f_c = f(c)
   
        print(f"iter: {k}  a:{float.hex(a)}  f(a): {float.hex(f_a)}  f'(a): {float.hex(ka)}  b: {float.hex(b)}  f(b): {float.hex(f_b)}   f'(b) {float.hex(kb)}")
        
        if (kc > 0):
            b = c
            f_b = f_c
            kb = kc
            rp_memed = False
            print(" b = c ", end=' ')
        elif kc < 0:
            a = c
            f_a = f_c
            ka = kc
            rp_memed = True
            print(" a = c ", end=' ')
        else:
            a, b = c, c
            break

        print(f'eps: {float.hex(max(c - a, b - c))}  c: {float.hex(c)}  f(c): {float.hex(f_c)}  f\'(c): {float.hex(kc)}', end=' ')
        print(f'f(x)_calls: {g.count0}\t f\'(x) calls: {g.count1}\n')

        
    return g.count0, (a + b) / 2, f((a + b) / 2)
