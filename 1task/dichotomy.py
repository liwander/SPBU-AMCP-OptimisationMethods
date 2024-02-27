from general import acc
from pandas import DataFrame as df
from general import hex

def dichotomy(f, a, b, eps=1e-6):
    header_row = ['iteration', 'a', 'c', 'd', 'b', 'delta', 'f(c)', 'f(d)', 'calls']
    print_table_rows = []
    k = 0
    while not (abs((b - a) / 2) < acc((a + b)/ 2)):
        k += 1
        delta = (b - a) / 16
        c = (a + b - delta) / 2
        d = (a + b + delta) / 2

        table_row = [k, hex(a), hex(c), hex(d), hex(b), hex(delta)]

        f_c, f_d = f(c), f(d)
        if f_c <= f_d:
            b = d
        else:
            a = c

        table_row += [hex(f_c), hex(f_d), f.callsNumber]
        print_table_rows.append(table_row)


    x = df(data=print_table_rows, columns=header_row)
    x.to_markdown('dichotomy_output.md', index=False)
    # x.to_csv('./output.csv')
    # print(tabulate(df, headers=header_row, tablefmt='psql'))
    return f.callsNumber, (a + b) / 2, f((a + b) / 2)



