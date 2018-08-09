# This script contains various functions that compute measures of variability for
# sequences of fasta data. Input is the same format as markovChain.py


# Counts the number of times each site changes from one basepair to a different one
def change_counts(amino_acids):
    num_amino_acids = len(amino_acids)
    num_base_pairs = len(amino_acids[0])

    counts = [0]*num_base_pairs
    for k in range(num_base_pairs):
        for i in range(1, num_amino_acids):
            if amino_acids[i][k] != amino_acids[i-1][k]:
                counts[k] += 1

    return counts


# Normalizes change_counts so that values are relative to 1
def change_counts_normalized(amino_acids):
    counts = change_counts(amino_acids)
    m = max(counts)
    if m == 0:
        return [0] * len(counts)
    return [x / m for x in counts]


# Counts the total number of basepairs that each site takes on
def site_range(amino_acids):
    num_base_pairs = len(amino_acids[0])

    site_array = []
    for k in range(num_base_pairs):
        site_array.append([acid[k] for acid in amino_acids])

    ret = []
    for site in site_array:
        ret.append(len(list(set(site))))

    return ret


# Normalizes site_range so that values are relative to 1
def site_range_normalized(amino_acids, inputFileName):
    ranges = site_range(amino_acids)
    m = max(ranges)
    outputFileName = inputFileName.replace('.fasta', '_variability.csv')
    with open(outputFileName, "w") as f:
        f.write('Site,Variability CLass\n')
        i = 1
        for x in ranges:
            f.write(str(i) + ',' + str(x / m) + '\n')
            i = i + 1
    return [x / m for x in ranges]

#print(site_range_normalized(['ACCFSDKELF', 'ACCSEDKEFA', 'ACCREGKRFA', 'AEEGCGKRFF']))
