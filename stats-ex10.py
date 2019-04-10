import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def model(x):
    return 1 / (1 + np.exp(-x))

size = 1000

#Gerando distribuição de dados
x = np.random.normal(size=size)
y = (x > 0).astype(np.float)

x = x[:, np.newaxis]

#Criando o objeto que realizará a regressão logistica
logreg = linear_model.LogisticRegression(C=1e5, solver='lbfgs')

#ajustado os dados
logreg.fit(x,y)

x_test = np.linspace(-4, 4, 400)

#Realizar previsões utilizando o arranjo de testes
y_pred = model(x_test * logreg.coef_ + logreg.intercept_).ravel()

plt.scatter(x, y, color='black',label='Dado original')
plt.plot(x_test,y_pred,color='red',label='Dado ajustado')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Regressão logistica')
plt.show()

