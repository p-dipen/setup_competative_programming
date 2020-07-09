import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


def riddle(arr):
    n = len(arr)
    s = []
    left = [-1]*(n+1)
    right = [n]*(n+1)

    for i in range(n):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()

        if (len(s) != 0):
            left[i] = s[-1]

        s.append(i)

    while len(s) != 0:
        s.pop()

    for i in range(n-1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()

        if (len(s) != 0):
            right[i] = s[-1]

        s.append(i)
    
    ans = [0] * (n + 1) 
    
    for i in range(n):
        Len = right[i] - left[i] - 1
        ans[Len] = max(ans[Len], arr[i])
        
    for i in range(n - 1, 0, -1): 
        ans[i] = max(ans[i], ans[i + 1])

    return ans[1:n+1]


n = int(input())

h = list(map(int, input().rstrip().split()))

res = riddle(h)

print(' '.join(map(str, res)))
