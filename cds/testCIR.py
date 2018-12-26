from Calibration import cir_q


tenor = [1, 2, 3, 4, 5, 10]
lbd0 = 3.55546e-04
k_ = 6.72349e-01
theta_ = 9.18901e-03
sigma_ = 4.34672e-02

for tt in tenor:
    print(cir_q(tt, lbd0, k_, theta_, sigma_))



#paths = 100
#cir_examples = []
#cir_levels = cox_ingersoll_ross_levels(mp)
#for i in range(paths):
#    cir_examples.append(cox_ingersoll_ross_levels(mp))

#plot_stochastic_processes(cir_examples, "Cox Ingersoll Ross")