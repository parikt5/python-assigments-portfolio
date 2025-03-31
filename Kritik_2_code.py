

# +
import numpy as np
def roots (f, a, b, tol = 1e-10):

    if np.sign(f(a))==np.sign(f(b)):
        return None

    for i in range(1000):
        mid =(a+b)/2


        if np.abs(f(mid))<tol:
            return mid
        elif np.sign(f(a)) == np.sign(f(mid)):
            return roots(f, mid, b, tol)

        else:
            return roots(f, a, mid, tol)

test_cases = [
    (lambda x:np.exp(x)+ np.log(x), 0.1, 1),
    (lambda x:np.arctan(x) - x**2, 0, 2),
    (lambda x:np.sin(x) /np.log(x), 3, 4),
    (lambda x:np.log(np.cos(x)), 5, 7),
]
for i, (f, a, b) in enumerate(test_cases):

    r1=roots(f,a,b)

    if r1 is not None:
        print (f"Root of function bet [{a}, {b}]={r1:.10f}")
# -








