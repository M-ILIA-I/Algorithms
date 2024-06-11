class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Problem description:
        
        Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

        Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
        
        Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
        """
        dct = {}
        n = len(arr2)
        res = []

        for i in range(len(arr1)):
            if arr1[i] in dct:
                dct[arr1[i]] += 1
            else:
                dct[arr1[i]] = 1

        for i in range(len(arr2)):
            if arr2[i] in dct:
                while dct[arr2[i]] != 0:
                    res.append(arr2[i])
                    dct[arr2[i]] -= 1
                del dct[arr2[i]]

        dct_keys = list(dct.keys())
        dct_keys.sort()
        for i in dct_keys:
            if i in dct:
                while dct[i] != 0:
                    res.append(i)
                    dct[i] -= 1
                del dct[i]
        return res
        