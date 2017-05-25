# Note for CY:
# use the following command to test the output file of this CGdump.py script
# head -n 1000000 ../../nanopolish/cgdumptest2.txt|awk -F"\t" '{print $1"\t"$2"\t"$2+2}' |bedtools getfasta -fi HCT116.fasta -bed - |grep -v ">"|uniq -c


from sys import argv
import re

if argv<3:
    sys.exit("usage: python script.py mode[forward,reverse] inputFile")
    
mode = argv[1] 
filename = argv[2]

if mode == "forward":
    with open(filename, "r") as file:
        firstline = True
        for line in file:
            if firstline:
                firstline = False
                continue
                
            line=line.split("\t")
        
            if int(line[3])>1:
                index=[m.start() for m in re.finditer('CG', line[7])]
                first=True
                for ix in index:
                    if not first:
                        nb=int(ix)-int(index[0])
                        print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+nb,int(line[1])+nb,float(line[6])*100)
                    if first:
                        print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1]),float(line[6])*100) 
                        first=False 
            if int(line[3])==1:
                        print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1]),float(line[6])*100) 

if mode == "reverse":
    with open(filename, "r") as file:
        firstline = True
        for line in file:
            if firstline:
                firstline = False
                continue
                
            line=line.split("\t")
        
            if int(line[3])>1:
                index=[m.start() for m in re.finditer('CG', line[7])]
                first=True
                for ix in index:
                    if not first:
                        nb=int(ix)-int(index[0])
                        print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+nb+1,int(line[1])+nb+1,float(line[6])*100)
                    if first:
                        print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+1,int(line[1])+1,float(line[6])*100) 
                        first=False 
            if int(line[3])==1:
                        print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+1,int(line[1])+1,float(line[6])*100)
