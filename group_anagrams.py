from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        m=defaultdict(list)
        for w in strs:
            m[''.join(sorted(w))].append(w)
        return list(m.values()) 