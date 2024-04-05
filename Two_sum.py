class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_int = []
        removed = []
        nums_copy = nums
        '''
        for i in nums_copy:
            #if len(sum_int) < 2:
            cand = i
            cand_ind = nums_copy.index(i)
            nums_copy[cand_ind] = target + 1
            if ((target-cand) in nums_copy):
                sum_int.append(cand_ind)
                sum_int.append(nums.index(target-cand))
                return sum_int
        '''
        for i in range(len(nums_copy)):
            cand = nums_copy[i]
            nums_copy[i] = 1e10
            if ((target-cand) in nums_copy):
                sum_int.append(i)
                sum_int.append(nums.index(target-cand))
                return sum_int
