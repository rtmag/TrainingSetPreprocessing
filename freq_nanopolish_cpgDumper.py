from sys import argv
import re

filename = argv[1]


with open(filename, "r") as file:
    for line in file:
        line=line.split("\t")
        
        if line[3]>2:
            index=[m.start() for m in re.finditer('CG', line[7])]
            first=True
            for ix in index:
                if not first:
                    nb=int(ix)-int(index[0])
                    print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+nb,int(line[1])+nb,float(line[6])*100)
                if first:
                    print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1]),float(line[6])*100) 
                    first=False

          
        if line[3]==2:
            print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1])+1,float(line[6])*100) 
            print '{}\t{}\t{}\t{}'.format(line[0],int(line[2])+1,int(line[2])+1,float(line[6])*100) 

        if line[3]==1:
            print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1]),float(line[6])*100) 
