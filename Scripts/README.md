# Scripts

This is the scripts directory of `influenzaMarkov`.

*  dnaToProt.py

This script takes in a sequence of `FASTA` sequences (nucleotides), and then translates them into amino acids. As output, it generates a `.fasta` file named `inputFile_PROT.fasta`.

*  label_HA.py

**This script must be run from the PyMOL interface.** It can be used to generate three-dimensional models of the variation in our data sets, as well as model the known epitope locations from literature.

*  markovChain.py

This script constructs a transition matrix of amino-acid substitution probabilities for use in a Markov chain.

*  **pipeline.py**

**If you want to recreate our analysis, run this script from the command line. You need to have the BioPython package installed.**

*  seqOrder.py

This script takes in a sequence of `FASTA` sequences and then orders them, chronologically.

*  siteMatch.py

This script compares the percentage of matching sites between two sequences. It's used to calculate the accuracy of predictions compared to actual sequences.

*  subsampleData.py

This script generates random subsamples of FASTA sequences.

*  variability.py

This script contains various functions that compute measures of variability for sequences of FASTA data. The required input is the same format as markovChain.py
