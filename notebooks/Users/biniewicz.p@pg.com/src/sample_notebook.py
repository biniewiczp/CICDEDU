# Databricks notebook source
# MAGIC %run ./InstallDepedencies

# COMMAND ----------

import numpy
print ( "***** Hello World ********")
numpy.test ('full')
print ("***** DUPA ***** ")
print ("proba 2")
print ("***** Hello World********")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
hours_full=list()
hour=dict()
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
hours_full=list()
hour=dict()
for line in fh:
    #print(line.rstrip())
    if not line.startswith('From'): continue
    lst=line.rstrip().split()
    if len(lst)>2:
         hours_full=lst[5].rstrip().split(':')
         hour[hours_full[0]]=hour.get(hours_full[0],0)+1
sorted(hour.items())

for i,j in sorted(hour.items()):
    print(i,j)