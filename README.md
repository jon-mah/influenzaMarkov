# Math_381

## Authors (Alphabetical by Last Name))
Emily Brunelli, University of Washington

Gunnar Johnson, University of Washington

Jonathan Mah, University of Washington

## Instructor

Sean Griffin, University of Washington


## Goals and Motivations

## Organization
Subdirectories:

*  `\Scripts\`: Contains the relevant scripts and pipeline.

*  `\Manuscript\`: Contains the relevant files pertaining to the project proposal and final paper.

*  `\Data\`: Contains the data used in this analysis.

## Input data
Input: An alignment of `.fasta` sequences.

## Protocol
In terms of protocol I was thinking:
1.  Sort given alignment in chronological order.
2.  Sample or explicitly calculate difference vector (with sites as indices) between consecutive sequences (i.e., A -> A, G, C, T etc…)
3.  Calculate probability matrix from difference vectors
4.  Markov chain for each site in the protein.
Now we can iteratively "predict" evolution for each site at some future time! But probably not because evolution is messy.


## Results and Conclusions

## To-do
*  The project
*  Team-name / project name?

## References
