#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.91%)
# Likes:    2699
# Dislikes: 0
# Total Accepted:    380.8K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans =""

        #枚举子串的长度 l+1
        for l in range(n):
            #枚举子串的起始位置i,这样可以通过j=i+1得到子串的结束位置
            for i in range(n):
                j = i+1
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] =True
                elif l ==1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans  = s[i:j+1] 
        return ans
        
# @lc code=end

