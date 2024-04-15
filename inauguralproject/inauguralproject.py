# Importing packacges

from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# DEFINING PARAMETERS
alpha = 1/3
beta = 2/3
N = 75
p1_values = np.linspace(0.5, 2.5, N)


# DEFINING UTILITY FUNCTIONS

# CONSUMER A
def utility_A(x1, x2, alpha):
    return x1**alpha * x2**(1 - alpha)
# COMSUMBER B
def utility_B(x1, x2, beta):
    return x1**beta * x2**(1 - beta)




# DEFINING DEMAND FUNCTIONS
def demand_A_x1(p1, omega_A1, omega_A2, alpha):
    return alpha * (p1 * omega_A1 + omega_A2) / p1

def demand_A_x2(p1, omega_A1, omega_A2, alpha):
    return (1 - alpha) * (p1 * omega_A1 + omega_A2)

def demand_B_x1(p1, omega_B1, omega_B2, beta):
    return beta * (p1 * omega_B1 + omega_B2) / p1

def demand_B_x2(p1, omega_B1, omega_B2, beta):
    return (1 - beta) * (p1 * omega_B1 + omega_B2)





# DEFINING market clearing conditions
def market_clearing_condition_x1(p1):
    # Total demand for good 1 should equal total endowment of good 1
    total_demand_x1 = demand_A_x1(p1, omega_A1, omega_A2, alpha) + demand_B_x1(p1, omega_B1, omega_B2, beta)
    total_endowment_x1 = omega_A1 + omega_B1
    return total_demand_x1 - total_endowment_x1

def market_clearing_condition_x2(p1):
    # Total demand for good 2 should equal total endowment of good 2
    total_demand_x2 = demand_A_x2(p1, omega_A1, omega_A2, alpha) + demand_B_x2(p1, omega_B1, omega_B2, beta)
    total_endowment_x2 = omega_A2 + omega_B2
    return total_demand_x2 - total_endowment_x2


# DEFINING FUNCTION TO DETERMINE ALLOCATION AT GIVEN PRICE
def allocation_at_price(p1, alpha, omega_A1, omega_A2):
    allocation_x1 = alpha * (p1 * omega_A1 + omega_A2) / p1
    allocation_x2 = (1 - alpha) * (p1 * omega_A1 + omega_A2)
    return allocation_x1, allocation_x2