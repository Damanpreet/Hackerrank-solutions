#!/usr/bin/python

# Head ends here

import math
from operator import itemgetter
def next_move(posr, posc, board):
    dirty_pos = []
    dirty_dis = []
    
    for index, row in enumerate(board):
        if 'd' in row:
            dirty_y = [i for i, val in enumerate(row) if val == 'd']
            for d in dirty_y:
                pos_d = (index, d)
                dirty_pos.append(pos_d)
            
    for each_pos in dirty_pos:
        dirty_dis.append(math.sqrt((each_pos[0]-posr)**2 +  (each_pos[1]-posc)**2))
        
    while len(dirty_dis) > 0:
        min_pos = min(enumerate(dirty_dis), key=itemgetter(1))[0]
        target = dirty_pos[min_pos]

        x = posr - target[0]
        y = posc - target[1]
        if x==0 and y==0: # if bot is at dirty location
            print('CLEAN')
        else:
            print(''.join(['DOWN\n'*abs(x) if x<0 else 'UP\n'*abs(x),'RIGHT\n'*abs(y) if y<0 else 'LEFT\n'*abs(y), 'CLEAN']))
        
        # updating bot position
        posr = target[0]
        posc = target[1]
        
        del(dirty_dis[min_pos]) 
        del(dirty_pos[min_pos])
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)