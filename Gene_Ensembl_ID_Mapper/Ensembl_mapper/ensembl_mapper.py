import pandas as pd
import requests

# Load your Excel file
df = pd.read_excel("")  # enter the file path of the excel file
genes = df['Genes'].dropna().unique().tolist() # assuming the gene names are under the column 'Genes'

# Function to get Ensembl ID and URL
def get_ensembl_info(gene, species='homo_sapiens'):
    url = f"https://rest.ensembl.org/xrefs/symbol/{species}/{gene}?"
    headers = {"Content-Type": "application/json"}
    r = requests.get(url, headers=headers)
    if r.ok:
        data = r.json()
        for entry in data:
            if entry.get('type') == 'gene':
                ensembl_id = entry['id']
                link = f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={ensembl_id}"
                return ensembl_id, link
    return None, None

# Map and store results
mapped = []
for gene in genes:
    ensembl_id, link = get_ensembl_info(gene)
    mapped.append({
        'Gene Symbol': gene,
        'Ensembl Gene ID': ensembl_id,
        'Ensembl Link': link
    })

# Save to new Excel file
result_df = pd.DataFrame(mapped)
result_df.to_excel("Gene_Ensembl_Mapped.xlsx", index=False)
print("Mapping complete. Output saved as Gene_Ensembl_Mapped.xlsx")
