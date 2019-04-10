import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

size = 1000

x = 5.0 * np.random.randn(size)

y = 1.051 * x + 2.05 * np.random.random(size)

x = x[:, np.newaxis]
y = y[:, np.newaxis]

#Criando o objeto que realizará a regressão linear
regr = linear_model.LinearRegression()

#Quebrando o arranjo em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#Treinando o modelo usando os dados de treino definidos acima
regr.fit(X_train,y_train)

#Realizar previsões utilizando o arranjo de testes
y_pred = regr.predict(X_test)

#Exibindo os coeficientes
print('Coeficiente angular: \n', regr.coef_)
print('Coeficiente linear: \n', regr.intercept_)

#Determinando erro quadrático médio
mse = mean_squared_error(y_test, y_pred)
print("Erro quadrático médio= %.2f" %mse)

#Determinando a variância
variancia = r2_score(y_test, y_pred)
print("Variância= %.2f" %variancia)

#Graficando os dados
plt.figure(1)
plt.plot(x,y,'*',color='black',label="Dado original")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear')
plt.show()

plt.figure(2)
plt.scatter(X_test,y_test,color='black',label="Dados de teste")
plt.plot(X_test,y_pred,color='blue',label="Dados ajustado")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear')
plt.show()