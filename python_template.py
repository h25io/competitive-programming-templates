'''           Collaborative CP template by h25

  https://github.com/h25io/competitive-programming-templates

   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
  / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
 `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'''
MOD = 10 ** 9 + 7
MOD_EDU = 998244353  # Used in CodeForces educational rounds

# TODO :
### Data structures
# Graph/tree
# Segment tree
### Algorithms

def iinput():
    return int(input())

def linput():
    return list(map(int, input().split()))

def arr2d(nrows, ncols, default=0):
    return [[default for c in range(ncols)] for r in range(nrows)]

# This function handles multiple testcases and Google Code Jam formatting
def codejam():
    nTestcases = iinput()
    for testcaseId in range(1, nTestcases + 1):
        print(f'Case #{testcaseId}: ', end='')
        solve()

""" Graph section """

class MergeFind(object):
    def __init__(self):
        self.parent = collections.defaultdict(lambda: None)

    def find(self, x):
        path = []
        while x is not None:
            path.append(x)
            x = self.parent[x]
        x = path.pop()
        for e in path:
            self.parent[e] = x
        return x

    def merge(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[xroot] = yroot
        return yroot

def bfs(root, adjacencyList):
    N = len(adjacencyList)
    res = []
    q = queue.Queue()
    q.put(root)
    seen = [False] * N
    seen[root] = True

    while not q.empty():
        current = q.pop()
        res.append(current)
        for neighbour in adjacencyList[current]:
            if not seen[neighbour]:
                seen[neighbour] = True
                q.push(neighbour)
    return res

def dfs(root, adjacencyList):
    N = len(adjacencyList)
    res = []
    q = [root]
    seen = [False] * N
    seen[root] = True

    while not q.empty():
        current = q.pop()
        res.append(current)
        for neighbour in adjacencyList[current]:
            if not seen[neighbour]:
                seen[neighbour] = True
                q.append(neighbour)
    return res


""" Math section """

def fastExponentiation(n, p, mod):
    res = 1
    n %= mod
    while p > 0:
        if p & 1:
            res = (res * n) % mod
        n = (n * n) % mod
        p >>= 1
    return res

# Get a sorted list of primes up to uplimit (included).
# Takes around 50ms for primes below 1M.
def generatePrimes(uplimit):
    factors = [0] * (uplimit + 1)
    primes = [2] if uplimit >= 2 else []
    for i in range(3, uplimit + 1, 2):  # on va passer en revue tous les impairs
        if not factors[i]:
            primes.append(i)
            for j in range(3 * i, uplimit + 1,
                           i << 1):  # seuls les facteurs k*p avec p premier et k impair méritent d'être marqués
                factors[j] = 1
    return primes

def isPrime(n):
    if (n % 2 == 0 and n != 2) or n < 2:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def getDivisors(n):
    d = 1
    res = []
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            if d * d != n:
                res.append(n // d)
        d += 1
    return res

def getPrimeDivisors(n, primes=None):
    if primes is None:
        primes = generatePrimes(n)
    res = []
    for prime in primes:
        t = 0
        while n % prime == 0:
            t += 1
            n /= prime
        if (t > 0):
            res.append((prime, t))
    return res

def check_composite(n, a, d, s):
    x = fastExponentiation(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1, s):
        x = (x * x) % n;
        if x == n - 1:
            return False
    return True


def millerRabin(n, iter=5):
    if n < 4:
        return n == 2 or n == 3
    s = 0
    d = n - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for i in range(iter):
        a = 2 + random.randint(0, n - 4)
        if check_composite(n, a, d, s):
            return False
    return True


""" Matrix section """

def zeroes(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matrixAdd(a, b):
    (N, M) = (len(a), len(a[0]))
    assert len(b) == len(a) and len(b[0]) == len(a[0])
    return [[a[i][j] + b[i][j] for j in range(M)] for i in range(N)]

def matrixMul(a, b):
    (N1, M1) = (len(a), len(a[0]))
    (N2, M2) = (len(b), len(b[0]))
    assert M1 == N2
    res = [[0 for j in range(M2)] for i in range(N1)]
    for i in range(N1):
        for j in range(M2):
            for k in range(N2):
                res[i][j] += a[i][k] * b[k][j]
    return res

def scalarMul(a, n):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= n
    return a

def scalarMod(a, n):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] %= n
    return a

def fastMatrixPow(m, p, mod=None):
    (N, M) = (len(m), len(m[0]))
    assert N == M
    res = identity(len(m))
    if mod is not None:
        m = scalarMod(m, mod)
    while p > 0:
        if p & 1:
            res = matrixMul(res, m)
            if mod is not None:
                res = scalarMod(res, mod)
        m = matrixMul(m, m)
        if mod is not None:
            m = scalarMod(m, mod)
        p >>= 1
    return res


""" Misc section """

# TO CHECK
def binarySearch(predicate, lowerLimit = 0, upperLimit = 1e16, epsilon = 1e-8):
    flip = 0
    if predicate(upperLimit):
        flip = 1
    nFlip = not flip

    while abs(lowerLimit-upperLimit) > epsilon:
        mid = (lowerLimit + upperLimit) / 2
        if(predicate(mid)):
            (lowerLimit, upperLimit) = (lowerLimit*flip + mid*nFlip, upperLimit*nFlip + mid*flip)
        else:
            (lowerLimit, upperLimit) = (lowerLimit*nFlip + mid*flip, upperLimit*flip + mid*nFlip)
    return lowerLimit

def binarySearchInt(predicate, lowerLimit = 0, upperLimit = int(1e16)):
    flip = 0
    if predicate(upperLimit):
        flip = 1
    nFlip = not flip

    while lowerLimit != upperLimit:
        mid = (lowerLimit + upperLimit + nFlip) // 2
        if(predicate(mid)):
            (lowerLimit, upperLimit) = (lowerLimit*flip + mid*nFlip, upperLimit*nFlip + mid*flip)
        else:
            (lowerLimit, upperLimit) = (lowerLimit*nFlip + (mid+1)*flip, upperLimit*flip + (mid-1)*nFlip)
    return lowerLimit
'''.-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
  / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
 `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'''


### Useful imports (uncomment only when needed to save performance)

#import collections
#import fractions
#import math
#import random
#import sys
#import queue

def solve():
    print(int(input()))

if __name__ == '__main__':
    solve()
