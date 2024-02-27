import math
from pandas import DataFrame as df
from general import acc, hex


def golden_ratio(f, a, b, eps=1e-3):
    header_row = ['iteration', 'a', 'c', 'd', 'b', 'f(c)', 'f(d)', 'calls']
    print_table_rows = []

    ratio_for_d = (math.sqrt(5) - 1) / 2
    ratio_for_c = (3 - math.sqrt(5)) / 2

    rp_cached = True
    d = a + (b - a) * ratio_for_d
    f_d = f(d)
    c = a + (b - a) * ratio_for_c
    f_c = f(c)

    k = 0

    # print("iter   a    c    d    b    f(c)    f(d)")/
    while not (abs((b - a) / 2) < acc( (a + b) / 2)):
        k += 1

        if (rp_cached):
            c = a + (b - a) * (ratio_for_c)
            f_c = f(c)
        else:
            d = a + (b - a) * ratio_for_d
            f_d = f(d)

        
        # print("{}, {}, {}, {}, {}".format(k, float.hex(a), float.hex(c), float.hex(d),float.hex(b)),end='   ')
            
        row = [k, hex(a), hex(c), hex(d), hex(b)]
        row += [hex(f_c), hex(f_d), f.callsNumber]

        # print("{}    {}".format(float.hex(f_c), float.hex(f_d)), f.callsNumber)
        # print(f"{float.hex(d -a)}   {float.hex(math.pi)}  {float.hex(f_c - f_d)}")    

        print_table_rows.append(row)

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


    x = df(data=print_table_rows, columns=header_row)
    x.to_markdown('gold_ration_output.md', index=False)
    return f.callsNumber, (a + b) / 2, f((a + b) / 2)
