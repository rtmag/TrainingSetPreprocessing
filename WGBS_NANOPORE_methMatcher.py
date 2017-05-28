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
        if (int(line[3])+int(line[4]))>0:
            if str(line[5])=="CG":
                WGBS[ ( str(line[0]), int(line[1]) ) ] = float(line[3])/(float(line[3])+float(line[4])) 
    
file.close()

NANO_file = 'hct116_pass_template_nanopolish_bwa_hct116corrected_forward_methylation_freq_CGdump.tsv'
output = open('WGBS_NANOforward_2.txt', 'w')

with open(NANO_file, "r") as file:
    for line in file:
        line = line.rstrip()
        line = line.split("\t")
        WGBS_meth = WGBS.get( ( str(line[0]), int(line[1])+1 ) ) or "EMPTY"
        if WGBS_meth != 'EMPTY':
            output.write('{}\t{}\t{}\t{}\n'.format(str(line[0]),int(line[1]),float(WGBS_meth)*100,float(line[3]) ) )
      
output.close()
file.close()
