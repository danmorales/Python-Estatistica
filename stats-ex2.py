import numpy as np
import matplotlib.pyplot as plt

mu = 0.5
sigma = 0.1

#Gerando distribuição normal com 1000 elementos
normal_dist = np.random.normal(mu, sigma, 1000)

#Graficando dados num histograma com n_bins
n_bins = 20
count, bins, ignored = plt.hist(normal_dist, n_bins, normed=True,color='red')

#Calculando gaussiana através dos dados
gaussiana = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2))

plt.plot(bins,gaussiana,linewidth=3, color='blue')
plt.xlabel('Intervalo')
plt.ylabel('Contagem')
plt.title('Distribuição normal')

plt.show()

