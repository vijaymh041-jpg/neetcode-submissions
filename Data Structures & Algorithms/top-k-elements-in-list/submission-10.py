from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = Counter(nums)
        result = []
        dict_keys = list(count.keys())
        dict_values = list(count.values())
        for i in range(k):
            ele = max(dict_values)
            idx = dict_values.index(ele)
            inter = dict_keys.pop(idx)
            dict_values.pop(idx)
            result.append(inter)
        return result
        