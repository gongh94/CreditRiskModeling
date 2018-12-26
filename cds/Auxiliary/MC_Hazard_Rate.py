from CoxIngersollRoss import *
import numpy as np


class MCHazardRate:

    def __init__(self, mp):
        self.mp = mp
        self.cir_levels = cox_ingersoll_ross_levels(mp)

    def get_hazard_rate(self, t):
            return self.cir_levels[np.floor(t / self.mp.time * self.mp.n_steps)]

    def get_survival_probability(self, t):
        idx = np.floor(t / self.mp.time * self.mp.n_steps)

        s = 0
        for i in range(self.mp.n_steps):
            if i <= idx:
                s += self.cir_levels[i] * self.mp.delta_t
        return np.exp(-s)

    def update(self):
        self.cir_levels = cox_ingersoll_ross_levels(self.mp)
