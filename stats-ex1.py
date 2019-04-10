import pandas as pd
from scipy import stats

df = pd.read_excel('IdadeAltura.xlsx',sheet_name='IdadeAltura')

df_media = df.mean()
df_mediana = df.median()
df_modo = df.mode()
df_std = df.std()
df_skew = df.skew()

print("Valores médios da distribuição")
print(df_media)

print("\n")
print("Valores medianos da distribuição")
print(df_mediana)

print("\n")
print("Exibindo modo da distribuição")
print(df_modo)

print("\n")
print("Exibindo desvio padrão da distribuição")
print(df_std)

print("\n")
print("Exibindo assimetria da distribuição")
print(df_skew)