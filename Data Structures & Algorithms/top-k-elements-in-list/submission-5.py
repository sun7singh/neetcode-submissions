class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = []
        count = Counter(nums)
        for num, freq in count.most_common(k):
            list.append(num)

        return list


