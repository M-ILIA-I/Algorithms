class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n <= 1:
            return n

        slow = 0
        fast = 0
        hs = {}
        res = 1
        while fast < n:
            if s[fast] in hs:
                res=max(res, fast-slow)
                slow = hs[s[fast]]+1
                if s[slow] == s[fast]:
                    slow = fast
                    hs[s[slow]] = slow
                else:
                    hs[s[fast]] = fast
                    fast+=1
                    
            else:
                hs[s[fast]] = fast
                fast+=1
                
                
        
        return max(res, n-slow-1)

if __name__ == "__main__":
    c =Solution()

    print(c.lengthOfLongestSubstring("aabaab!bb"))