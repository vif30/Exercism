def to_rna(dna_strand):
    rna = ""
    for i in dna_strand:
        if i == "G":
            rna += "C"
        if i == "C":
            rna += "G"
        if i == "T":
            rna += "A"
        if i == "A":
            rna += "U"
    return rna
