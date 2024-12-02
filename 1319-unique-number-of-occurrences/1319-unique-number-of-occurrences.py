class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(0,len(arr)):
            if arr[i] not in count:
                count[arr[i]] = arr.count(arr[i])

        return len(count.values()) == len(set(count.values()))


