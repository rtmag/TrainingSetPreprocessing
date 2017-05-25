# TO DO
# 1) fast way to read-in file into dictionary
# 2) use tuple as keys

from sys import argv
import re
import gzip
  
WGBS_file = argv[1] 
NANO_file = argv[2]


WGBS = {}
with gzip.open(WGBS_file, "r") as file:
    for line in file:
        line=line.split("\t")
        WGBS[ ( str(line[0]), int(line[1]) ) ] = float(line[3])
    

