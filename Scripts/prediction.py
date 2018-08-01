# This script predicts the next mutation of the final fasta sequence in the input list, using a Markov chain
# derived from the entire set of fasta sequences given.

from markovChain import markov_chain

# Used for mapping from basepairs into numbers.
BASEPAIRS = 'ACDEFGHIKLMNPQRSTVWY'


def prediction(amino_acids):
    markov_matrices = markov_chain(amino_acids)
    last_fasta = amino_acids[-1]
    new_fasta = ''
    for k in range(len(last_fasta)):
        last_basepair = last_fasta[k]
        last_index = BASEPAIRS.index(last_basepair)
        if sum(markov_matrices[k][last_index]) == 0:
            print(1)
            new_fasta += last_basepair
        else:
            print(2)
            m = max(markov_matrices[k][last_index])
            first_index = -1
            for i in range(len(markov_matrices[k][last_index])):
                if markov_matrices[k][last_index][i] == m:
                    first_index = i
                    break
            new_fasta += BASEPAIRS[first_index]
    return new_fasta


# Example usage
print(prediction(['ACCFSDKELF', 'ACCSEDKEFA', 'ACCREGKRFA', 'AEEGCGKRFF']))