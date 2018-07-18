"""

The purpose of script is to align FASTA sequences from a given dataset
in chronological order.

JCM 7_18_2018
"""

import re
from Bio import SeqIO
import random
import sys

def main(inputFileName, seed):

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


    seqList = []
    # Fills subsamples with (sequencesPerYear) number of records,
    # attempting to give different sequences to each subsample.
    for year in sorted(yearDictionary.keys()):
        seqList.append(yearDictionary[year])

main(example.fasta, 0)
