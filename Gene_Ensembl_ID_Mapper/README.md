# Gene to Ensembl ID Mapper

This workflow maps gene (e.g., TP53, IGF1) to their corresponding Ensembl Gene IDs using the [Ensembl REST API](https://rest.ensembl.org/).

## Features

- Batch annotation of genes
- Human gene support (can be extended to other species)
- Generates direct links to Ensembl gene pages
- Built with Python and `pandas`

## 📦 Requirements

```bash
pip install -r requirements.txt