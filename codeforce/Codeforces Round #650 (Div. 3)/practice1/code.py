import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def combineString(strg):
    if len(strg) == 2:
        return strg
    arr = list(strg)
    i = 0
    rtn = ''
    while i < len(strg):
        if i == 0:
            rtn = arr[i]
            i += 1
        elif i + 1 == len(strg):
            rtn += arr[i]
            i += 1
        else:
            if arr[i] == arr[i + 1]:
                rtn += arr[i]
                i += 2
     
    return rtn


t = int(input())

for t_itr in range(t):
    n = input()

    strg = n

    result = combineString(strg)

    print(result)