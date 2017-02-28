
zcat combine_hct116_WGBS_1_bismark_bt2_pe.coverage.report.gz | awk -F'\t' '{ $COV=($4+$5); $B=($4/$COV) ; \
                                                                          if( $COV>4 ){ if( $B>=0.8 ){ \
                                                                                print $1"\t"$2"\t"$3"\t"M } } \
                                                                          if( $COV>4 ){ if( $B<=0.2 ){ \
                                                                                print $1"\t"$2"\t"$3"\t"U } } \
                                                                           }' > FILTERED.txt
