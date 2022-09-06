import numpy as np

def logistic_map(x,r):
    log_m =r*x *(1-x)
    return log_m

def iterate_f(it, xi, r):
    """
    takes a number of iterations `it`, a starting value,
    and a parameter value for r. It should execute f repeatedly (it times), each
    time using the last result of f as the new input to f. Append each iteration's
    result to a list l. Finally, convert the list into a numpy array and return it.
    """
    x = xi
    l = []
    for _ in range(it):
        x = logistic_map(x, r)
        l.append(x)

    return np.array(l)
