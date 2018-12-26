from math import exp


class BootstrapSpreadCurve(object):

    def __init__(self):
        self.surv_prob = dict()  # Map each t to a survival probability
        self.surv_prob[0] = 1

        self.points = dict()  # Map each t to a pair (par, time_intvl)
        self.zero_rate = 0.01  # flat zero_rate
        self.R = 0.5  # recovery rate

    def add_point(self, t, par, time_intvl):
        self.points[t] = (par, time_intvl)

    def get_surv_probs(self):
        self.__bootstrap_surv_probs__()
        return [self.surv_prob[t] for t in self.get_timepoints()]

    def get_timepoints(self):
        return sorted(self.points.keys())

    def __bootstrap_surv_probs__(self):
        for t in self.points.keys():
            point = self.points[t]
            self.surv_prob[t] = self.__calculate_surv_prob__(t, point)

    def __calculate_surv_prob__(self, t, point):

        (par, time_intvl) = point

        denominator = exp(-self.zero_rate * t) * (time_intvl * par + 1 - self.R)

        numerator = exp(-self.zero_rate * t)*(1-self.R) * self. surv_prob[t-time_intvl]

        for t0 in self.points.keys():
            if t0 < t:
                (par0, time_intvl0) = self.points[t0]
                numerator -= exp(-self.zero_rate * t0) * (self.surv_prob[t0]*time_intvl0*par -\
                                (1 - self.R) * (self.surv_prob[t0 - time_intvl0] - self.surv_prob[t0]))

        return numerator/denominator


if __name__ == "__main__":
    spread_curve = BootstrapSpreadCurve()

    #spread_curve.add_point(1, 0.001801, 1)
    #spread_curve.add_point(2, 0.002098, 1)
    #spread_curve.add_point(3, 0.002306, 1)
    #spread_curve.add_point(4, 0.003116, 1)
    #spread_curve.add_point(5, 0.003492, 1)
    #spread_curve.add_point(10, 0.003913, 5)

    #spread_curve.add_point(1, 0.005206, 1)
    #spread_curve.add_point(2, 0.007808, 1)
    #spread_curve.add_point(3, 0.007789, 1)
    #spread_curve.add_point(4, 0.010470, 1)
    #spread_curve.add_point(5, 0.011997, 1)
    #spread_curve.add_point(10, 0.012596, 5)

    #spread_curve.add_point(1, 0.024719, 1)
    #spread_curve.add_point(2, 0.023708, 1)
    #spread_curve.add_point(3, 0.022904, 1)
    #spread_curve.add_point(4, 0.021703, 1)
    #spread_curve.add_point(5, 0.019901, 1)
    #spread_curve.add_point(10, 0.014900, 5)

    spread_curve.add_point(1, 0.005932, 1)
    spread_curve.add_point(2, 0.007513, 1)
    spread_curve.add_point(3, 0.008300, 1)
    spread_curve.add_point(4, 0.010545, 1)
    spread_curve.add_point(5, 0.011600, 1)
    spread_curve.add_point(10, 0.012600, 5)

    y = spread_curve.get_surv_probs()
    # x = spread_curve.get_timepoints()

    # print(x)
    print(y)

    # import matplotlib.pyplot as plt

    # plt.plot(x, y)
    # plt.title("Default Curve")
    # plt.ylabel("Survival Probability")
    # plt.xlabel("t")
    # plt.show()

