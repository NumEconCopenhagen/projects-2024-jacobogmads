import numpy as np
from types import SimpleNamespace
import matplotlib.pyplot as plt

class Parameters:
    def __init__(self):
        self.A = 1.0
        self.gamma = 0.5
        self.alpha = 0.3
        self.nu = 1.0
        self.epsilon = 2.0
        self.tau = 0.0
        self.T = 0.0
        self.w = 1.0

class Firm:
    def __init__(self, params):
        self.A = params.A
        self.gamma = params.gamma

    def labor_demand(self, w, p):
        return (p * self.A * self.gamma / w) ** (1 / (1 - self.gamma))

    def output(self, w, p):
        ell = self.labor_demand(w, p)
        return self.A * ell ** self.gamma

    def profit(self, w, p):
        ell = self.labor_demand(w, p)
        return (1 - self.gamma) / self.gamma * w * ell

class Consumer:
    def __init__(self, params):
        self.alpha = params.alpha
        self.nu = params.nu
        self.epsilon = params.epsilon

    def consumption_1(self, ell, w, T, p1, p2, tau, pi1, pi2):
        return self.alpha * (w * ell + T + pi1 + pi2) / p1

    def consumption_2(self, ell, w, T, p1, p2, tau, pi1, pi2):
        return (1 - self.alpha) * (w * ell + T + pi1 + pi2) / (p2 + tau)

    def utility(self, ell, w, T, p1, p2, tau, pi1, pi2):
        c1 = self.consumption_1(ell, w, T, p1, p2, tau, pi1, pi2)
        c2 = self.consumption_2(ell, w, T, p1, p2, tau, pi1, pi2)
        return np.log(c1 ** self.alpha * c2 ** (1 - self.alpha)) - self.nu * ell ** (1 + self.epsilon) / (1 + self.epsilon)

    def optimal_labor_supply(self, w, T, p1, p2, tau, pi1, pi2):
        ell_guess = 1.0
        result = minimize(lambda ell: -self.utility(ell, w, T, p1, p2, tau, pi1, pi2), ell_guess)
        return result.x[0]

def market_clearing_conditions(params):
    firm1 = Firm(params)
    firm2 = Firm(params)
    consumer = Consumer(params)
    
    p1_range = np.linspace(0.1, 2.0, 10)
    p2_range = np.linspace(0.1, 2.0, 10)
    
    market_clearing = []
    
    for p1 in p1_range:
        for p2 in p2_range:
            pi1 = firm1.profit(params.w, p1)
            pi2 = firm2.profit(params.w, p2)
            
            ell_star = consumer.optimal_labor_supply(params.w, params.T, p1, p2, params.tau, pi1, pi2)
            
            c1_star = consumer.consumption_1(ell_star, params.w, params.T, p1, p2, params.tau, pi1, pi2)
            c2_star = consumer.consumption_2(ell_star, params.w, params.T, p1, p2, params.tau, pi1, pi2)
            
            y1_star = firm1.output(params.w, p1)
            y2_star = firm2.output(params.w, p2)
            
            ell1_star = firm1.labor_demand(params.w, p1)
            ell2_star = firm2.labor_demand(params.w, p2)
            
            labor_market_clearing = np.isclose(ell_star, ell1_star + ell2_star)
            goods_market_1_clearing = np.isclose(c1_star, y1_star)
            goods_market_2_clearing = np.isclose(c2_star, y2_star)
            
            market_clearing.append((p1, p2, labor_market_clearing, goods_market_1_clearing, goods_market_2_clearing))
    
    return market_clearing

def print_market_clearing_conditions(market_clearing):
    for condition in market_clearing:
        p1, p2, labor_market, goods_market_1, goods_market_2 = condition
        print(f"p1: {p1}, p2: {p2} | Labor Market: {labor_market}, Goods Market 1: {goods_market_1}, Goods Market 2: {goods_market_2}")

# Parameters
params = Parameters()

# Check market clearing conditions
market_clearing = market_clearing_conditions(params)
print_market_clearing_conditions(market_clearing)