from sys import argv
import re

if argv<3:
    print "usage: python script.py mode[forward,reverse] inputFile"
    sys.exit()
    
mode = argv[1] 
filename = argv[2]

if mode == "forward":
    with open(filename, "r") as file:
        for line in file:
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
        for line in file:
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
