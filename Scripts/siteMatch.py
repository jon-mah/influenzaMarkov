#Compares two sequences and outputs match ratio.
def siteMatch(aminoAcids):
    numberMatches = 0
    for i in range(len(aminoAcids[0])):
        if aminoAcids[0][i] == aminoAcids[1][i]:
            numberMatches += 1
    percent = numberMatches/len(aminoAcids[0])
    return percent

print((siteMatch(['AGGSEDKELA', 'ACCSEDKEFA'])))
