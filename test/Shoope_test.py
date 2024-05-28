class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    
    def levelPrintTree(self, pre, mid) :
        # write code here 
        root = TreeNode(-1)
        def buildtree(root,pre,mid):
            if not pre or not mid:
                return None
            root = TreeNode(pre[0])
            ind = mid.index(pre[0])
            root.left = buildtree(root,pre[1:ind+1],mid[:ind])
            root.right = buildtree(root,pre[ind+1:],mid[ind+1:])
            return root
        root = buildtree(root,pre,mid)
        def layertravel(root):
            q = [root]
            res = []
            while q:
                temp = q.pop(0)
                res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            return res
        res = layertravel(root)
        # print(res)
        return res
        


class Solution:
    def maxSubArrSum(self, nums) :
        # write code here
        res = []
        lens = len(nums)
        for i in range(lens):
            for j in range(i+1,lens+1):
                res.append(sum(nums[i:j]))
        return max(res)
s = Solution()
res = s.maxSubArrSum([-1,2,3])
print(res)

class Solution:
    res = []
    def trunkLoad(self, w, c) :
        # write code here
        temp = [0] * (len(c)+1)
        def dfs(w,sum,c,temp):
            if sum > w:
                return 
            if sum == w:
                self.res.append(temp.copy())
                return 
            for i,weight in enumerate(c):
                if temp[i+1]:
                    return 
                temp[i+1] += 1
                dfs(w,sum+weight,c,temp)
                temp[i+1] -= 1
            return 
        dfs(w,0,c,temp)
        if not self.res:
            return -1
        m = 9999
        asns = []
        for i in self.res:
            if sum(i) < m:
                m = sum(i)
                ans = i
        return ans[1:]
s = Solution()
res = s.trunkLoad(13,[5,2,6,4,3])
print(res)