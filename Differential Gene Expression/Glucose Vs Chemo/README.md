# Differential Gene Expression Analysis: Glucose vs Chemical Conditions

This project investigates differential gene expression (DGE) between glucose and chemical conditions. It demonstrates a complete bioinformatics pipeline—from raw sequence processing to statistical evaluation and data visualization—focusing on RNA-Seq analysis using shell scripts, R, and Python.

> This project is aimed at NGS data processing, scripting, and DGE analysis workflows.

----

## Objectives

- Perform quality control and preprocessing on raw FASTQ files.
- Align reads to a reference genome using high-performance alignment tools.
- Conduct differential expression analysis using DESeq2.
- Visualize key expression differences with volcano plots and heatmaps.
- Maintain workflow reproducibility using batch scripts and modular code.

----

## Repository Structure
. Glucose Vs Chemo/
# Shell scripts for trimming reads
   . Batch-Files/trim_batch/   

# SAM/BAM alignment files
   . Batch-Files/Sam_files/ 

# FastQC and MultiQC quality reports
   . Batch-Files/QC-Files/

# Feature Count file for batch files
   . Batch-Files/Feature_count 

# Summary (.html) files for batch files
   . Batch-Files/Summary_batch     

   
# FastQC and MultiQC quality reports
. Chem-files/QC_files

# Feature Count file for batch files
. Chem-files/Feature_count           

# DESeq2-based DGE pipeline
. R_script/JOVAC_01.R                

# Output: plots, expression tables
. DGE_results                        

. README.md
---

## Data & Methodology

### Input
- Paired-end RNA-seq `.fastq` files (glucose vs chemical).
- Reference genome (mouse).

### Tools Used

| Step                     | Tool(s)               |
|--------------------------|-----------------------|
| Quality Control          | FastQC, MultiQC       |
| Trimming                 | Trimmomatic           |
| Alignment                | HISAT2 or BWA         |
| File Handling            | SAMtools              |
| DGE Analysis             | DESeq2 (R)            |
| Plotting & Visualization | ggplot2, matplotlib   |

----

## Setup Instructions

### Using Conda (recommended)
``bash
conda create -n dge_env \
  fastqc trimmomatic hisat2 samtools \
  r-base r-tidyverse bioconductor-deseq2 \
  python=3.9 matplotlib 
conda activate dge_env
All versions used are compatible with standard UNIX/Linux environments. Use Mamba to speed up Conda installations if needed.

----

## Output Overview

## All final results are stored in the DGE_results/ output_files:
- results.csv – normalized gene expression values and p-values
- heatmap_GluVsChem.png – hierarchical clustering of DEGs
- multiqc_report.html – consolidated QC report
