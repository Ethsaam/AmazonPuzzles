import numpy

'''
An N x N square is partitioned into integer-sided rectangles which do not overlap and together completely cover
the N x N square.

In the top two rows of the diagram, all 8 ways to do this for a 2 x 2 square are shown. The bottom row of the diagram
shows 2 of the 84231996 ways in which a 5x5 square may be partitioned.


In how many ways can a 7 x 7 square be partitioned?

Solution based on Sequence A116694, as presented on https://oeis.org/A116694
'''

bMap = {}
mMap = {}
aMap = {}

def MFunction(n):
    if n in mMap:
        return mMap[n];
    k = 2 ** (n - 2)
    if n == 1:
        mMap[n] = [[2]]
        return [[2]]
    else:
        m = 2 * k
        matrix = [[0 for x in range(m)] for y in range(m)]
        for i in range(m):
            for j in range(m):
                if i < k:
                    if j < k:
                        matrix[i][j] = MFunction(n - 1)[i][j]
                    else:
                        matrix[i][j] = BFunction(n - 1)[i][j - k]
                else:
                    if j < k:
                        matrix[i][j] = BFunction(n - 1)[i - k][j]
                    else:
                        matrix[i][j] = 2 * MFunction(n - 1)[i - k][j - k]
    mMap[n] = matrix
    return matrix;


def BFunction(n):
    if n in bMap:
        return bMap[n];
    k = 2 ** (n - 2)
    if n == 1:
        bMap[n] = [[1]]
        return [[1]]
    else:
        m = 2 * k
        matrix = [[0 for x in range(m)] for y in range(m)]
        for i in range(m):
            for j in range(m):
                if i < k:
                    if j < k:
                        matrix[i][j] = BFunction(n - 1)[i][j]
                    else:
                        matrix[i][j] = BFunction(n - 1)[i][j - k]
                else:
                    if j < k:
                        matrix[i][j] = BFunction(n - 1)[i - k][j]
                    else:
                        matrix[i][j] = MFunction(n - 1)[i - k][j - k]
    bMap[n] = matrix
    return matrix;


def AFunction(n, m):
    if n in aMap:
        if m in aMap[n]:
            return aMap[n][m];
    if n == 0 or m == 0:
        return 1;
    else:
        if m > n:
            if m not in aMap:
                aMap[m] = {n: AFunction(m, n)}
            return AFunction(m, n);
        else:
            allSum = 0
            matrix = numpy.linalg.matrix_power(numpy.matrix(MFunction(m), dtype='int64'), n - 1)
            for i in range(len(matrix)):
                allSum = allSum + numpy.sum(matrix[i])
            aMap[m] = {n: allSum}
            return allSum;


print AFunction(7, 7)
