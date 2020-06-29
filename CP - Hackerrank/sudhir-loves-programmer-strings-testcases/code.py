import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


t = input()
arr = [0] * 27
text = list(t)


i = 0

while i < len(text):
    print('insert  ',text[i], i)
    if i + 1 < len(text):
        if text[i + 1] == '(':
            st = ''
            skip = 2
            for j in text[i + 2:]:
                skip += 1
                if j == ')':
                    break
                st += j
            arr[int(text[i])] = arr[int(text[i])] + int(st)
            i += skip
        elif i + 2 < len(text) and text[i + 2] == '#':
            skip = 3
            if i + 3 < len(text) and text[i + 3] == '(':
                skip += 1 
                index = text[i] + text[i + 1]
                st = ''
                for j in text[i + 4:]:
                    skip += 1
                    if j == ')':
                        break
                    st += j
                arr[int(index)] = arr[int(index)] + int(st)
            else:
                index = text[i] + text[i + 1]
                arr[int(index)] = arr[int(index)] + 1

            i += skip
        else:
            arr[int(text[i])] = arr[int(text[i])] + 1
            i+=1

    else:
        arr[int(text[i])] = arr[int(text[i])] + 1
        i+=1

for index, val in enumerate(arr):
    if index > 0:
        print(val)


