class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = [False]*len(strs)
        for i in range(0, len(strs)):
            if used[i] == True:
                continue
            in_list = [strs[i]]
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    in_list.append(strs[j])
                    used[j] = True
            output.append(in_list)
        return output
