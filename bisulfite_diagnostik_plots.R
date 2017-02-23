
data = read.table( pipe("zcat combine_hct116_WGBS_1_bismark_bt2_pe.coverage.report.gz|cut -f 4,5,6"), 
                  colClasses=c("integer", "integer", "character") )
