# module 01
def validate_dna(seq):
    valid_bases = ['A', 'C', 'G', 'T']
    for base in seq:
        if base not in valid_bases:
            return False
        return True
    return None

# module 02
def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return (g + c) / len(seq)

# module 03
def transcribe(seq):
    return seq.replace('T', 'U')

# module 04
def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_comp = ''.join([complement[base] for base in seq[::-1]])
    return rev_comp

# module 05
def translate(seq):
    codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
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
    protein = ''
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon in codon_table:
            protein += codon_table[codon]
        else:
            protein += 'X'
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
