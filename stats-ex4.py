from scipy.stats import poisson, gaussian_kde
import matplotlib.pyplot as plt

#Gerando distribuição Poisson com 10000 pontos
poisson_dist = poisson.rvs(mu=4, size=10000)

#Gerando histograma da distribuição
n_bins = 10
count, bins, ignored = plt.hist(poisson_dist, n_bins, normed=True,color='red')

#Calculando gráfico de densidade da distribuição

densidade = gaussian_kde(poisson_dist)
xs = np.linspace(0,n_bins,200)
densidade._compute_covariance()

plt.plot(xs,densidade(xs))
plt.xlabel('Poisson')
plt.ylabel('Frequencia')
plt.title('Distribuição Poisson')
plt.show()