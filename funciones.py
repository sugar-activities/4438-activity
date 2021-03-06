#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importamos lo necesario
import sys, os, urllib
from tempfile import mktemp

def progreso(bloque, tamano_bloque, tamano_total):
  cant_descargada = bloque*tamano_bloque
  porcentaje=int((100.0*cant_descargada)/float(tamano_total))
  sys.stdout.write(str(porcentaje) + '% ' + "\r[" + ("#"*(porcentaje/2)) + ' '*(50-(porcentaje/2))+']')

def lista():
  print ''
  for actividad in os.listdir("./lista"):
    if actividad[-1:]!='~':
      print actividad
  print ''

def version():
  ver=open("/home/olpc/Activities/Buscaractividades.activity/version_actual", 'r')
  for numero in ver:
    print "La version actual es: %s" % (numero)
  ver.close()

def actualizar():
  print "\nComprobando si hay actualizaciones..."
  temp=mktemp()
  urllib.urlretrieve("https://sites.google.com/site/materialxo/home/ultima_version", temp, reporthook=None)
  temp_=open(temp, 'r')
  actual=open("./version_actual")
  for versiones in temp_:
    for actuales in actual:
      if int(versiones)>int(actuales):
        for i in range(int(actuales)+1, int(versiones)+1):
          while 1:
            resp=raw_input("\nSe puede actualizar a la versión %d. ¿Deseas actualizar? " % (i))
            if resp=='si':
              print "Actualizando a la versión %d..." % (i)
              direccion="https://sites.google.com/site/materialxo/home/%d" %(i) + ".zip"
              urllib.urlretrieve(direccion, "/tmp/actualizar.zip", reporthook=None)
              os.chdir("/home/olpc/Activities/Buscaractividades.activity/lista")
              os.system("unzip /tmp/actualizar.zip ; cp " + temp + " /home/olpc/Activities/Buscaractividades.activity/version_actual ; rm /tmp/actualizar.zip")
              os.system("clear")
              print "¡Lista actualizada! Si no hay más actualizaciones reinicia esta actividad.\n"
              os.system("rm -rf " + temp)
              break
            if resp=='no':
              print "No se actualizará a la versión %d." % (i)
              os.system("rm -rf " + temp)
              break
            else:
              print "Respuesta incorrecta."
      else:
        print "Ya tienes la última version disponible."
