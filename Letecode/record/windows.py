from collections import deque
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @param size int整型 
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self , num, size: int):
        # write code here
        ans = []
        q = deque()
        for i, x in enumerate(num):
            # 入
            while q and num[q[-1]] <= x:
                q.pop()
                print(q)
            q.append(i)
            # 出
            if i-q[0] >= size:
                q.popleft()
            # 记录
            if i >= size - 1:
                ans.append(num[q[0]]) 

        return ans
    
s = Solution()
res = s.maxInWindows([2,1,3,5,3],3)