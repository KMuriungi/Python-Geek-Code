import random
import sys
import os

textFile = open("textFile.txt","wb")

print (textFile.mode)

print (textFile.name)

textFile.write(bytes("KITHINJI A. MURIUNGI\n ", 'UTF-8'))