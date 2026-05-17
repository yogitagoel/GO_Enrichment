import pandas as pd

# Read annotation file
df = pd.read_csv(
    "human_gene_annotation.tsv",
    sep="\t",
    low_memory=False
)

# Convert strand values
df["strand_symbol"] = df["strand"].map({
    1: "+",
    -1: "-"
})

# Add chr prefix
df["chromosome_name"] = (
    "chr" + df["chromosome_name"].astype(str)
)

# Fix mitochondrial chromosome name
df["chromosome_name"] = df["chromosome_name"].replace({
    "chrMT": "chrM"
})

# Create BED dataframe
bed = pd.DataFrame()

# Column 1: chromosome
bed[0] = df["chromosome_name"]

# Column 2: TSS
bed[1] = df["transcription_start_site"]

# Column 3: TSS + 1
bed[2] = df["transcription_start_site"] + 1

# Column 4: chr@start-end|gene
bed[3] = (
    bed[0]
    + "@"
    + bed[1].astype(str)
    + "-"
    + bed[2].astype(str)
    + "|"
    + df["external_gene_name"]
)

# Column 5: placeholder
bed[4] = "."

# Column 6: strand
bed[5] = df["strand_symbol"]

# Save BED file
bed.to_csv(
    "genes.bed",
    sep="\t",
    header=False,
    index=False
)

print("genes.bed created successfully!")
