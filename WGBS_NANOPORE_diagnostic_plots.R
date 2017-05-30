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



#postscript("figure1.1.ps")
pdf("figure1.1.pdf", width=5, height=7)
par(mfrow=c(3,2))

smoothScatter(fwd[,3],fwd[,4],main=paste("Forward strand\nPearson cor:",round(fwd.cor,3)), xlab="WGBS M-Levels",ylab="Nanopore Methylation level",nrpoints=0)

smoothScatter(rev[,3],rev[,4],main=paste("Reverse strand\nPearson cor:",round(rev.cor,3)), xlab="WGBS M-Levels",ylab="Nanopore Methylation level",nrpoints=0)

plot(density(fwd[,3]),main="Forward strand WGBS") 
legend("topleft",legend=paste( names(summary(fwd[,3])),summary(fwd[,3]),collapse=" | "),cex=.4)
plot(density(rev[,3]),main="Reverse strand WGBS")
legend("topleft",legend=paste( names(summary(rev[,3])),summary(rev[,3]),collapse=" | "),cex=.4)

plot(density(fwd[,4]),main="Forward strand Nanopore")
legend("topleft",legend=paste( names(summary(fwd[,4])),summary(fwd[,4]),collapse=" | "),cex=.4)
plot(density(rev[,4]),main="Reverse strand Nanopore")
legend("topleft",legend=paste( names(summary(rev[,4])),summary(rev[,4]),collapse=" | "),cex=.4)
dev.off()

