# This script executes the pipeline utilized in this project.

from prediction import prediction
from siteMatch import siteMatch
from Bio import SeqIO
from variability import site_range_normalized


def main(inputFileName):

    # Uses biopython package to read the .fasta input file and extracts
    # the record object.
    seqList = []
    for record in SeqIO.parse(inputFileName, "fasta"):
        seqList.append(str(record.seq))

    print("Prediction:  " + prediction(seqList))
    predicted = prediction(seqList)
    #Year 2017 of Subsample 0

    seqList1 = []
    seq2017 = inputFileName.replace('.fasta', '_2017.fasta')
    for record in SeqIO.parse(seq2017, "fasta"):
        seqList1.append(str(record.seq))
    print("2017 actual: " + seqList1[0])

    print(siteMatch(predicted, seqList1[0]))
    #print(seqList1[0][1])
    site_range_normalized(seqList, inputFileName)

main('../Data/Subsample_0_PROT.fasta')
main('../Data/Subsample_1_PROT.fasta')
main('../Data/Subsample_2_PROT.fasta')
main('../Data/Subsample_3_PROT.fasta')
main('../Data/Subsample_4_PROT.fasta')
