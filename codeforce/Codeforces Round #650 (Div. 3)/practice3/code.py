import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

import math

def countSpace(tab, k):
    arr = list(tab)
    check = set(tab)
    if len(check) == 1:
        val = int(check.pop())
        if val == 0:
            if len(arr) == 1 or len(arr) <= k:
                return 1
                
            leng = len(arr)
            if leng % 2 > 0:
                leng += 1
            # print('leng',leng)
            return int(leng / (k+1))
        else:
            return 0
    else:
        arrb = list()
        leng = len(arr)
        if leng % 2 > 0:
            leng += 1

        ja = 0
        for i, j in enumerate(arr):
            if j == '1':
                arrb.append(i)

        sorted(arrb)
        h = int(leng / (k + 1)) - len(arrb)
        # print(h)
        # print('arrb',arrb)
        n = 0
        while n + 1 < len(arrb):
            su = arrb[n + 1] - arrb[n]
            mo = int(su % k)
            n += 1
            if mo > 0:
                a = int(math.ceil(su) / (k + 1)) - mo
                # print(a,su,mo)
                if a == 0:
                    if n + 2 >= len(arrb) and ja == 0:
                        return 0
                else:
                    ja += a
        # print(ja,h)
        if ja > 0:
            h = ja
    return h
    


t = int(input())

for t_itr in range(t):
    n = list(map(int, input().rstrip().split()))

    tab = input()

    result = countSpace(tab,n[1])

    print(result)