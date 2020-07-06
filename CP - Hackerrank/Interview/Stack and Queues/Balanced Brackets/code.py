import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def isBalanced(s):
    paried = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    d = []
    for i in s:
        if paried.get(i):
            if len(d) == 0:
                return 'NO'
            
            if d.pop() != paried.get(i):
                return 'NO'
        else:
            d.append(i)
    if len(d) > 0:
        return 'NO'
    return 'YES'

t = int(input())

for t_itr in range(t):
    s = input()

    result = isBalanced(s)

    print(result)