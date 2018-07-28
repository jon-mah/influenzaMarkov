# Scripts

This is the scripts directory of `influenzaMarkov`.

*  seqOrder.py (Roughly finished)

This script takes in a sequence of `FASTA` sequences and then orders them, chronologically.

*  dnaToProt.py (Roughly finished)

This script takes in a sequence of `FASTA` sequences (nucleotides), and then translates them into amino acids. As output, it generates a `.fasta` file named `inputFile_PROT.fasta`.

*  seqDifference.py (Not started)

This script takes in two `FASTA` sequences, and notes the differences by site. I'm thinking we could do this recursively instead of having to annotate differences by hand, because that would suck.

For example, if `fastaOne` was 'FSYC' and `fastaTwo` was 'FSLC', then the difference would be `Y --> L` at index 3. This is accomplished by using a 20 x 20 matrix, where the indexing of row, column indicates a transition from 'row' to 'column'.

*   markovChain (roughly finished)

Takes sequences in and array and outputs a probability matrix. 
