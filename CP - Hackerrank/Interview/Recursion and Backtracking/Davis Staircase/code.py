import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


def stepPerms(n):
    if n == 0 or n == 1:
        return 1

    if n == 2:
        return 2

    return stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)


s = int(input())

for s_itr in range(s):
    n = int(input())

    res = stepPerms(n)
    print(res)
