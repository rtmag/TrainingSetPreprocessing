samtools view -Sb hct116_correct_pass_alignment.sam | bedtools bamtobed -i - > hct116_correct_pass_alignment.bed

more hct116_correct_pass_alignment.bed|grep "9102bb6e-5363-4fee-9ac7-05af8b497733_Basecall_2D_2d"| \
bedtools getfasta -fi HCT116_MUHV.fasta -bed - > hct116_ch9_read990_metri_METHYL.fasta

