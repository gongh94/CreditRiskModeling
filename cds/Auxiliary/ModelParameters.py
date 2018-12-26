import numpy as np


class ModelParameters:

    def __init__(self, time, n_steps, lambda0=0.0,
                 cir_k=0.0, cir_theta=0.0, sigma=0.0):

        # This is the amount of time to simulate for
        # In unit of years
        self.time = time

        self.n_steps = n_steps

        # This is the starting interest rate value
        self.lambda0 = lambda0

        # This is the annual drift factor for geometric brownian motion
        self.cir_k = cir_k

        # This is the long run average interest rate for Cox Ingersoll Ross
        self.cir_theta = cir_theta

        # This is the ANNUAL volatility of the stochastic processes
        self.sigma = sigma/np.sqrt(np.floor(n_steps/time))

        self.delta_t = time/n_steps
