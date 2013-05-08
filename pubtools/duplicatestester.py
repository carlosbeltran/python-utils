#! /usr/bin/python
import sys
import re

f = open("final.txt",'r')
lista = f.readlines()


for i,linea in enumerate(lista):
    match = re.findall(r'\(\d\d\d\d\)',linea)
    if len(match) >1:
        print i+1
        print str(linea)
