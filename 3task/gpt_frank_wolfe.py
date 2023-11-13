import numpy as np
from collections.abc import Callable
from common import constraintFunctionGradient, objectFunctionGradient, objectFunction, cf

vector = np.array


def frank_wolfe(obj_func: Callable[[vector], float],
                grad_func: Callable[[vector], vector],
                feasible_set: Callable[[vector], vector],
                init_point: vector,
                max_iter: int = 1000,
                tol: float = 1e-6
                ) -> vector:
    """
    Solves a constrained convex optimization problem using the Frank-Wolfe algorithm.

    Parameters:
        obj_func (callable): The objective function to minimize.
        grad_func (callable): The gradient of the objective function.
        feasible_set (callable): A function that returns the feasible set given a point.
        init_point (ndarray): The initial feasible point.
        max_iter (int): The maximum number of iterations to run.
        tol (float): The tolerance for stopping criteria.

    Returns:
        ndarray: The optimal solution.
    """
    x = init_point
    for k in range(max_iter):
        g = grad_func(x)
        v = feasible_set(x)
        t = minimize_linear_approx(obj_func, g, v)
        x_new = x + t * (v - x)
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x


def minimize_linear_approx(obj_func, g, feasible_set):
    """
    Finds the optimal step size that minimizes the linear approximation of the objective function.

    Parameters:
        obj_func (callable): The objective function to minimize.
        g (ndarray): The gradient of the objective function at the current point.
        feasible_set (ndarray): The feasible set at the current point.

    Returns:
        float: The optimal step size.
    """
    v = feasible_set
    inner_prod = np.dot(g, v)
    t = np.min([1.0, -obj_func(v) / inner_prod])
    return t

def feasible_set(x : vector):
    return (np.dot(x, constraintFunctionGradient) / np.linalg.norm(constraintFunctionGradient) ** 2) * constraintFunctionGradient 


def projGD():
    return frank_wolfe(objectFunction,
                      objectFunctionGradient,
                      feasible_set,
                      np.array([cf - 1, 1]))