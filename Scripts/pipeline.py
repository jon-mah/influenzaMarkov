# This script executes the pipeline utilized in this project.

from prediction import prediction
from siteMatch import siteMatch
from Bio import SeqIO



def main(inputFileName):

    # Uses biopython package to read the .fasta input file and extracts
    # the record object.
    seqList = []
    for record in SeqIO.parse(inputFileName, "fasta"):
        seqList.append(str(record.seq))

    print(prediction(seqList))
    predicted = prediction(seqList)
    #Year 2017 of Subsample 0

    seqList1 = []
    for record in SeqIO.parse('..\Data\Subsample_0_PROT_2017.fasta', "fasta"):
        seqList1.append(str(record.seq))
    print(seqList1)

    print(siteMatch(predicted, seqList1))
    #print(seqList1[0][1])
main('..\Data\Subsample_0_PROT.fasta')
