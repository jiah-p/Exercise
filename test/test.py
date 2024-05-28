
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 层序打印二叉树
# @param pre int整型 一维数组 前序遍历数组
# @param mid int整型 一维数组 中序遍历数组
# @return int整型一维数组
#
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
        
s = Solution()
res = s.levelPrintTree([1,2,3,4,5],[2,1,4,3,5])
print(res)