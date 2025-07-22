# module 01
def validate_dna(seq):
    valid_bases = ['A', 'C', 'G', 'T']
    for base in seq:
        if base not in valid_bases:
            print(f"Invalid base: {base}")
    print(f"Valid bases")

# module 02
def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    gc_content = (g + c) / len(seq)
    result01 = round(gc_content * 100, 2)
    print("G =",g, "C =", c)
    print("Length of Sequence = ",len(seq))
    return result01


# module 03
def transcribe(seq):
    return  seq.replace('T', 'U')

# module 04
def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_comp = ''.join([complement[base] for base in seq[::-1]])
    return rev_comp

# module 05
def translate(seq):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    # Step 1: Clean the sequence
    seq = seq.upper().replace('\n', '').replace(' ', '')
    seq = ''.join([base for base in seq if base in 'ATGC'])

    # Step 2: Make sure it's a multiple of 3
    seq = seq[:len(seq) - (len(seq) % 3)]

    # Step 3: Translate codons
    protein = ''
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, 'X')  # 'X' for unknown codon

    return protein

# module 06
def codon_freq(seq):
    freq = {}
    for i in range(0, len(seq)-2,3):
        codon = seq[i:i+3]
        if codon in freq:
            freq[codon] += 1
        else:
            freq[codon] = 1
    return freq
