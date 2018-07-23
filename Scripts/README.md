# Scripts

This is the scripts directory of `influenzaMarkov`.

*  seqOrder.py (Roughly finished)

This script takes in a sequence of `FASTA` sequences and then orders them, chronologically.

*  seqDifference.py (Not started)
This script takes in two `FASTA` sequences, and notes the differences by site.

For example, if `fastaOne` was 'FSYC' and `fastaTwo` was 'FSLC', then the difference would be `Y --> L` at index 3. This is accomplished by using a 20 x 20 matrix, where the indexing of row, column indicates a transition from 'row' to 'column'.
