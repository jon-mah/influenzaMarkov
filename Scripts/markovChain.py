import numpy as np
from aminoAcid import aminoAcids
# Returns a 20x20xnumberOfSites Markov transition matrix using the given aminoAcids.
# aminoAcids should be an ordered list of strings, each string being the entire set
# of basepairs in a single line. Then main(aminoAcids)[k][a][b] is the probability
# of the k-th amino acid site's chance of mutating from acid a to acid b.
def markov_chain(aminoAcids):
    #aminoAcids = ['ACCFSDKELA','ACCSEDKEFA','ACCREGKRFA','AEERCGKRFF'] only used as example
    j = len(aminoAcids[0])

    transitionArray = []

    for k in range(j):
        aminoAcidTransition = {}
        for i in range(len(aminoAcids)-1):
            transition = aminoAcids[i][k] + aminoAcids[i+1][k]
            if transition in aminoAcidTransition:
                aminoAcidTransition[transition] += 1
            else:
                aminoAcidTransition[transition] = 1
        transitionArray.append(aminoAcidTransition)

    letterToNumber = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11,
    'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}

    markovMatrices = np.zeros((j,21,21)) #creates a 21x21xnumberSites matrix, or 21x21x10 matrix in this case

    for site in range(j): #for each amino acid site in a sequence

        for key in transitionArray[site]:
           markovMatrices[site][letterToNumber[key[0]]][letterToNumber[key[1]]] = transitionArray[site][key]  #first letter of aa, ab, etc.

        markovMatrices = markovMatrices[:, :20, :20]
        
        for z in range(20):
            sumRow = np.sum(markovMatrices[site][z])
            if sumRow != 0:
                markovMatrices[site][z] /= sumRow
            else:
                markovMatrices[site][z] = markovMatrices[site][z]

        #print(markovMatrices[site]) prints out n 20x20 arrays, n being number of sites
    return markovMatrices


markov_chain(['ACCFSDKELA', 'CCCSEDKEFA', '-CCREGKRFA', 'AEERCGKRFF'])

# Note that you must print out a site's matrix by itself to view its entire contents,
# i.e. print(main(...)[0])
