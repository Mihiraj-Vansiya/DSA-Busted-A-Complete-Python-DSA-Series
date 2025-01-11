import sys

def main():
    print('Namaste Duniya')

    a = 123
    print(a,type(a))

    a1 = 'v'
    print(a1,type(a1))

    bl = True
    print(bl,type(bl))

    f = 2.1
    print(f,type(f))

    d = 1.232
    print(d,type(d))

    print(f"size of a is {sys.getsizeof(a)}")
    print(f"size of char a1 is {sys.getsizeof(a1)}")
    print(f"size of bool bl is {sys.getsizeof(bl)}")
    print(f"size of float f is {sys.getsizeof(f)}")
    print(f"size of d is {sys.getsizeof(d)}")

    a2 = ord('a')
    print(a2)

    a3 = ord('b')
    print(a3)

    al = ord('z')
    print(al)

    ch = chr(98)
    print(ch)

    ch2 = chr(120)
    print(ch2)

    a6 = -112
    print(a6)

    # Operaters
    a7 = 2
    print(a7 / 5)

    a8 = 2.0
    print(a8 / 5)

    a9 = 4
    print(a9 / 6)

    # RELATION OPERATERS
    ax = 2
    bx = 3

    print(ax == bx)
    print(ax != bx)
    print(ax <= bx)
    print(ax >= bx)
    print(ax < bx)
    print(ax > bx)

    # LOGICAL OPERATERS
    ax1 = 23
    print(not ax1)

    ax2 = 0
    print(not ax2)

if __name__ == '__main__':
    main()