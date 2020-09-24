#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (38.18%)
# Likes:    4949
# Dislikes: 0
# Total Accepted:    558.7K
# Total Submissions: 1.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)     #结果链表的dummy节点
        cur = dummyHead
        carry = 0
        while l1 or l2:             #只要有一个链表未结束，继续遍历
            valL1 = l1.val if l1 else 0     #结束的链表赋值0
            valL2 = l2.val if l2 else 0
            total = valL1 + valL2 + carry
            carry = total // 10             #进位处理
            cur.next = ListNode(total % 10)
            cur = cur.next                  #结果链表创建
            if l1:                          #只遍历未结束的链表，结束的上面直接赋值0
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:                       #不要忘记最后退出循环后，进位的处理
            cur.next = ListNode(carry)
        return dummyHead.next


# @lc code=end

