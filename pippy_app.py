#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importamos lo necesario
import sys, urllib, os
from tempfile import mktemp
from funciones import *

print "Buscar e instalar actividades\n"
print "Para actualizar la lista escribe: actualizar\nPara saber la versión de la lista escribe: version\nPara saber los programas de la lista, escribe: lista\n"

while 1:
  try:
    for tmp in os.listdir("/tmp/"):
      if tmp[0:3]=='tmp' or tmp=='actualizar.zip':
        os.system("rm -rf /tmp/"+tmp)
    actividad=raw_input("Escribe el nombre de la actividad: ").title()
    if actividad=='Version':
      version()
    elif actividad=='Lista':
      lista()
    elif actividad=='Actualizar':
      actualizar()
    else:
      if os.path.exists("./lista/%s" % (actividad))==True:
        fichero=open("./lista/%s" % (actividad))
        for linea in fichero:
          actividad=linea
        temporal=mktemp()
        print ''
        urllib.urlretrieve(actividad, temporal, progreso)
        print "\n\n¡Actividad descargada!"
        while 1:
          conf=raw_input("\n¿Instalar la actividad? ").title()
          if conf=='Si':
            print ''
            os.system("sugar-install-bundle " + temporal)
            os.system("clear ; rm -rf " + temporal)
            print 'Se ha instalado la actividad. Si no aparece en el hogar ni en la lista se recomienda reiniciar la XO.\n'
            break
          elif conf=='No':
            print 'No se ha instalado nada.\n'
            os.system("rm -rf " + temporal )
            break
          else:
            print "Respuesta incorrecta."
      else:
        print "La actividad no se ha encontrado.\n"
  except IOError:
    print "Hay problemas con la conexión a Internet. Revísala o conéctala otra vez.\n"
  except SyntaxError:
    print ''
