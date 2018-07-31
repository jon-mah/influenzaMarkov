import numpy as np
from itertools import tee


# Used for mapping from basepairs into numbers.
BASEPAIRS = 'ACDEFGHIKLMNPQRSTVWY'


# Returns (A_0, A_1), (A_1, A_2), ...
def pairwise(A):
    a, b = tee(A)
    next(b, None)
    return zip(a, b)


# Returns a 20x20xnumberOfSites Markov transition matrix using the given aminoAcids.
# aminoAcids should be an ordered list of strings, each string being the entire set
# of basepairs in a single line. Then main(aminoAcids)[k][a][b] is the probability
# of the k-th amino acid site's chance of mutating from acid a to acid b.
def main(amino_acids):
    num_base_pairs = len(amino_acids[0])
    num_amino_acids = len(amino_acids)

    # Collect each site transition into its own array
    site_array = []
    for k in range(num_base_pairs):
        site_array.append([acid[k] for acid in amino_acids])

    markov_matrices = np.zeros((num_base_pairs,20,20))

    for k in range(num_base_pairs):
        matrix = markov_matrices[k]
        pairs = pairwise(site_array[k])
        for (a,b) in pairs:
            matrix[BASEPAIRS.index(a)][BASEPAIRS.index(b)] += 1 / (num_amino_acids - 1)

    return markov_matrices


# Example usage
print(main(['ACCFSDKELA', 'ACCSEDKEFA', 'ACCREGKRFA', 'AEERCGKRFF']))
# Note that you must print out a site's matrix by itself to view its entire contents,
# i.e. print(main(...)[0])

