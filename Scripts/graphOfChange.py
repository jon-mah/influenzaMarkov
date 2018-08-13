from prediction import prediction
from siteMatch import siteMatch
from Bio import SeqIO
import matplotlib.pyplot as plt
import re
#from matplotlib import pylab

from scipy import stats

def graph(inputFileName):

    seqList = []
    for record in SeqIO.parse(inputFileName, "fasta"):
        seqList.append(str(record.seq))

    #print("Prediction:  " + prediction(seqList))

    f = open("..\Data\Subsample_0_PROT.fasta", "r")
    subsample = f.read()

    #Tracks amount of change relative to original 1918 sequence
    change1918Array = []
    for k in range(len(seqList)-1):
        change1918Array.append(siteMatch(seqList[0], seqList[k+1]))
        #print(change1918Array[k])

    #Tracks amount of change from year to year, e.g. 1918 to 1919, 1919 to 1920
    changePerYear = []
    for k in range(len(seqList)-1):
        changePerYear.append(siteMatch((seqList[k]), seqList[k+1]))
        #print(1 - changePerYear[k])
    predicted = prediction(seqList)

    #Year 2017 of Subsample 0
    seqList1 = []
    for record in SeqIO.parse('..\Data\Subsample_0_PROT_2017.fasta', "fasta"):
        seqList1.append(str(record.seq))

    x1 = re.findall("\d{4}_(\d{4})", subsample)
    #print(x1)

    #CHANGES PER YEAR
    x1 = list(map(int, x1))
    plt.plot(x1[1:len(x1)], changePerYear)
    plt.ylabel('Sites retained')
    plt.xlabel("Year")
    plt.title("Sites retained between consecutive data points")
    plt.show()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x1[1:len(x1)], changePerYear)
    print("Changes per year: " + str(slope) + "x + " + str(intercept))

    #CHANGE RELATIVE TO 1918
    plt.plot(x1[1:len(x1)], change1918Array)
    plt.ylabel('Amino acids sites retained relative to 1918')
    plt.xlabel("Year")
    plt.title("Site Change Over Time")
    plt.show()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x1[1:len(x1)], change1918Array)
    print("Change relative to 1918: " + str(slope) + "x + " + str(intercept))

    #print("2017 actual: " + seqList1[0])

    #print(siteMatch(predicted, seqList1[0]))

    #print(seqList1[0][1])
    #prediction()

graph('..\Data\Subsample_0_PROT.fasta')
