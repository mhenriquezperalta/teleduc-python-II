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
#print(detalle_boletas.loc[1:10])
#detalle_boletas = detalle_boletas.loc[~(detalle_boletas["ID"].str.contains("4XXXXX")) & ~(detalle_boletas["Nombre"].str.contains("XXXX"))]
print(detalle_boletas)

#b
#print(detalle_boletas["Fecha"].str.replace("_/","/"))
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("!","")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("{","")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("-","")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace(".","")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("-","")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace(".","")
print(detalle_boletas["Fecha"])


#4

#5

#6
#lista_productos = pd.read_csv("Lista productos.csv", encoding="UTF-8", sep=",")
#print(lista_productos)

#7


#8


#9