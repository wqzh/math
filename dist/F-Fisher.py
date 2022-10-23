
from math import gamma as Gamma
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01,5,0.01,)

def Fisher(n1, n2, x):
    c = Gamma((n1+n2)/2) / Gamma(n1/2) / Gamma(n2/2) 
    c = c *  np.power(n1, n1/2) *  np.power(n2, n2/2)
    return c * np.power(x, n1/2-1)*np.power(n1*x+n2, -(n1+n2)/2)

N1 = [4, 10, 10, 4]
N2 = [4, 4, 10, 10]

plt.figure(dpi=350)
for n1,n2 in zip(N1, N2):
    plt.plot(x, Fisher(n1, n2, x), label=fr'$n_1={n1}, n_2={n2}$')
#plt.ylim(0, 0.5)
plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()
plt.title('F-Distribution')
plt.savefig('./figs/Fisher.pdf')
print(sum(Fisher(4, 4, x))*0.01)
