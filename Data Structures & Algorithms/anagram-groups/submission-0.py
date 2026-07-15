class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_out = []
        used = [False]*len(strs)
        for i in range(0,len(strs)):
            if used[i]:
                continue
            list = [strs[i]]
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    list.append(strs[j])
                    used[j] = True
            list_out.append(list)
        return list_out
