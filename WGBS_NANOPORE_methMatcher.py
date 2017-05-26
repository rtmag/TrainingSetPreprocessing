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
        if (line[3]+line[4])>0:
          if str(line[5])=="CG"
             WGBS[ ( str(line[0]), int(line[1]) ) ] = float(line[3](line[3]+line[4]))
    
file.close()

with open(NANO_file, "r") as file:
    for line in file:
        line = line.split("\t")
        WGBS_meth = WGBS.get( ( str(line[0]), int(line[1]) ) ) or False
        WGBS_meth = str(WGBS_meth)
        if WGBS_meth:
            print '{}\t{}\t{}\t{}'.format(str(line[0]),int(line[1]),float(WGBS_meth),float(line[3]))
      
file.close()
