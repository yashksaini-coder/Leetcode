from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        count = Counter(arr)
        unique = len(count)

        count_array = [0] * 100000
        for key in count:
            key_count = count[key]
            count_array[key_count] += 1

        for i in range(1, 100000):
            if count_array[i] != 0:
                remove = k // i
                if remove == 0:
                    break
                else:
                    remove = min(remove, count_array[i])
                    unique -= remove
                    k -= remove * i

        return unique

sol = Solution()
arr1, k1 = [5, 5, 4], 1
arr2, k2 = [4, 3, 1, 1, 3, 3, 2], 3

print(sol.findLeastNumOfUniqueInts(arr1, k1))  # Output: 1
print(sol.findLeastNumOfUniqueInts(arr2, k2))  # Output: 2
