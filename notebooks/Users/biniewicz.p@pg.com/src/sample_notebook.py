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
