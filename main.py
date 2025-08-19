import pandas as pd
from matplotlib import pyplot as plt

# Gráfica de ejemplo
eje_y = [2,3,5,7,11]
eje_x = ["A","B","C","D","E"]

# Barra estática
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="blue", label="Datos de ejemplo")
ax.set_title("Gráfica de ejemplo (barras)")
fig.savefig("Generados/grafica_ejemplo_barra.png", bbox_inches="tight")
plt.close(fig)

# Pastel estático
fig, ax = plt.subplots()
ax.pie(eje_y, labels=eje_x,autopct="%1.1f%%", startangle=90)
ax.set_title("Gráfica de ejemplo (pastel)")
fig.savefig("Generados/grafica_ejemplo_pastel.png", bbox_inches="tight")
plt.close(fig)

#Leer archivo excel
archivo_excel="Datos/Datos_base_practica4.xlsx"
contador=1
while contador <=5:
    data_hoja= pd.read_excel(archivo_excel, sheet_name=f"Hoja{contador}", engine="openpyxl")
    print(f"Datos leídos de la hoja {contador}")
    
    eje_x = data_hoja.iloc[:, 0]  
    eje_y_barras = data_hoja.iloc[:, 1] 
    eje_y_pastel = data_hoja.iloc[:, 2] 
    
    # Gráfico de barras 
    fig, ax = plt.subplots()
    ax.bar(eje_x, eje_y_barras, color="green", label=f"Datos de Hoja {contador}")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_xticklabels(eje_x, rotation=45)
    ax.set_title(f"Gráfica de la hoja {contador}(barras)")
    fig.savefig(f"Generados/grafica_{contador}_barras.png", bbox_inches="tight")
    plt.close(fig)
    
    # Gráfico de pastel 
    fig, ax = plt.subplots()
    ax.pie(eje_y_pastel, labels=eje_x,autopct="%1.1f%%", startangle=90)
    ax.set_title(f"Gráfica de la hoja {contador}(pastel)")
    fig.savefig(f"Generados/grafica_{contador}_pastel.png", bbox_inches="tight")
    plt.close(fig)
    
    contador=contador+1
print("Gráficas de barra y pastel generadas y guardadas en la carpeta 'Generados'.")
