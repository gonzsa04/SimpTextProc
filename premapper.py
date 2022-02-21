#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import sys
import mapper

filterType = sys.argv[1]

mypath = sys.argv[2]
#comentar linea de abajo
mypath = "C:/Users/Gonzalo Sanz/Desktop/Gonzalo/PythonSearchTool/SimpTextProc/test"
mypath = mypath.replace("\\", "/")

files = listdir(mypath)
for file in files:
    #print(file)
    fichero = open(mypath + "/" + file, 'r', encoding="UTF-8")
    mapper.filterWords(fichero, file, filterType)