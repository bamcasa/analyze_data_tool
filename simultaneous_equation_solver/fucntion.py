import numpy as np

def function(x,a,*args):
    n = len(args)
    print(f"{n}차 함수")

    coefficients = list(args)
    coefficients.insert(0,a)

    print(coefficients)

    result = x * 0

    for i in range(n, -1, -1):
        result += coefficients[n-i] * x ** i

    return result
x = np.linspace(-10, 10, 100)
#x = 1
a = 1
b = 1
c = 1
d = 1
result = function(x,a,b,c)
