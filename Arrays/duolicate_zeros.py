class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Description problem:

        Given a fixed-length integer array arr, duplicate each occurrence of zero,
        shifting the remaining elements to the right.

        Note that elements beyond the length of the original array are not written.
        Do the above modifications to the input array in place and do not return anything.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=1
            i+=1