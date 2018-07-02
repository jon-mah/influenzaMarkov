"""
Math 381
Triangle-Free solver

The purpose of this script is to find the maximum number of edges
for a triangle-free graph given n nodes.
"""
def main(n):

    edgeList = []
    for i in range(n):
        for j in range(i + 1, n):
            edge = str(i) + str(j)
            edgeList.append(edge)

    with open('triangleFree.lp') as f:
        for x in edgeList:
            f.write(x)

    # Look at bipartite graphs

main(4)
