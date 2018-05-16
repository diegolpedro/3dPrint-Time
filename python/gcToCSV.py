#!/usr/bin/python
###############################################################################
# gctocsv - Gcode to CSV extractor                 Autor: PEDRO, Diego - 2018 #
#                                                  Para:  3dClassicParts      #
# Versiones                                                                   #
# 1.0 = Version funcional. Solo muestra salida, no genera todavia el csv.     #
# 1.1 = Agregado de escritura en CSV.                                         #
# 1.2 = Filtrado de parametros con forma de comentario. Se adiciono help.     #
###############################################################################
version = 1.2

import sys	# Para argumentos.
import re       # Regular expresions.
import commands # Permite ejecutar comandos.

# Return 1 cuando cumpla regex
def displaymatch(regex, testLine):
  match = re.search(regex, testLine)
  if match is None:
    return 0
  return 1

# Help
if len(sys.argv) <> 2:
  print "Error de parametros. Sintaxis: ./gcToCSV.py <dir_name>"
  sys.exit(1)
    

# Inicializacion de variables.
folder_name = sys.argv[1] # Nombre del directorio recibido por
                          # linea de comandos.
files = commands.getoutput('ls '+folder_name).split()
                          # Leemos contenido de directorio y separamos
                          # el resultado en forma de array.
                          # [file1, file2, ..., filen]
idFile = 0

# Apertura de archivo de salida.
file_out = open('output.csv', 'w')
lineaCsv = 'id,filename,cantG1,cantM204,filament_type,default_acceleration,travel_speed,layer_height,support_material,infill_speed,fill_density,fill_pattern,nozzle_diameter\n'
file_out.write(lineaCsv)


for file_name in files:   # Recorremos archivos.
  
  cantG1 = 0              # Inicializamos contadores de etiquetas.
  cantM204 = 0
  filament_type = 'Null'
  path = folder_name+'/'+file_name # Armamos direccion.

  with open(path, 'r') as file:    # Abrimos archivos y contamos etiquetas.
    idFile = idFile+1
    for line_text in file:

      # Contamos etiquetas.
      cantG1 = cantG1+displaymatch("^G1", line_text)
      cantM204 = cantM204+displaymatch("^M204", line_text)
      
      # Filtramos parametros. En cada uno se guarda solo el resultado.
      if displaymatch("; filament_type", line_text) <> 0:
        result = line_text.split('=')
        filament_type = result[1].strip()
      
      if displaymatch("; default_acceleration", line_text) <> 0:
        result = line_text.split('=')
        def_acc = result[1].strip()
      
      if displaymatch("; travel_speed", line_text) <> 0:
        result = line_text.split('=')
        travel_speed = result[1].strip()
      
      if displaymatch("; layer_height", line_text) <> 0:
        result = line_text.split('=')
        layer_height = result[1].strip()
      
      if displaymatch("; support_material", line_text) <> 0:
        result = line_text.split('=')
        support_mat = result[1].strip() # Quitamos espacios en blanco y guardo solo resultado.
        support_mat = support_mat[:-1]  # Quita porcentaje.
      
      if displaymatch("; infill_speed", line_text) <> 0:
        result = line_text.split('=')
        infill_speed = result[1].strip()
      
      if displaymatch("; fill_density", line_text) <> 0:
        result = line_text.split('=')
        fill_density = result[1].strip() # Quitamos espacios en blanco y guardo solo resultado.
        fill_density = fill_density[:-1] # Quita porcentaje.
 
      if displaymatch("; fill_pattern", line_text) <> 0:
        result = line_text.split('=')
        fill_pattern = result[1].strip()

      if displaymatch("; nozzle_diameter", line_text) <> 0:
        result = line_text.split('=')
        nozzle_diameter = result[1].strip()
    
    file.close()

  # Mostramos resultados.
  print "\nArchivo: "+file_name
  print "Numero de Archivo: "+str(idFile)
  print "Cantidad de G1: "+str(cantG1)
  print "Cantidad de M204: "+str(cantM204)
  print "Filament type: "+filament_type
  print "Default acceleration: "+def_acc
  print "Travel speed: "+travel_speed
  print "Layer height: "+layer_height
  print "Support material: "+support_mat
  print "Infill speed: "+infill_speed
  print "Fill density: "+fill_density
  print "Fill patern: "+fill_pattern
  print "Nozzle diameter: "+nozzle_diameter

  lineaCsv =      str(idFile)    +','+file_name    +','+str(cantG1) \
             +','+str(cantM204)  +','+filament_type+','+def_acc     \
             +','+travel_speed   +','+layer_height +','+support_mat \
             +','+infill_speed   +','+fill_density +','+fill_pattern\
             +','+nozzle_diameter+'\n'
  file_out.write(lineaCsv)
  
file_out.close()
