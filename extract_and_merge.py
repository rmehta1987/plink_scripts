r in {1..22}; do
    plink --noweb --bfile ../files/ALL.chr$chr.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes \
        --keep-allele-order --keep EUR_IDS.txt --make-bed \
            --out ../files/EUR/ALL.chr$chr.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.EUR ;
            done


