class Solution:
  def two_sum(self, nums: List[int], target: int) -> List[int]:
    index = {}

    for i, num in enumerate(nums):
      rest = target - num

      if rest in index:
        return [index[rest], i]

      index[num] = i