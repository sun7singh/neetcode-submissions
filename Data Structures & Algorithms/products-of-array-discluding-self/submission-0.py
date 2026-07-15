class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            tmp = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                tmp *= nums[j]
            output.append(tmp)
        return output
