#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
import re
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
# class Solution:
#     def solve(self , s: str) -> int:
#         # write code here
#         op = set({'+','*','-','(',')'})
#         temp = ''
#         ls = []
#         for i in s:
#             if i in op:
#                 if temp != '':
#                     ls.append(temp)
#                 temp = ''
#                 ls.append(i)
#             else:
#                 temp += i
#         if temp != '':
#             ls.append(temp)
#         def cal(s):
#             num = []
#             op_set = {'+':0,'-':0,'*':1}
#             op = []
#             while s:
#                 temp = s.pop(0)
#                 if temp not in op_set:
#                     num.append(int(temp))
#                 else:
#                     if op and op_set[temp] > op_set[op[-1]]:
#                         r = int(s.pop(0))
#                         l = num.pop()
#                         t = r*l
#                         num.append(t)
#                     elif op:
#                         r = int(s.pop(0))
#                         l = num.pop()
#                         if temp == '+':
#                             num.append(l+r)
#                         if temp == '-':
#                             num.append(l-r)
#                         else:
#                             num.append(l*r)
#                     else:
#                         op.append(temp)
#             if op[0] == '*':
#                 return num[0] * num[1]
#             elif op[0] == '+':
#                 return num[0] + num[1]
#             elif op[0] == '-':
#                 return num[0] - num[1]

  
#         s1 = []
#         s2 = []
#         while ls:
#             temp = ls.pop(0)
#             if temp == ')':
#                 p = s1.pop()
#                 while p != '(':
#                     s2.append(p)
#                     p = s1.pop()
#                 s2.reverse()
#                 s1.append(cal(s2))
#             else:
#                 s1.append(temp)
#         return cal(s1)
# 需要对比下 哪里没考虑进去


class Solution:
    def solve(self , s ):
        # write code here
        s = s.strip()
        stack = []
        res = 0
        number = 0
        sign = '+'
        
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index] == '(':
                end = index + 1
                lens = 1
                while lens > 0:
                    if s[end] == '(':
                        lens += 1
                    if s[end] == ')':
                        lens -= 1
                    end += 1
                number = self.solve(s[index + 1: end - 1])
                index = end - 1
                continue
            if '0' <= s[index] <= '9':
                number = number * 10 + int(s[index])
            if not '0' <= s[index] <= '9' or index == len(s) - 1:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-1 * number)
                elif sign == '*':
                    stack.append(stack.pop() * number)
                elif sign == '/':
                    stack.append(stack.pop() / number)
                number = 0
                sign = s[index]
            index += 1
        
        while stack:
            res += stack.pop()
        return res