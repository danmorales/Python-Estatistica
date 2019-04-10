from scipy.stats import bernoulli, gaussian_kde
import matplotlib.pyplot as plt

#Gerando distribuição Bernoulli com 10000 pontos
bernoulli_dist = bernoulli.rvs(size=1000,p=0.6)

#Gerando histograma da distribuição
n_bins = 10
count, bins, ignored = plt.hist(bernoulli_dist, n_bins, normed=True,color='red')

#Calculando gráfico de densidade da distribuição

densidade = gaussian_kde(bernoulli_dist)
xs = np.linspace(0,2,200)
densidade._compute_covariance()

plt.plot(xs,densidade(xs))
plt.xlabel('Poisson')
plt.ylabel('Frequencia')
plt.title('Distribuição Bernoulli')
plt.show()