import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def left(h,p,i):
    j = i-1
    r = 0
    while j > -1:
        if p <= h[j]:
            j-=1
            r+=1
        else:
            return r

    return r


def right(h,p,i):
    z = i+1
    r = 0
    while z < len(h):
        # print('right',h[z],p)
        if p <= h[z]:
            z+=1
            r+=1
        else:
            return r

    return r

def largestRectangle(h):
    le = len(h)
    i = 0
    rec = 0
    while i < le:
        p = h[i]
        # print('p',p)
        l = left(h,p,i)
        r = right(h,p,i)
        temp = p * (l+r+1)
        # print('temp',temp)
        if rec < temp:
            rec = temp
        i+=1

    return rec


n = int(input())

h = list(map(int, input().rstrip().split()))

result = largestRectangle(h)

print(str(result))