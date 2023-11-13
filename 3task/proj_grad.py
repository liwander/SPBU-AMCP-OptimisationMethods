import numpy as np
from common import *

def proj(g):
    """Projection of x onto the feasible set defined by c"""
    r = (np.dot(g, constraintFunctionSlope) / np.linalg.norm(constraintFunctionSlope) ** 2) * constraintFunctionSlope
    return r

def proj_grad(f, grad_f, x0, max_iter=1000, tol=1e-3):
    """Projected gradient method for constrained optimization"""
    x = x0
    # alpha = 2 / (i + 2)
    alpha = 1e-1
    for i in range(max_iter):
        # Compute gradient
        g = grad_f(x)
        # Update x
        x = proj(x - alpha * g)
        # Check convergence
        if np.linalg.norm(g) < tol:
            break
        # Update x and iteration counter
    return x

def PG():
    return proj_grad(objectFunction,
                      objectFunctionGradient,
                      np.array([cf - 1, 1]))
        