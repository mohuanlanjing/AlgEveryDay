#coding: utf-8
"""
三色旗算法（要求为蓝白红排列，一次只能调换两只旗子并且要求移动次数最少）：
很通俗的做法是将三枚指针（a，b，c）中的ab指向列头，c指向列尾，通过b顺序前
进来对元素进行调换, 即b指向为红时与c交换元素，b指向蓝时与a交换元素
"""

def swap(i, j):
    tmp = j
    j = i
    i = tmp
    return i, j

def moveFlag(rope):
    """
    返回排列好的绳子，并打印每一步交互步骤
    """
    a = 0
    b = 0
    c = len(rope) - 1
    r = list(rope)
    tmp = 0
    while b <= c:
        if r[b] == 'R':
            if r[c] != 'R': # 当c不为红色时才交换
                r[b], r[c] = swap(r[b], r[c])
                print 'swap b, c, a=%s, b=%s, c-1=%s'%(a, b, c-1)
            c -= 1
        if r[b] == 'B':
            if r[a] != 'B': # 当a不为蓝色时才交换
                r[b], r[a] = swap(r[b], r[a])
                print 'swap b, a, a+1=%s, b=%s, c=%s'%(a+1, b, c)
            a += 1
        if r[b] == 'B' or r[b] == 'W':
            b += 1
            #print 'move b, a=%s, b+1=%s, c=%s'%(a, b, c)
        print ''.join(r)
    return ''.join(r)
            
if __name__ == "__main__":
    rope = 'BBRWBWR'
    moveFlag(rope)
