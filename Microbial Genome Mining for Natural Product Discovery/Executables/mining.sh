#!/bin/bash

# ==========================================
# PHASE 1: ASSEMBLY EXTRACTION & SCAFFOLDING
# ==========================================
conda create -n biosynthetic -y
conda activate biosynthetic
conda install -c bioconda samtools blast ragtag -y

# Install Entrez Direct
sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
export PATH=${HOME}/edirect:${PATH}

# Index and extract the shattered antiSMASH contigs
samtools faidx CBC-1.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_13:1-40197" > Contig13_NRPS.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_15:1-30650" > Contig15_NRPS.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_22:1-12876" > Contig22_NRPS.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_23:1-6497" > Contig23_NRPS.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_24:1-3817" > Contig24_NRPS.fasta
csamtools faidx CBC-1.fasta "CBC-1-assembly_contig_25:1-3407" > Contig25_NRPS.fasta
samtools faidx CBC-1.fasta "CBC-1-assembly_contig_26:1-3356" > Contig26_NRPS.fasta

# Concatenate the fragments
cat Contig13_NRPS.fasta Contig15_NRPS.fasta Contig22_NRPS.fasta Contig23_NRPS.fasta Contig24_NRPS.fasta Contig25_NRPS.fasta Contig26_NRPS.fasta > Fragmented_NRPS_Cluster.fasta

# Build BLAST database and align to reference (Assuming K10.fna is your local MAP K-10 genome)
makeblastdb -in K10.fna -dbtype nucl -out RefDB
blastn -query Fragmented_NRPS_Cluster.fasta -db RefDB -out Fragmented_NRPS_alignment.tsv -outfmt "6 qseqid sseqid pident length qstart qend sstart send" -evalue 1e-10

# Verify alignment coordinates
awk -F'\t' '{print $0}' Fragmented_NRPS_alignment.tsv | sort -k7,7n

# Scaffold the contigs into a single sequence
ragtag.py scaffold K10.fna Fragmented_NRPS_Cluster.fasta -o RagTag_NRPS_Output

# Export the biosynthetic environment
conda env export -n biosynthetic > biosynthetic.yml

# ==========================================
# PHASE 2: MANUAL ANNOTATION CHECKPOINT
# ==========================================
echo "PIPELINE PAUSED."
echo "ACTION REQUIRED: You must now upload 'RagTag_NRPS_Output/ragtag.scaffold.fasta' to the antiSMASH web portal."
echo "Download the resulting Region 1.1 GenBank file and save it in this directory as 'NZ_CP106873.1_RagTag.region001.gbk'."
echo "Once the file is in place, execute Phase 3."

# (The script should logically exit or pause here in practice)

# ==========================================
# PHASE 3: SYNTENY VISUALIZATION
# ==========================================
conda create -n clinker python=3.10 -y
conda activate clinker
conda install -c conda-forge -c bioconda clinker-py -y

# Extract the homologous reference operon directly from NCBI
efetch -db nuccore -id NZ_CP106873.1 -seq_start 1480000 -seq_stop 1580000 -format gb > Reference_MAP_K10_1.51Mb.gbk

# Execute comparative visualization
clinker NZ_CP106873.1_RagTag.region001.gbk Reference_MAP_K10_1.51Mb.gbk -p Final_BGC_Synteny_Figure.html
