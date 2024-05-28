#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
class Solution:
    flag = False
    num = 0
    def minMoney(self , arr, aim: int) -> int:
        # write code here
        arr.sort(reverse= True)
        # print(arr)
        def findmin(arr,aim,sum):
            if self.flag:
                return
            if sum == aim:
                self.flag = True
                return self.num
            if sum > aim:
                return 
            for i in arr:
                self.num +=1 
                findmin(arr,aim,sum+i)
                if self.flag:
                    break
                self.num -= 1
        findmin(arr,aim,0)
        if self.flag:
            return self.num
        else:
            return -1
    
s = Solution()
res = s.minMoney([357,322,318,181,22,158,365],4976)
print(res)