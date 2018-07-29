import numpy as np

aminoAcids = ['ACCFSDKELA','ACCSEDKEFA','ACCREGKRFA','AEERCGKRFF']
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

print(transitionArray)

letterToNumber = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11,
                  'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19}

markovMatrices = np.zeros((j,20,20)) #creates a 20x20xnumberSites matrix, or 20x20x10 matrix in this case

for site in range(j): #for each amino acid site in a sequence
    for key in transitionArray[site]:
       markovMatrices[site][letterToNumber[key[0]]][letterToNumber[key[1]]] = transitionArray[site][key]  #first letter of aa, ab, etc.

    for z in range(20):
        sumRow = np.sum(markovMatrices[site][z])
        if sumRow != 0:
            markovMatrices[site][z] /= sumRow
        else:
            markovMatrices[site][z] = markovMatrices[site][z]

    print(markovMatrices[site])
    print()





