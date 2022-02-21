#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import os

def filterWords(text, fileName, filterType):
    i = 1
    
    comment = False
    if '.xml' not in fileName:# and '.cmp' not in fileName and '.cls' not in fileName:# and '.cls' not in fileName:
        for line in text:

            if '//' in line and ('.cls' in fileName or '.js' in fileName):
                line = line[0:line.find('//') - 1]
            else: 
                if '@modify' in line:
                    line = line[0:line.find('@modify') - 1]
            if "{'label':" in line:
                line = line[0:line.find("{'label':") - 1]

            if ('/*' in line and ('.cls' in fileName or '.js' in fileName)) or '<!--' in line or ((' <p' in line or ' <h' in line) and '.cls' not in fileName):
                comment = True

            if comment == False:
                ogLine = line
                line = re.sub( r'^\W+|\W+$', '', line )
                words = re.split(r"\W+", line)
        
                for word in words:
                    #print(words)
                    ogLine = ogLine[0:ogLine.find(word) + 200].rstrip('\n').rstrip('\t')
                    letter = ''
                    
                    if filterType == 'w':
                        print(filterType + "-_-_" + letter +  "-_-_" + word + "-_-_" + ogLine + "-_-_" + str(i) + "-_-_" + fileName)
                    else:
                        if filterType == 'l':
                            for letter in word:
                                print(filterType + "-_-_" + letter +  "-_-_" + word + "-_-_" + ogLine + "-_-_" + str(i) + "-_-_" + fileName)
                            
            if '*/' in line or '-->' in line or '</p' in line or '</h' in line:
                comment = False
                
            i+= 1

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    filterWords(sys.stdin)