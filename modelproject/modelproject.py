from scipy.optimize import minimize_scalar
import numpy as np



def maximize(g, a, b, args):
    """
    Maximize the function `g` over the interval [a, b].
    
    This function converts the maximization problem into a minimization problem
    by negating the function `g`, which allows us to use the `minimize_scalar` method.
    The `args` parameter passes additional arguments to the function `g`.
    
    Parameters:
        g (function): The function to maximize.
        a, b (float): The lower and upper bounds of the interval for maximization.
        args (tuple): Additional arguments to pass to the function `g`.

    Returns:
        tuple: The maximizer (where the maximum occurs) and the maximum value of `g`.
    """
    # Define the objective function as the negative of `g` for minimization
    objective = lambda x: -g(x, *args)
    # Perform bounded minimization to find the maximizer
    result = minimize_scalar(objective, bounds=(a, b), method='bounded')
    maximizer, maximum = result.x, -result.fun  # Reverse negation to get max value
    return maximizer, maximum




class CakeEating:
    """
    A class representing the dynamic problem of cake eating where an agent decides
    how much cake to consume over time to maximize utility given preferences and
    resource constraints.
    
    Parameters:
        beta (float): Discount factor reflecting time preference.
        n (float): Population growth rate, affecting resource dilution.
        alpha (float): Elasticity parameter influencing production.
        k_grid_min (float): Minimum capital in the grid.
        k_grid_max (float): Maximum capital in the grid.
        k_grid_size (int): Number of points in the capital grid.
    """
    def __init__(self, beta=0.9, n=0.05, alpha=1, k_grid_min=1e-3, k_grid_max=20.0, k_grid_size=150):
        self.beta, self.n, self.alpha = beta, n, alpha
        # Set up the grid for capital values
        self.k_grid = np.linspace(k_grid_min, k_grid_max, k_grid_size)

    def u(self, c):
        """Utility function with logarithmic utility of consumption."""
        return np.log(c)

    def u_prime(self, c):
        """Derivative of the utility function, representing marginal utility of consumption."""
        return 1 / c

    def state_action_value(self, c, k, v_array):
        """
        Calculate the right-hand side of the Bellman equation for a given state `k` and action `c`.
        
        This represents the value of taking action `c` (consuming `c` units of cake) while having
        `k` units of capital, based on the future value function represented by `v_array`.
        
        Parameters:
            c (float): Consumption level.
            k (float): Current capital.
            v_array (np.array): Array representing the value function for different capital levels.

        Returns:
            float: Value of taking action `c` at state `k`.
        """
        u, beta, n, alpha = self.u, self.beta, self.n, self.alpha
        # Function to interpolate the next value from the value function
        v = lambda k: np.interp(k, self.k_grid, v_array)
        # Next period's capital after consumption and population growth
        k_next = (k**alpha - c) / (1 + n)
        return u(c) + beta * (1 + n) * v(k_next)



def T(v, ce):
    """
    Bellman operator function that updates the value function based on an initial guess.

    It computes the value function for each state by finding the optimal consumption that
    maximizes the state-action value.

    Parameters:
        v (np.array): Current estimate of the value function.
        ce (CakeEating): An instance of the CakeEating class.
    
    Returns:
        np.array: Updated value function after applying the Bellman operator.
    """
    v_new = np.empty_like(v)
    for i, k in enumerate(ce.k_grid):
        """
        Here, maximize is called to find the optimal consumption for a given capital 
        level k and its value. The second argument 1e-10 is the lower bound of the interval 
        for maximization, and k is the current capital level. Since the upper bound is not 
        explicitly specified here, the optimization is essentially unbounded in the upper direction.
        """
        v_new[i] = maximize(ce.state_action_value, 1e-10, k, (k, v))[1]
    return v_new



def compute_value_and_policy(ce, tol=1e-4, max_iter=1000, verbose=True, print_skip=1):
    """
    Computes the value function and consumption policy for the CakeEating problem using iteration.

    Parameters:
        ce (CakeEating): An instance of the CakeEating class.
        tol (float): Tolerance level for convergence.
        max_iter (int): Maximum number of iterations.
        verbose (bool): If True, print debug information.
        print_skip (int): Number of iterations to skip between debug prints.

    Returns:
        tuple: The converged value function and corresponding consumption policy.
    """
    # Start with the initial guess for the value function
    v = ce.u(ce.k_grid)
    i = 0
    error = tol + 1
    policy = np.zeros_like(ce.k_grid)

    while i < max_iter and error > tol:
        v_new = T(v, ce)
        error = np.max(np.abs(v - v_new))
        i += 1
        if verbose and i % print_skip == 0:
            print(f"Error at iteration {i} is {error}.")
        v = v_new

    if error > tol:
        print("Failed to converge!")
    elif verbose:
        print(f"\nConverged in {i} iterations.")

    # Calculate the consumption policy once convergence is achieved
    for j, k in enumerate(ce.k_grid):
        c = maximize(ce.state_action_value, 1e-10, k, (k, v))[0]
        policy[j] = c

    return v_new, policy
