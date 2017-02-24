# Reading in bismark cytosine report. <MethylatedCount> <UnmethylatedCount> <Context>
data = read.table( pipe("zcat combine_hct116_WGBS_1_bismark_bt2_pe.coverage.report.gz|cut -f 4,5,6"), 
                  colClasses=c("integer", "integer", "character") )

# open plot file
pdf("Diagnostik_coverage_HCT116_CY.pdf")

### Coverage barplot ###
coverage = data[,1] + data[,2]
coverage[coverage>15] = 15

barplot( table(coverage), border=NA, col="darkred", main="Coverage all Cs")
dev.off()
### Methylation level distribution ###
# set coverage threshold first

coverage = data[,1] + data[,2]

pdf("Diagnostik_beta_CG_HCT116_CY.pdf")
cov.ix = coverage > 9 & data[,3]=="CG"
# plot
beta = data[cov.ix,1] / coverage[cov.ix]
plot(density(beta))
# close plot file
dev.off()

pdf("Diagnostik_beta_CHG_HCT116_CY.pdf")
cov.ix = coverage > 9 & data[,3]=="CHG"
# plot
beta = data[cov.ix,1] / coverage[cov.ix]
plot(density(beta))
# close plot file
dev.off()

pdf("Diagnostik_beta_CHH_HCT116_CY.pdf")
cov.ix = coverage > 9 & data[,3]=="CHH"
# plot
beta = data[cov.ix,1] / coverage[cov.ix]
plot(density(beta))
# close plot file
dev.off()
