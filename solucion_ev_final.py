import pandas as pd

#1
detalle_boletas = pd.read_csv("detalle_boletas.csv", encoding="latin-1", sep=",")

#print(detalle_boletas)

#2
#a eliminar columna Precio_prod
#del detalle_boletas["Precio_prod"]
#print(detalle_boletas)

#b
#detalle_boletas["Pais_Venta"]="Chile"
#print(detalle_boletas)

#c
#detalle_boletas = detalle_boletas.rename(columns={"NXXX":"Num Boleta"})
#print(detalle_boletas)

#3
#a