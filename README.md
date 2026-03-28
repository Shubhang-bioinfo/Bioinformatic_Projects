# Bioinformatic_Projects

**Bioinformatic_Projects** is a curated repository comprising a series of independent, modular, and academic-focused bioinformatics and computational biology projects.  
Each script reflects applied problem-solving in genomics, transcriptomics, machine learning, metagenomics, etc.

These projects were developed during postgraduate study in bioinformatics, with the objective of gaining proficiency in research-aligned data analysis pipelines using R, Python, and PyTorch. Emphasis is placed on algorithmic clarity, reproducibility, and translational relevance.

---

## 📁 Repository Contents

| Project | Description | Language(s) |
|--------|-------------|-------------|
| `DNA_Sequence_Analyzer/` | A pipeline to validate, transcribe, reverse-complement, translate, and analyze nucleotide sequences. | Python |
| `Voice_to_Text_Clinical_Model/` | A PyTorch-based voice-to-text model designed to streamline clinical documentation through speech recognition. | Python (PyTorch) |
| `Mycobacterium_Alignment/` | Sequence alignment of _Mycobacterium perituberculosis_ isolates for comparative genomics. | Python (Biopython) |
| `Differential_Gene_Expression/` | Differential gene expression analysis in murine samples exposed to glucose and chemical treatments. | R, Python |

---

## 🔬 Project Overviews

### 1. DNA Sequence Analyzer

This project consists of standalone Python scripts for core sequence analysis tasks, including:

- Nucleotide sequence validation 
- GC content estimation
- DNA to RNA transcription
- Reverse complementation
- Six-frame translation
- Codon frequency distribution

The scripts operate without dependencies on external libraries such as Biopython, to reinforce conceptual understanding of bioinformatics algorithms from first principles.

📁 Folder: `DNA_Sequence_Analyzer/`

---

### 2. Voice-to-Text Clinical Model

This project proposes a machine learning-based solution for **automated clinical documentation** via voice-to-text transcription. Using PyTorch and scikit-learn, a neural network model is trained on sample clinical utterances to produce accurate transcriptions.

**Key components:**
- Preliminary integration with structured text formatting for diagnosis recording

This module addresses inefficiencies in manual patient data entry by clinicians, offering a proof-of-concept for integration into hospital information systems.

📁 Folder: `Voice_to_Text_Clinical_Model/`

---

### 3. Mycobacterium Alignment

Implements global and local sequence alignments for studying genomic similarity across _Mycobacterium perituberculosis_ strains.

**Implemented using:**
- Biopython’s `pairwise2` module
- Basic I/O handling for FASTA files
- Output includes alignment score and visualization of conserved regions

Intended for preliminary comparative genomics and pathogen evolution studies.

📁 Folder: `Mycobacterium_Alignment/`

---

### 4. Differential Gene Expression (DGE) Analysis

This R-based project involves a DGE analysis using gene expression data derived from **murine models exposed to glucose and a chemical treatment**. It includes:

- Preprocessing and normalization using DESeq2
- Volcano plot generation for differentially expressed genes
- Functional enrichment insights (optional)
- Gene annotation and grouping

📁 Folder: `Differential_Gene_Expression/`

---

## Technical Stack

- **Languages:** Python 3.x, R 4.x  
- **Libraries/Frameworks:** Biopython, PyTorch, DESeq2, Scikit-learn, Pandas, Matplotlib  
- **Tools:** Git, PyCharm, VSCode, RStudio, Conda

---

## Citation & Use

This repository is intended for **academic training, code transparency, and reproducibility**. Students, researchers, and developers are encouraged to fork and adapt the scripts for their own learning and analyses. Proper attribution is appreciated.

If any portion of the code is used in publications or derivative work, please cite as:

> Shubhang [M.Sc. (Honors) Bioinformatics]. *Bioinformatic_Projects: A collection of applied bioinformatics projects*. GitHub repository, 2025. [https://github.com/Shubhang-bioinfo/Bioinformatic_Projects](https://github.com/Shubhang-bioinfo/Bioinformatic_Projects)

---

## Contact

For research queries or collaboration proposals, please connect via:

- GitHub: [github.com/Shubhang-bioinfo](https://github.com/Shubhang-bioinfo)
- Email: shubhangbiotech.22685@gmail.com
- LinkedIn: [linkedin.com/shubhang-arya](https://www.linkedin.com/in/shubhang-arya-4b2b0524a/) 
