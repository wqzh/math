
from math import gamma as Gamma
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1,0.01,)

def Beta(alpha, beta, x):
    c = Gamma(alpha+beta)/(Gamma(alpha) * Gamma(beta))
    return c * np.power(x, alpha-1)*np.power(1-x, beta-1)

alpha = [.5, 5, 1, 2, 2, 8]
beta = [.5, 1, 3, 2, 5, 8]

plt.figure(figsize=(5,5), dpi=350)#figsize=(5,5),
for a,b in zip(alpha, beta):
    plt.plot(x, Beta(a,b,x), 
              label=fr'$\alpha={a}, \beta={b}$')
plt.ylim(0, 3.5)
plt.xlim(0, 1.)
plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()
plt.title('Beta Distribution')
plt.savefig('./figs/Beta.pdf')