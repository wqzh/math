
from math import gamma as Gamma
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01,30,0.01,)

def Chi2(n, x):
    c = 1 / Gamma(n/2.) / np.power(2., n/2.)
    return c * np.power(x, n/2-1)*np.exp(-x/2)

#N = [ 2, 3,4, 6, 9 ]  #plt.ylim(0, 0.5)
#N = [ 1, 4, 10, 20 ] #plt.ylim(0, 0.3)
N = [1,2,4,6,11]

plt.figure(dpi=350)
for n in N: #N, range(1,10)
    plt.plot(x, Chi2(n, x), label=fr'$n={n}$')
plt.ylim(0, 0.5)
plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()
plt.title('$\chi^2$ Distribution')
plt.savefig('./figs/Chi2.pdf')
print(sum(Chi2(4, x))*0.01)
