#coding: utf-8
"""
骑士走棋盘,西洋棋走法(就是中国象棋的马)，然后在走的时候，对每一个
现在能走的路的下一条路所有出路进行计算，选择最少的一条路走
"""
next_move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)] # 骑士可能的下一步方向
tmp_move = []
max_x = 8
max_y = 8

def getBoard():
    rv = []
    for i in range(max_x):
        rv.append([0]*max_y)
    return rv
board = getBoard() # 获取棋盘

def possible(i, j):
    """
    判断坐标i，j有多少个可能的出口
    """
    cnt = 0
    for x, y in next_move:
        if x + i < 0 or y + j < 0 or x + i > max_x-1 or y + j > max_y-1:
            continue
        if board[x+i][y+j] == 0: # 当且仅当可能走的位置为0（即未走过）的时候, 才增加可能的出口数
            cnt += 1
            tmp_move.append((x+i, y+j))
    return cnt

def getNextTmpMove(i, j):
    # 跟possible有些重叠，但是为了好看点，将它们分开了
    rv = []
    for x, y in next_move:
        if x + i < 0 or y + j < 0 or x + i > max_x-1 or y + j > max_y-1: # 越界
            continue
        if board[x+i][y+j] == 0: # 当且仅当可能走的位置为0（即未走过）的时候, 才增加可能的出口数
            rv.append((x+i, y+j))
    return rv

def travl(i, j):
    next_move_count = [0] * 8 # 记录下一步的每一步的出口数
    board[i][j] = 1 # 立足点为第一步
    px = i # 过程中的横坐标
    py = j # 过程中的竖坐标
    tmp_move = [] # 下一步可能走的坐标容器
    next_cnt = [] # 下一步可能走的坐标的出口数量容器
    for m in range(2, max_x*max_y + 1): # 遍历棋盘, 这里指一个棋盘有max_x*max_y个格子要遍历
        tmp_move = getNextTmpMove(px, py) # 获取下一步可能走的坐标
        for i, j in tmp_move:
            next_cnt.append(possible(i, j)) # 获取每个可能走的坐标的下一步的出口数
        if not next_cnt: # 没有可能的出口数，无解
            print u'无解'
            return False
        min_cnt = min(next_cnt)  # 取最小
        next_move = tmp_move[next_cnt.index(min_cnt)] # 获取下一步走的坐标
        px, py = next_move[0], next_move[1] # 下一步的坐标
        board[px][py] = m # 记录下一步坐标是第几步
        next_cnt = []
    for i in board:
        print i
        

if __name__ == "__main__":
    i = 0
    j = 0
    travl(i, j)
