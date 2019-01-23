def plus():
    plus = '+'
    return plus


def minus(args, ):
    minus = ' - ' * args
    return minus


def vert_dash(args, ):
    vert_dash = '|' + ' ' * args + ' | ' + ' ' * args + '|'
    return vert_dash


def print_grid(v, m):
    print(plus() + minus(1) + plus() + minus(1) + plus())
    print(vert_dash(2))
    print(plus() + minus(1) + plus() + minus(1) + plus())
    print(vert_dash(2))
    print(plus() + minus(1) + plus() + minus(1) + plus())




print_grid(2,1)

