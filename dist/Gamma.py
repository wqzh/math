
from math import gamma as Gamma
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01,20,0.01,)

def Ga(alpha, beta, x):
    c = np.power(beta, alpha) / Gamma(alpha)
    return c * np.power(x, alpha-1)*np.exp(-beta*x)

alpha = [1, 2, 3, 5, 9, 6]
beta = [2, 2, 2, 1, 0.5, 1]

# alpha = [0.5, 1, 2, 2, 2]
# beta = [0.5, 0.5, 0.5, 1, 2,]

### bata
plt.figure(dpi=350)
for a,b in zip(alpha, beta):
    plt.plot(x, Ga(a,b,x), label=fr'$\alpha={a}, \beta={b}$')
plt.legend()
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('$\Gamma$-Distribution')
plt.savefig('./figs/Gamma.pdf')

### inverse beta
plt.figure(dpi=350)
for a,b in zip(alpha, beta):
    plt.plot(x, Ga(a,1/b,x), label=fr'$\alpha$={a}, '+r'$\beta^{-1}$'+f'={b}')
plt.legend()
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('$\Gamma$-Distribution')
plt.savefig('./figs/Gamma_inv_beta.pdf')




### use scipy pdf
# import scipy.stats as st
# plt.figure(dpi=350)
# for a,b in zip(alpha, beta):
#     plt.plot(x, st.gamma.pdf(x, a, scale=b), 
#               label=fr'$\alpha={a}, \beta={b}$')
# plt.legend()

### test 
# import scipy.stats as st
# for a,b in zip(alpha, beta):
#     print(sum(st.gamma.pdf(x, a, scale=b))*0.01)
#     print(sum(Ga(a,b,x))*0.01)
