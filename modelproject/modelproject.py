from scipy import optimize
from scipy.optimize import minimize_scalar, bisect
import numpy as np

def maximize(g, a, b, args):
    """
    Maximize the function g over the interval [a, b].

    We use the fact that the maximizer of g on any interval is
    also the minimizer of -g.  The tuple args collects any extra
    arguments to g.

    Returns the maximal value and the maximizer.
    """

    objective = lambda x: -g(x, *args)
    result = minimize_scalar(objective, bounds=(a, b), method='bounded')
    maximizer, maximum = result.x, -result.fun
    return maximizer, maximum




class CakeEating:

    def __init__(self, beta=0.9, n=0.05, alpha=0.33, k_grid_min=1e-3, k_grid_max=6.0, k_grid_size=150):
        self.beta, self.n, self.alpha = beta, n, alpha

        # Set up grid
        self.k_grid = np.linspace(k_grid_min, k_grid_max, k_grid_size)

    # Utility function: Log utility
    def u(self, c):
        return np.log(c)

    # The derivative of the utility function
    def u_prime(self, c):
        return 1 / c

    # The state-action value function
    def state_action_value(self, c, k, v_array):
        """
        Right hand side of the Bellman equation given capital k and consumption c.
        """

        u, beta, n, alpha = self.u, self.beta, self.n, self.alpha
        v = lambda k: np.interp(k, self.k_grid, v_array)

        k_next = (k**alpha - c) / (1 + n)  # Calculating next period's capital
        return u(c) + beta * (1 + n) * v(k_next)
        




def T(v, ce):
    """
    The Bellman operator.  Updates the guess of the value function.

    * ce is an instance of CakeEating
    * v is an array representing a guess of the value function

    """
    v_new = np.empty_like(v)

    for i, k in enumerate(ce.k_grid):
        # Maximize RHS of Bellman equation at state k
        v_new[i] = maximize(ce.state_action_value, 1e-10, k, (k, v))[1]

    return v_new


