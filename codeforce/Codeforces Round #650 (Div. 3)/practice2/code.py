import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def findIndex(arr, mo) -> int:
    for i, j in enumerate(arr):
        if j % 2 == mo:
            return i 

def countStep(arr):
    if len(arr) == 1:
        return -1
    cs = 0
    for i, j in enumerate(arr):
        mo = i % 2
        if not (mo == j % 2):
            swap = findIndex(arr[i + 1:], mo)
            if swap == 0:
                swap = 1
            arr[i], arr[int(swap) + i] = arr[int(swap) + i], arr[i]
            cs += 1
    return cs


t = int(input())

for t_itr in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countStep(arr)

    print(result)