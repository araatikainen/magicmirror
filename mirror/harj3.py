import numpy as np
from scipy.optimize import minimize

def target_function(x):
    x1, x2, x3 = x
    return x1+2*x2+3*x3

