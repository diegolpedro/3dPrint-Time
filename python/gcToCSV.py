#!/usr/bin/python
###############################################################################
# gctocsv - Gcode to CSV extractor                 Autor: PEDRO, Diego - 2018 #
#                                                  Para:  3dClassicParts      #
# Versiones                                                                   #
# 1.0 = Version funcional. Solo muestra salida, no genera todavia el csv.     #
###############################################################################
version = 1.1

import sys	    # Para argumentos.
import re       # Regular expresions.
import commands # Permite ejecutar comandos.

# Return 1 cuando cumpla regex
def displaymatch(regex, testLine):
  match = re.search(regex, testLine)
  if match is None:
    return 0
  return 1

folder_name = sys.argv[1] # Nombre del directorio recibido por
                          # linea de comandos.
files = commands.getoutput('ls '+folder_name).split()
                          # Leemos contenido de directorio y separamos
                          # el resultado en forma de array.
                          # [file1, file2, ..., filen]

file_out = open('output.csv', w)

for file_name in files:   # Recorremos archivos.
  
  cantG1 = 0              # Inicializamos contadores de etiquetas.
  cantM204 = 0
  cantLine = 0

  path = folder_name+'/'+file_name # Armamos direccion.
  
  print path

  with open(path, 'r') as file:    # Abrimos archivos y contamos etiquetas.
    for line_text in file:
      cantG1 = cantG1+displaymatch("^G1", line_text)
      cantM204 = cantM204+displaymatch("^M204", line_text)
      cantLine = cantLine+1
    file.close()

  # Mostramos resultados.
  print "Archivo: "+file_name
  print "Cantidad de Lineas: "+str(cantLine)
  print "Cantidad de G1: "+str(cantG1)
  print "Cantidad de M204: "+str(cantM204)
  lineaCsv = file_name+','+cantLine+','+cantG1+','+cantM204
  file_out.write(lineaCsv)
  

