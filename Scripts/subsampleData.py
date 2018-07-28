"""

The purpose of script is to subsample FASTA sequences from a given dataset,
with a relatively equal distribution across the desired range of years.
This script creates (numSubsamples) number of subsamples, each with
(sequencesPerYear) number of sequences from each year in the given
data set.

JCM 7_28_2018
"""

import re
from Bio import SeqIO
import random
import sys

# TODO: Fix templist.sort()
# In order for randomization to be reproducable, it assumes the same order of
# sequences in the input file.


def main(inputFileName, seed, sequencesPerYear, numSubsamples, firstYearOfData, lastYearOfData):
    """
    Variable Arguments:
    seed:					This is the seed which randomizes the subsampling.
    sequencesPerYear:		This integer determines the maximum number of
                            unique sequences from each year are added to
                            each subsample.
    numSubsamples:			This integer determines the number of
                            subsamples that are created.
    firstYearOfData:		This integer determines the first year (inclusive)
                            of the range from when data is subsampled.
    lastYearOfData:			This integer determines the last year (inclusive)
                            of the range from when data is subsampled.
    """
####
####
    random.seed(seed)

    yearDictionary = {}			# Maps from year to list of records

    # Example Sequence ID: ">cds_ACP44147_A/New_York/19/2009_2009/04/25_HA"
    # Captured:  ">cds_ACP44147_A/New_York/19/(2009)_(2009)/04/25_HA"
    pattern = re.compile(r"^.+(\d\d\d\d).(\d\d\d\d).+$")

    # Uses biopython package to read the .fasta input file and extracts
    # the record object, as idendtified by the year described in the
    # records ID.
    for record in SeqIO.parse(inputFileName, "fasta"):
        stringID = str(record.id)
        # Constructs a match object if the current record contains pattern.
        formattedID = pattern.match(stringID)
        if formattedID:			# Returns true if record contains pattern
            year1 = int(formattedID.group(1))
            year2 = int(formattedID.group(2))
            if year1 == year2:		# Both years must match
                if year1 >= firstYearOfData and year1 <= lastYearOfData:
                    # If a list for the associated year has already
                    # been created, appends this record to that list
                    if year1 in yearDictionary.keys():
                        yearDictionary[year1].append(record)
                    # Otherwise, initializes new list.
                    else:
                        yearDictionary[year1] = [record]

    # Randomly shuffles each list of records with respect to
    # the random seed.
    for year in yearDictionary.keys():
        tempList = yearDictionary[year]
        # tempList.sort()
        random.shuffle(tempList)

    x = []
    for num in range(0, numSubsamples):
        x.append(num)		# x = [0, 1, ..., numSubsamples]

    # range(numSubamples)

    subsampleDictionary = {}		# Maps from subsample to list of records.

    for i in x:
        subsampleDictionary['subSample_{}'.format(i)] = []

    index = 0		# Indexing used in modular cycling

    # Fills subsamples with (sequencesPerYear) number of records,
    # attempting to give different sequences to each subsample.
    for year in sorted(yearDictionary.keys()):
        yearList = yearDictionary[year]			# Reference list to year
        # Note: Modular addition of index with respect to the length
        # of the current yearList should cycle through records
        # associated with the current yearList.
        for i in x:
            subsampleList = subsampleDictionary['subSample_{}'.format(i)]
            tempSet = set()
            for j in range(0, sequencesPerYear):
                # Add "next" record from this year
                if yearList[index % len(yearList)].id not in tempSet:
                    subsampleList.append(yearList[index % len(yearList)])
                    tempSet.add(yearList[index % len(yearList)].id)
                    index += 1			# Indexing used in modular cycling

    for i in x:
        subsampleList = subsampleDictionary['subSample_{}'.format(i)]
        # Rename outputFile_0 to "subsampled_" + "inputFileName"
        outputFile_i = inputFileName.replace(".fasta","TEMP_Subsample_{}.fasta".format(i))
        with open(outputFile_i, "w") as output_handle:
            SeqIO.write(subsampleList, output_handle, "fasta")

main("H1_Human_Alignments.fasta", 0, 1, 5, 1918, 2018)
