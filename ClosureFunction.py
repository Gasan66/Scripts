def f():

    x = 1

    def inc():
        nonlocal x
        x += 1
        print(x)
    return inc


a = f()

a()
a()
a()
