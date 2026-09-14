class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums :
            if i in hashMap :
                hashMap[i]+=1
            else :
                hashMap[i] = 1
        return sorted(hashMap.keys(), key=hashMap.get)[-k:]