#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param areas int整型一维数组 
# @return int整型
#
class Solution:
    def maxArea(self , areas) -> int:
        # write code here
        res = 0
        temp = 0
        for i in range(len(areas)):
            res = max(min(areas[temp:i+1]) * (i-temp +1), res, areas[i])
            if res == areas[i]:temp = i
        return res
    

s = Solution()
res = s.maxArea([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1])
print(res)