#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr) -> int:
        # write code here
        # viw = set()
        temp = []
        res = []
        for i in arr:
            if i not in temp:
                temp.append(i)
            else:
                res.append(temp.copy())
                index = temp.index(i)
                temp = temp[index:]
        if temp:
            res.append(temp.copy())
        maxi = max([len(i) for i in res])
        return maxi
s = Solution()
res = s.maxLength([2,2,3,4,3])
print(res)
