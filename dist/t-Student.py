
from math import gamma as Gamma
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.01,)

def Student(n, x):
    c = Gamma((n+1)/2) / Gamma(n/2) / np.sqrt(n*np.pi)
    return c * np.power(1+x**2/n, -(n+1)/2)

N = [1,2,3,4,5,6] # 1, 2, 3,4, 6, 9 

plt.figure(dpi=350)
for n in N:
    plt.plot(x, Student(n, x), label=fr'$n={n}$')
#plt.ylim(0, 0.5)
plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()
plt.title('t-Distribution')
plt.savefig('./figs/Student.pdf')

print(sum(Student(4, x))*0.01)
print(sum(Student(6, x))*0.01)