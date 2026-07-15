class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        count = 0
        for i in range(0, len(nums)):
            tmp = 1
            for j in range(i+1, len(nums)):
                if s_nums[j-1]+1 == s_nums[j]:
                    tmp += 1
                elif s_nums[j-1] == s_nums[j]:
                    continue
                else:
                    break
            if count < tmp:
                count = tmp            
        return count        