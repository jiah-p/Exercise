# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param lists ListNode类一维数组 
# @return ListNode类
#
class Solution:
    def mergeKLists(self , lists):
        # write code here
        left = 0
        right = len(lists) -1

        def mergeklist(lists,left,right):
            if left >= right:
                return 
            mid = (right + left) // 2

            mergeklist(lists,left,mid)
            mergeklist(lists,mid+1,right)

            lists[left] = merge(lists, left, right)

        def merge(lists, left, right):
            # p1 第一个位置保持较小的值
            p1 = lists[left]
            p2 = lists[right]

            if lists[left].val > lists[right].val:
                p1 = lists[right]
                p2 = lists[right]
            res = p1
            while p1 and p2:
                if p1.next.val > p2.val:
                    temp = p2
                    p2 = p2.next
                    temp.next = None
                    rec = p1.next
                    p1.next = temp
                    temp.next = rec
                p1 = p1.next

            return res
        mergeklist(lists,left,right)
        return lists[left]
    
s = Solution()
res = s.mergeKLists([{1,2},{1,4,5},{6}])

print(res)