import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

size = 1000

x = np.random.randn(size)

y = 1.051 * x + np.random.random(size)

plt.plot(x,y,'*',color='black',label="Dado original")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear')

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("Coeficiente angular (slope)=  %f"  %slope)
print("Coeficiente linear (intercept)=  %f"  %intercept)
print("R quadrado (r-squared)=  %f" %r_value**2)
print("Valor p (p-value)= %f" %p_value)
print("Erro (Std)= %f" %std_err)

ajuste = intercept + slope*x

plt.plot(x,ajuste,color='red',label="Dado ajustado")
plt.legend()
plt.show()