from MC_Hazard_Rate import MCHazardRate
from ModelParameters import ModelParameters
from Calibration import cir_q

import numpy as np

n_steps_int = 20


# integral of Z(s) and dQ(s)
def int_z_dq(t1, t2, n_steps, zero_rate, mc):

    int_times = []
    dx = (t2-t1) / n_steps

    for i in range(n_steps):
        int_times.append(t1 + (i + 1) * dx)

    value = np.exp(- zero_rate * int_times[0]) * (mc.get_survival_probability(int_times[0]) -
                                                  mc.get_survival_probability(t1))

    for i in range(n_steps - 1):
        value += np.exp(- zero_rate * int_times[i + 1]) * \
                    (mc.get_survival_probability(int_times[i + 1]) -
                        mc.get_survival_probability(int_times[i]))

    return value


def default_leg(notional, zero_rate, recovery, maturity, mc):
    return - notional * (1-recovery) * int_z_dq(0, maturity, n_steps_int, zero_rate, mc)


def premium_leg(maturity, zero_rate, f, mc):
    # CDS fee is payable annually

    s = 0
    for i in range(maturity):
        s += np.exp(- zero_rate * (i + 1)) * mc.get_survival_probability((i + 1))

    return f*s
    # accrued interest
    # ac = 0
    #for k in range(maturity):
    #    ac += int_z_dq(k, k+1, n_steps_int, zero_rate, mc)

    # risky annuity
    # ra = s - ac
    # return f*ra


def cds_spread(maturity, zero_rate, recovery, mc):
    return default_leg(1, zero_rate, recovery, maturity, mc) / premium_leg(maturity, zero_rate, 1, mc)


if __name__ == "__main__":
    # zero_rate
    r = 0.01

    # maturity
    m = 7

    # recovery rate
    rcv = 0.5

    #lbd0 = 0.00425745
    #k_ = 0.08669852
    #theta_ = 0.01538081
    #sigma_ = 0.02847497

    lbd0 = 0.00104975
    k_ = 0.89655486
    theta_ = 0.02803922
    sigma_ = 0.09404974

    mp = ModelParameters(time=m,
                         n_steps=100,
                         lambda0=lbd0,
                         cir_k=k_,
                         cir_theta=theta_,
                         sigma=sigma_)

    hazard_rate_process = MCHazardRate(mp)

    n_runs = 1000
    sum_ = 0
    for j in range(n_runs):
        hazard_rate_process.update()
        sum_ += cds_spread(m, r, rcv,  hazard_rate_process)

    print(sum_/n_runs)


