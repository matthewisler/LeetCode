class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_ptr = 0
        end_ptr = len(numbers) - 1
        while start_ptr < end_ptr:
            total = numbers[start_ptr] + numbers[end_ptr]

            if total == target:
                return [start_ptr + 1, end_ptr + 1]
            elif total > target:
                end_ptr -= 1
            else:
                start_ptr += 1
                
