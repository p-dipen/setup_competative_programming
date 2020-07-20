import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


def stepPerms(n):
    steps = [1, 2, 3]
    ways = dict()

    def climb(n, steps, ways):
        ret = 0
        for step in steps:
            if n - step == 0:
                ret += 1
            elif n - step > 0:
                if n - step not in ways:
                    ways[n - step] = climb(n - step, steps, ways)
                print('ways', ways, ways[n - step])
                ret += ways[n - step]
        return ret

    return climb(n, steps, ways)
# def stepPerms(n):
#     if n == 0 or n == 1:
#         return 1

#     if n == 2:
#         return 2

#     return stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)


s = int(input())

for s_itr in range(s):
    n = int(input())

    res = stepPerms(n)
    print(res)
