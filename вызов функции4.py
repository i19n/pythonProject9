def fun(x):
    if x<0:
        return x*2
    else:
        return x*3
def main():
    for i in range(-3,4):
        y=fun(i)
        print('fun(', i, ')=', y, sep='')
main()