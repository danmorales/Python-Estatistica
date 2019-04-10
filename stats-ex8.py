import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def cinematica(t,s0,v0,a):
	s = s0 + v0*t +(a*t*t/2.0)
	return s
	
t = np.linspace(0, 5, 500)

s0 = 0.5
v0 = 2.0
a = 1.5

s_noise = 0.5 * np.random.normal(size=t.size)

s = cinematica(t,s0,v0,a)

sdata = s + s_noise

coefs, pcov = curve_fit(cinematica, t, sdata)

plt.plot(t, sdata, 'b-', label='Deslocamento')
plt.plot(t, cinematica(t, *coefs), 'r-',label='Função ajustada')
plt.xlabel('Tempo')
plt.ylabel('Deslocamento')
plt.title('Ajuste de curva')
plt.legend()
plt.show()

print("Espaço inicial= %f" %coefs[0])
print("Velocidade inicial= %f" %coefs[1])
print("Aceleração= %f" %coefs[2])