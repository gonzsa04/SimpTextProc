#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgi import test
import os
import sys

if os.path.exists("outPut.txt"):
  os.remove("outPut.txt")

path = sys.argv[1]
#comentar linea de abajo
#path = "D:/Users/Gonzalo/Desktop/JGSL/Proyectos/PythonSearch Tool/SimpTextProc"
path = path.replace("\\", "/")

keypath = sys.argv[2]
#comentar linea de abajo
#keypath = "/Keys.txt"
keypath = keypath.replace("\\", "/")

testPath = sys.argv[3]
#comentar linea de abajo
#testPath = "/test"
testPath = testPath.replace("\\", "/")

filterType = sys.argv[4]

keyFile = open(path + keypath, 'r', encoding="UTF-8")

#path = '"' + path + testPath + '"'

for key in keyFile:
    print(key)
    command = 'cmd /c "py premapper.py ' + filterType + ' ' + path  + ' | sort | py reducer.py ' + key + '"'
    #command = 'cmd /c "py premapper.py ' + filterType + '"'
    os.system(command)
    #os.system('cmd /k "cls"')