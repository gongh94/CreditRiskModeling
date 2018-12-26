import numpy
import math
import numpy.random as nrand

"This py uses Model Parameters class"


def brownian_motion(param):
    sqrt_delta_sigma = math.sqrt(param.delta_t) * param.sigma
    return nrand.normal(loc=0, scale=sqrt_delta_sigma, size=param.n_steps)


def cox_ingersoll_ross_levels(param):

    bm = brownian_motion(param)
    # Setup the parameters for interest rates
    k, theta, zero = param.cir_k, param.cir_theta, param.lambda0
    # Assumes output is in levels
    levels = [zero]

    for i in range(1, param.n_steps):
        drift = k * (theta - levels[i-1]) * param.delta_t
        randomness = math.sqrt(levels[i - 1]) * bm[i - 1]
        levels.append(levels[i - 1] + drift + randomness)

    return numpy.array(levels)

