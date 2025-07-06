import pandas as pd
from matplotlib import pyplot as plt

archivo_excel = "Datos/Datos_base_practica3.xlsx"
data_hoja_5= pd.read_excel(archivo_excel, sheet_name="Hoja5")
print(data_hoja_5)

eje_y = [2,3,5,7,11]
eje_x = ["A","B","C","D","E"]
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="blue", label="Datos de ejemplo")
fig.savefig("generados/grafica_ejemplo.png", bbox_inches="tight")

eje_x = data_hoja_5.iloc[:, 0]  
eje_y = data_hoja_5.iloc[:, 1]  
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="green", label="Datos de Hoja5")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_xticklabels(eje_x, rotation=45)
fig.savefig("generados/grafica_hoja5.png", bbox_inches="tight")