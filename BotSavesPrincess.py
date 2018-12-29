#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    count = 0
    for index, row in enumerate(grid):
        if 'm' in row:
            pos_m = (index, row.index('m'))
            count += 1
        if 'p' in row:
            pos_p = (index, row.index('p'))
            count += 1
        if count == 2:
            break
    x = pos_m[0] - pos_p[0] 
    y = pos_m[1] - pos_p[1]
    print(''.join(['DOWN\n' * abs(x) if x<0 else 'UP\n' * abs(x), 'RIGHT\n' * abs(y) if y<0 else 'LEFT\n' * abs(y)]))
            

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())


displayPathtoPrincess(m,grid)