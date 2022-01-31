#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if os.path.exists("outPut.txt"):
  os.remove("outPut.txt")

path = sys.argv[1].replace("\\", "/")
keypath = sys.argv[2].replace("\\", "/")
filterType = sys.argv[3]

keyFile = open("C:/Users/Gonzalo Sanz/Desktop/Gonzalo/PythonSearchTool" + "/Keys.txt", 'r', encoding="UTF-8")

for key in keyFile:
    command = 'cmd /c "py premapper.py ' + filterType + ' ' + path + ' | sort | py reducer.py ' + key + '"'
    #command = 'cmd /c "py premapper.py ' + filterType + '"'
    print(key)
    os.system(command)
    #os.system('cmd /k "cls"')

'''Ownership
Industry
Roles
Type
Status
CaseReason
CaseOrigin
Subject
Rating
Stage
ForecastCategory
Rol
Category'''