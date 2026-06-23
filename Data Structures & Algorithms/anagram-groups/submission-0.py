class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for elem in strs:

            key = "".join(sorted(elem))

            if key in group:
                group[key].append(elem)
            else:
                group[key] = [elem]


        return list(group.values())