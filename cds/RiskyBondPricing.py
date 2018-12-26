from ModelParameters import ModelParameters
from MC_Hazard_Rate import MCHazardRate
import numpy as np
# risky bonds with zero recovery


def risky_bond_price(coupon_rate, notional, maturity, zero_rate, mc):

    s = 0

    for i in range(maturity):
        s += coupon_rate * notional * np.exp(- zero_rate * (i+1)) * mc.get_survival_probability((i+1))
    s += notional * np.exp(- zero_rate * maturity) * mc.get_survival_probability(maturity)
    return s


if __name__ == "__main__":
    zero_rate = 0.01
    maturity = 8
    coupon_rate = 0.05

    #lbd0 = 0.00425745
    #k_ = 0.08669852
    #theta_ = 0.01538081
    #sigma_ = 0.02847497

    lbd0 = 0.00104975
    k_ = 0.89655486
    theta_ = 0.02803922
    sigma_ = 0.09404974

    mp = ModelParameters(time=maturity,
                         n_steps=100,
                         lambda0=lbd0,
                         cir_k=k_,
                         cir_theta=theta_,
                         sigma=sigma_)

    hazard_rate_process = MCHazardRate(mp)

    sum_ = 0
    n_runs = 1000

    for i in range(n_runs):
        hazard_rate_process.update()
        sum_ += risky_bond_price(coupon_rate, 100, maturity, zero_rate, hazard_rate_process)

    print(sum_/n_runs)

