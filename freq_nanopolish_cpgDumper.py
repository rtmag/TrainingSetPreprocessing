from sys import argv

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
                    print '{}\t{}\t{}\t{}'.format(line[0],int(line[1])+nb,int(line[1])+nb+1,line[6])
                if first:
                    print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1])+1,line[6]) 
                    first=False

          
        if line[3]==2:
            print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1])+1,line[6]) 
            print '{}\t{}\t{}\t{}'.format(line[0],int(line[2])+1,int(line[2])+2,line[6]) 

        if line[3]==1:
            print '{}\t{}\t{}\t{}'.format(line[0],line[1],int(line[1])+1,line[6]) 
            
      
