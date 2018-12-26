from math import *
import numpy as np
from scipy.optimize import minimize

# expected Q of CIR model solved from Feynman-Kac PDE
def cir_q(t, lambda0, k, theta, sigma):

    xi = sqrt(k*k + 2*sigma*sigma)

    a = pow(2*xi*exp((xi+k)*t/2) / ((xi+k)*(exp(xi*t)-1) + 2*xi), 2*k*theta/(sigma*sigma))

    b = 2*(exp(xi*t)-1)/((xi+k)*(exp(xi*t)-1)+2*xi)

    q = a*exp(-b*lambda0)

    return q

# print(cir_Q(7, 0.02, 0.1, 0.05, 0.13))


# param = (lambda0, k, theta, sigma)
def error(param):

    tenor = [1, 2, 3, 4, 5, 10]
    target = np.array([0.988275104164196, 0.9705355057482422, 0.9516088539142633, 0.9188954547397059, 0.8899609903605353, 0.7813780925229601])
    values = []

    for t in tenor:
        values.append(cir_q(t, param[0], param[1], param[2], param[3]))

    np.asarray(values)

    return np.sum(np.square(values - target))


if __name__ == "__main__":
    initial = np.array([0.074, 0.067, 0.05, 0.0013])

    res = minimize(error, initial, method="Nelder-Mead", options={'xtol': 1e-5, 'disp': True})
    print(res.x)

    # 2*k*theta > sigma^2 has to be satisfied
    if 2 * res.x[1] * res.x[2] - res.x[3] * res.x[3] > 0:
        print("good: 2*k*theta > sigma^2")
    else:
        print("not good: 2*k*theta <= sigma^2")