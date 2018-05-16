#Cargo datos desde los csv.
datos_tiempo = read.csv2("tiempos.csv", header=TRUE, sep=";")

# Visualizamos los datos.
head(datos_tiempo)
names(datos_tiempo)

# Veamos como se distribuyen los tiempos.
boxplot( datos_tiempo["print_time"], 
         main = "Tiempos de Impresion", 
         col=2)

