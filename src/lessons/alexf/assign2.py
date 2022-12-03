#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-data-access/walk.htm

from pathlib import *

import arcpy
from arcpy import env

env.overwriteOutput = True
scriptDir = Path.cwd()
WilsonDir = scriptDir / 'Wilson_NC'
dbDir = scriptDir / 'Wilson_NC' / 'Wilson_NC.gdb'

#create FC to GDB
env.workspace = str(dbDir)
element = "County"
desc = arcpy.da.Describe(element)
FCPath = str(dbDir)
FCName = "Powerlines"
arcpy.management.CreateFeatureclass(str(FCPath),FCName,geometry_type = "POLYLINE", spatial_reference = element)

#determine and print number of datasets

walk = arcpy.da.Walk(WilsonDir, type=)

shpNr = len(arcpy.ListFiles())

print("Point feature classes: ")
print("Polyline feature classes: ")
print("Polygon feature classes: ")
print("Raster datasets: ")
print("Tables: ")
print("Shapefiles: ")

# -------------

gdbList = []

fdList = []

for paths, subdirs, names in os.walk(workingPath):
    for subdir in subdirs:
        if subdir[-4:] == '.gdb':
            gdbName = os.path.join(paths, subdir)
            gdbList.append(gdbName)

for fgdb in gdbList:
    walk = arcpy.da.Walk(fgdb, datatype="FeatureDataset")
        for fd in walk:
            if fd[0][-4:] not in '.gdb':
                fdList.append(fd[0])
