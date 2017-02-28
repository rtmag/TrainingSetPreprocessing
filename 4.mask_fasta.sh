# Extracting "M" coordinates => "+" & Methylated
grep -E -w "\+.*\M" FILTERED.txt  |awk -F "\t" '{print $1"\t"$2-1"\t"$2}' > M_coor.bed

# Extracting "U" coordinates => "+" & Unmethylated
grep -E -w "\+.*\U" FILTERED.txt  |awk -F "\t" '{print $1"\t"$2-1"\t"$2}' > U_coor.bed

# Extracting "H" coordinates => "-" & Methylated
grep -E -w "\-.*\M" FILTERED.txt  |awk -F "\t" '{print $1"\t"$2-1"\t"$2}' > H_coor.bed

# Extracting "V" coordinates => "-" & Unmethylated
grep -E -w "\-.*\U" FILTERED.txt  |awk -F "\t" '{print $1"\t"$2-1"\t"$2}' > V_coor.bed

# MASKING
bedtools maskfasta -fi ~/CY/RawData/P007_48_DMSO/HCT116.fasta -bed M_coor.bed -fo HCT116_M.fasta -mc M
bedtools maskfasta -fi HCT116_M.fasta -bed U_coor.bed -fo HCT116_MU.fasta -mc U
bedtools maskfasta -fi HCT116_MU.fasta -bed H_coor.bed -fo HCT116_MUH.fasta -mc H
bedtools maskfasta -fi HCT116_MUH.fasta -bed V_coor.bed -fo HCT116_MUHV.fasta -mc V
