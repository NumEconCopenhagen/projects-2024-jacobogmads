# Utility Functions
def uA(x1, x2, alpha=alpha):
    return (x1 ** alpha) * (x2 ** (1 - alpha))

def uB(x1, x2, beta=beta):
    return ((1-x1) ** beta) * ((1-x2) ** (1 - beta))

#Initial utilities 
initial_uA = uA(omega_A1, omega_A2)
initial_uB = uB(omega_B1, omega_B2)
