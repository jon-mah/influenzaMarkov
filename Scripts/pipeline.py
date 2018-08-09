# This script executes the pipeline utilized in this project.

from prediction import prediction
from Bio import SeqIO

def main(inputFileName):

    # Uses biopython package to read the .fasta input file and extracts
    # the record object.
    seqList = []
    for record in SeqIO.parse(inputFileName, "fasta"):
        seqList.append(str(record.seq))

    print(prediction(seqList))

main('..\Data\Subsample_0_PROT.fasta')
