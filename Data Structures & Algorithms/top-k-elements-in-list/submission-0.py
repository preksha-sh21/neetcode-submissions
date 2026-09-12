class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        sorted_dict=sorted(dict,key=dict.get,reverse=True)

        return sorted_dict[:k]