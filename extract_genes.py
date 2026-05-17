genes = set()

with open("motif_hits.fa") as f:
    for line in f:
        if line.startswith(">"):
            gene = line.strip().split("|")[-1]
            genes.add(gene)

with open(
    "optimal_site_nrf1_in_hg38_tss_upstream_500.genes.tsv",
    "w"
) as out:
    for g in sorted(genes):
        out.write(g + "\n")

print("Gene list created!")
