import numpy as np

aminoAcids = ['ABBSJDKELA','ACCSEDKEFA','ACCREGKRFA','AEERCGKRFF']
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

letterToNumber = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,
                  'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19}

markovMatrices = np.zeros((j,20,20)) #creates a 20x20xnumberSites matrix, or 20x20x10 matrix in this case

for site in range(j): #for each amino acid site in a sequence
    for key in transitionArray[site]:
       markovMatrices[site][letterToNumber[key[0]]][letterToNumber[key[1]]] = transitionArray[site][key]  #first letter of aa, ab, etc.
       #sum up number transitions for each row, then divide that row by sum

    for z in range(20):
        sumRow = np.sum(markovMatrices[site][z])
        if sumRow != 0:
            markovMatrices[site][z] /= sumRow
        else:
            markovMatrices[site][z] = markovMatrices[site][z]

    print(markovMatrices[site])
    print()





