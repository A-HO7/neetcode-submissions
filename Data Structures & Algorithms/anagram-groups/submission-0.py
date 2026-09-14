class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashMap = {}
        index = 0
        for i in strs :
            if "".join(sorted(i)) in hashMap :
                print("".join(sorted(i)))
                result[hashMap["".join(sorted(i))]].append(i)
            else :
                result.append([i])
                hashMap["".join(sorted(i))] = index
                index +=1

        return result        