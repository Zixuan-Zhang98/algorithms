class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, res)
        return res
        
    def dfs(self, nums, index, res):
        if index >= len(nums) - 1:
            res.append(nums[:])
        else:
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.dfs(nums, index + 1, res)
                nums[i], nums[index] = nums[index], nums[i]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        cur = []
        self.permuteHelper(nums, cur, results)
        return results
        
    def permuteHelper(self, nums, cur, results):
        if len(cur) == len(nums):
            results.append(list(cur))
            return
        
        for i in range(len(nums)):
            if nums[i] in cur:
                continue
            else:
                cur.append(nums[i])
                self.permuteHelper(nums, cur, results)
                cur.pop()

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuting(nums, i, results):
            if i == len(nums):
                results.append(list(nums))
            else:
                for j in range(i, len(nums)):
                    nums[i], nums[j] = nums[j], nums[i]
                    permuting(nums, i + 1, results)
                    nums[i], nums[j] = nums[j], nums[i]
            
        results = []
        permuting(nums, 0, results)
        return results