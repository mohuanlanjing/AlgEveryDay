#coding: utf-8
"""
杨辉三角，在n>2时a[i][j] = a[i-1][j-1] + a[i-1][j]
"""

def pascal(n):
    """
    打印出行数为n的杨辉三角
    """
    r = [] # 总容器
    tmp = [] # 每一行的容器
    i = 0 # 行数
    for i in range(n):
        for j in range(i+1): # i行j列
            if j == 0 or j == i:  # 首尾为1
                tmp.append(1)
            else:
                tmp.append(r[i-1][j-1] + r[i-1][j])
        r.append(tmp)
        tmp = [] # 清空容器
    for i in r: #打印
        print i
            
if __name__ == "__main__":
    n = 3
    pascal(n)
