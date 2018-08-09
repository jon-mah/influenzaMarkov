#Compares two sequences and outputs match ratio.
def siteMatch(aminoAcid1, aminoAcid2):

    numberMatches = 0

    length = len(aminoAcid1)

    for i in range(length):
        if aminoAcid1[i] == aminoAcid2[i]:
            numberMatches += 1
    percent = numberMatches/length

    return percent

#print((siteMatch(['AGGSEDKELA', 'ACCSEDKEFA'])))
