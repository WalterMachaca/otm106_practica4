import pandas as pd

archivo_excel = "Datos/Datos_base_practica3.xlsx"

data_hoja_1= pd.read_excel(archivo_excel, sheet_name="Hoja 1")

print(data_hoja_1)
