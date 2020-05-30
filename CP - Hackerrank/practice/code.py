import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def countInversions(arr):
    swapCount = 0
    i = 0
    while i < len(arr) - 1:
        ni = i + 1
        if arr[i] > arr[ni]:
            print('swap',arr[i],arr[ni])
            print('arr',arr)
            arr[i],arr[ni] = arr[ni],arr[i]
            swapCount += 1
            print('afterarr',arr)
            if i > 0:
                i -= 1

        else:
            i += 1

    return swapCount


t = int(input())

for t_itr in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countInversions(arr)

    print('result',result)