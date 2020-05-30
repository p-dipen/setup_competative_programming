#!/bin/python3

import math
import os
import random
import re
import sys


def getMedium(exp,index,even):
    medium = 0
    count = 0
    for i,j in enumerate(exp):
        count += j
        if count >= index:
            medium += i
            if not(even):
                break;
            else:
                if index - count == 0:
                    index += 1
                    even = False
                else:
                    medium += i
                    break;
    return medium 

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    exp = [0]*201
    noti = 0
    for i in range(0,d):
        exp[expenditure[i]] += 1

    start = 0
    end = d
    even = False
    even1 = False
    if d % 2 == 0:
        medium = d // 2
        print(medium)
        even = True
        even1 = True
    else:
        medium = int(d // 2) + 1

    while end < len(expenditure):
        print(noti)
        medi = getMedium(exp,medium,even)
        print(medi,expenditure[end])
        if even1:
            medi = medi / 2
        if expenditure[end] >= 2 * medi:
            noti += 1    
        exp[expenditure[start]] -= 1
        exp[expenditure[end]] += 1
        start += 1
        end += 1

    return noti
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
