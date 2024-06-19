class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem description:

        Given a string s, find the length of the longest substring without repeating characters.
        """
        n = len(s)
        if n <= 1:
            return n

        max_length, left = 0, 0
        cm = {}

        for right in range(n):
            if s[right] not in cm or cm[s[right]] < left:
                cm[s[right]] = right
                max_length = max(max_length, right-left+1)
            else:
                left = cm[s[right]] + 1
                cm[s[right]] = right
        
        return max_length

if __name__ == "__main__":
    c =Solution()
    
    print(c.lengthOfLongestSubstring("ggububgvfk"))