"""
The purpose of this script is to translate fasta files
from nucleotides to codons.
JCM 7/25/2018
"""

import glob
def main(inputFileName):
    aaDict = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
              'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
              'tta': 'L', 'tca': 'S', 'taa': 'Stop', 'tga': 'Stop',
              'ttg': 'L', 'tcg': 'S', 'tag': 'Stop', 'tgg': 'W',
              'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
              'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
              'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
              'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
              'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
              'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
              'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
              'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
              'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
              'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
              'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
              'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G',
              '---': '?'}
    output = inputFileName[:-6] + '_PROT' + inputFileName[-6:]
    with open(inputFileName, "r") as input:
        with open(output, "w") as f:
            for line in input:
                if (line[0] is '>'):
                    f.write(line)
                else:
                    line = line.lower()
                    siteNum = int(len(line) / 3)
                    for i in range(0, siteNum):
                        index = i * 3
                        codon = line[index] + line[index + 1] + line[index + 2]
                        f.write(aaDict[codon])

                    f.write('\n')

main('../Data/example_Influenza_ordered.fasta')
