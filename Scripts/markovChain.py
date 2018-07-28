import numpy as np

aminoAcids = ['abbsjdkela','accsedkefa','accregkrfa','aeercgkrff']
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

letterToNumber = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
                  'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19}

markovMatrices = np.zeros((j,20,20)) #creates a 20x20xnumberSites matrix, or 20x20x10 matrix in this case

for site in range(j):
    for key in transitionArray[site]:
       #First: make a matrix counting occurrences of switches. Then, add
       #up everything along that row to find the probability of switching.
       #markovMatrices(letterToNumber[key[0]]) =
       markovMatrices[site][letterToNumber[key[0]]][letterToNumber[key[1]]] = transitionArray[site][key]  #first letter of aa, ab, etc.
       #print(markovMatrices[site])#[siteNumber]
       #print(key)
        #print(letterToNumber[key[0]])
    #print(markovMatrices[site])
    #print()
    sum = np.sum(markovMatrices[site]) #Sums total number of transitions, then divides site by number to find probability
    markovMatrices[site] /= sum
    print(markovMatrices[site])
    print()



