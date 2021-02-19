from GameOfLife.Cell import Cell
width = 9
height = 9

arr = [Cell for i in range(width)]

for i in range(width):
    stat = True
    if i/2 == 1:
        stat = True
    else:
        stat = False
    arr[i] = Cell.__init__(arr[i], 1, 1, stat)


cell = Cell

cell.__init__(cell, 5, 7, False)


print(cell.getx(cell), cell.gety(cell), cell.getStatus(cell))

for i in range(width):
    print(arr[i].getStatus())

