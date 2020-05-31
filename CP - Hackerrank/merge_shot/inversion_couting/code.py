import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')    

def countInversions(arr):
    if len(arr) == 1:
        return 0
    else:

        r = len(arr)//2
        L = arr[:r]
        M = arr[r:]

        inL = countInversions(L)
        inM = countInversions(M)

        i = j = k = 0
        inversion = 0 + inL + inM 
        while i < len(L) and j < len(M):
            if L[i] <= M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
                inversion += (len(L) - i)
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
        
    return inversion


t = int(input())

for t_itr in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countInversions(arr)

    print('result',result,arr)