class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        Problem description:

        You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

        The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

        You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

        Notes:

        Elements with the same mapped values should appear in the same relative order as in the input.
        The elements of nums should only be sorted based on their mapped values and not be replaced by them.
        """
        def get_mapped_value(num: int) -> int:
            mapped_num_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num_str)
        mapped_values = [(num, get_mapped_value(num)) for num in nums]
        mapped_values.sort(key=lambda x: x[1])
        return [num for num, _ in mapped_values] 