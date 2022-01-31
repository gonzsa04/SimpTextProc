#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

def printLines():
    word = sys.argv[1]

    fichero = open('outPut.txt', 'a',  encoding="UTF-8")

    for line in sys.stdin:
        filterType, letter, key, keyLine, lineNumber, fileName = line.split( '-_-_' )
        if key == word and filterType == 'w':
            fichero.write(
                "(F: " + filterType + ") Se ha encontrado la palabra " + key + " en el archivo " + fileName.rstrip('\n') + " en la Línea " + lineNumber +
                '\n' +
                '\n' +  lineNumber + ' ' + keyLine[keyLine.find(keyLine.split()[0]):-1] + 
                '\n' +
                '\n' + 
                fileName +
                '\n' +
                "-Linea " + lineNumber +
                '\n' + 
                '\n' + 
                "----------------------------------------------------------------------------------------" +
                '\n'
             )
        else:
            if letter == word and filterType == 'l':
                fichero.write(
                    "(F: " + filterType + ") Se ha encontrado la letra " + letter + " en la palabra " + key + " en el archivo " + fileName.rstrip('\n') + " en la Línea " + lineNumber +
                    '\n' +
                    '\n' +  lineNumber + ' ' + keyLine[keyLine.find(keyLine.split()[0]):-1] + 
                    '\n' +
                    '\n' + 
                    fileName +
                    '\n' +
                    "-Linea " + lineNumber +
                    '\n' + 
                    '\n' + 
                    "----------------------------------------------------------------------------------------" +
                    '\n'
                )
            #print ("word: " + word)
            #print ("key: " + key)
            #print ("keyLine: " + keyLine)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    printLines()