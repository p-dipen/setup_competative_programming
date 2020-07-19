import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')

def minimumMoves(grid, startX, startY, goalX, goalY):
    print(grid)
    return 2

n = int(input())

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

startXStartY = input().split()

startX = int(startXStartY[0])

startY = int(startXStartY[1])

goalX = int(startXStartY[2])

goalY = int(startXStartY[3])

result = minimumMoves(grid, startX, startY, goalX, goalY)

print(str(result) + '\n')
