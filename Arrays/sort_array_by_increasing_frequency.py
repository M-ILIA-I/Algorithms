class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Problem description:

        Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

        Return the sorted array.
        """
        cntr = Counter(nums)
        sorted_cntr = sorted(cntr.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for i in sorted_cntr:
            res += [i[0]] * i[1]    
        
        return res
