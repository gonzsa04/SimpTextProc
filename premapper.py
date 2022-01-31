#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import sys
import mapper

mypath = 'C:/Users/Gonzalo Sanz/Desktop/Gonzalo/PythonSearchTool/test'
files = listdir(mypath)

filterType = sys.argv[1]

for file in files:
    #print(file)
    fichero = open(mypath + "/" + file, 'r', encoding="UTF-8")
    mapper.filterWords(fichero, file, filterType)