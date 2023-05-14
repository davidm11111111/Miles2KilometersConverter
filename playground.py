def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add (3, 4, 5, 6, 7))

def calculate(n, **kwargs):
    print(kwargs)
    for key, value, in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(add=3, multiply=5)
