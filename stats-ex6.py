import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('AjusteCurva.xlsx',sheet_name='Curvas')

x = df["x"]
a = df["a(x)"]
b = df["b(x)"]
c = df["c(x)"]

print("Exibindo valores do arranjo")
print(df)

print("\n")
print("Graficando as diferentes funçÕes no mesmo gráfico")

plt.figure(1)
plt.plot(x,a,'*',color='black')
plt.plot(x,b,'s',color='red')
plt.plot(x,c,'.',color='blue')
plt.xlabel('X')
plt.ylabel('F(x)')
plt.show()

print("\n")
print("Realiando ajustes da função a(x) e graficando")

plt.figure(2)
plt.plot(x,a,'*',color='black')
plt.xlabel('X')
plt.ylabel('a(x)')

a1 = np.poly1d(np.polyfit(x, a, 1))
a2 = np.poly1d(np.polyfit(x, a, 2))
a3 = np.poly1d(np.polyfit(x, a, 3))

print("\n")
print("Exibindo equações dos ajustes")
print("Grau 1 ",a1)
print("Grau 2 ",a2)
print("Grau 3 ",a3)

xp = np.linspace(np.min(x), np.max(x), 100)

plt.plot(xp,a1(xp),color='red',label='Grau 1')
plt.plot(xp,a2(xp),color='blue',label='Grau 2')
plt.plot(xp,a3(xp),color='green',label='Grau 3')
plt.legend(bbox_to_anchor=(0.1, 0.95), loc='upper left', borderaxespad=0.)
plt.show()

print("\n")
print("Realiando ajustes da função b(x) e graficando")

plt.figure(3)
plt.plot(x,b,'*',color='black')
plt.xlabel('X')
plt.ylabel('b(x)')

b1 = np.poly1d(np.polyfit(x, b, 1))
b2 = np.poly1d(np.polyfit(x, b, 2))
b3 = np.poly1d(np.polyfit(x, b, 3))

print("\n")
print("Exibindo equações dos ajustes")
print("Grau 1 ",b1)
print("Grau 2 ",b2)
print("Grau 3 ",b3)

plt.plot(xp,b1(xp),color='red',label='Grau 1')
plt.plot(xp,b2(xp),color='blue',label='Grau 2')
plt.plot(xp,b3(xp),color='green',label='Grau 3')
plt.legend(bbox_to_anchor=(0.1, 0.95), loc='upper left', borderaxespad=0.)
plt.show()

print("\n")
print("Realiando ajustes da função b(x) e graficando")

plt.figure(4)
plt.plot(x,c,'*',color='black')
plt.xlabel('X')
plt.ylabel('c(x)')

c1 = np.poly1d(np.polyfit(x, c, 1))
c2 = np.poly1d(np.polyfit(x, c, 2))
c3 = np.poly1d(np.polyfit(x, c, 3))

print("\n")
print("Exibindo equações dos ajustes")
print("Grau 1 ",c1)
print("Grau 2 ",c2)
print("Grau 3 ",c3)

plt.plot(xp,c1(xp),color='red',label='Grau 1')
plt.plot(xp,c2(xp),color='blue',label='Grau 2')
plt.plot(xp,c3(xp),color='green',label='Grau 3')
plt.legend(bbox_to_anchor=(0.1, 0.95), loc='upper left', borderaxespad=0.)
plt.show()