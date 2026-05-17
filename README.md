# GO Enrichment Analysis of NRF1 Motif in Human Promoters

In this project, we analyzed human promoter regions to identify genes containing the NRF1 transcription factor binding motif (`GCGC..GCGC`). 

The workflow involved:

- Converting human gene annotation data into BED format
- Generating 500 bp upstream promoter regions in a strand-aware manner using `bedtools`
- Extracting promoter DNA sequences from the human genome
- Searching promoter sequences for the NRF1 motif
- Extracting genes containing the motif
- Performing Gene Ontology (GO) enrichment analysis using `clusterProfiler` in R

The final output includes enriched biological processes and a GO enrichment dot plot visualization.
