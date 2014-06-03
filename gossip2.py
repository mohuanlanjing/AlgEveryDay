#coding: utf-8
"""
老鼠走迷宫的py实现，老鼠依次选择上右下左的方向访问迷宫
走过的位置标记为1，如果走不通就标记成0, 这次是显示所有
迷宫路径
"""
si = 1 # 起始ij坐标
sj = 1
ei = 5 # 结束ij坐标
ej = 5
success = 0

def printMigo():
    l = []
    for i in migo:
        for j in i:
            if j == 2:
                l.append(u'■') # 一个unicode字符占两个ASCII字符位置
            if j == 1:
                l.append(u'·')
            if j == 0:
                l.append('  ')
        print ''.join(l)
        l = []

def visit(i, j):
    global migo, success
    migo[i][j] = 1 # 将所在地标志为已走
    if i == ei and j == ej: # 已到达目的地
        printMigo()
    if migo[i-1][j] == 0: # 向上走
        visit(i-1, j)
    if migo[i][j+1] == 0: # 向右走
        visit(i, j+1)
    if migo[i+1][j] == 0: # 向下走
        visit(i+1, j)
    if migo[i][j-1] == 0: # 向左走
        visit(i, j-1)
    migo[i][j] = 0 # 退格时为了不影响其他路径，将路径重新设置为0

def getMigo():
    """
    返回迷宫数组
    """
    migo = [
        [2, 2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2]
    ]
    return migo
migo = getMigo()

if __name__ == "__main__":
    visit(si, sj)

