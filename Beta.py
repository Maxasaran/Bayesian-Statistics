import numpy as np
from scipy.stats import beta
from scipy import integrate

x = 0.5 # probability
a = 0.45 # low bound
b = 0.55 # upper bound


def beta_pdf(x):
    result = beta.pdf(x, 9, 11)
    return result
	
Density_of_prob = integrate.quad(beta_pdf, a ,b)

print(Density_of_prob)