# Reading in bismark cytosine report 
data = read.table( pipe("zcat combine_hct116_WGBS_1_bismark_bt2_pe.coverage.report.gz|cut -f 4,5,6"), 
                  colClasses=c("integer", "integer", "character") )

# Coverage barplot
coverage = data[,1] + data[,2]
coverage[coverage>15] = 15
barplot(table(coverage),border=NA,col="darkred")

# Methylation level distribution

