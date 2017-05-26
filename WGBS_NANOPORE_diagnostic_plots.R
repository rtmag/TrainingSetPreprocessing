library(graphics)

# panels on the plot #rows then #columns
par(mfrow=c(3,2))

fwd=read.table("WGBS_NANOforward_2.txt",sep="\t")
rev=read.table("WGBS_NANOreverse_2.txt",sep="\t")

smoothScatter(fwd[,3],fwd[,4],main="Forward strand",xlab="WGBS M-Levels",ylab="Nanopore Methylation level")
smoothScatter(rev[,3],rev[,4],main="Reverse strand",xlab="WGBS M-Levels",ylab="Nanopore Methylation level")

plot(density(fwd[,3]),main="Forward strand WGBS")
plot(density(rev[,3]),main="Reverse strand WGBS")

plot(density(fwd[,4]),main="Forward strand Nanopore")
plot(density(rev[,4]),main="Reverse strand Nanopore")
