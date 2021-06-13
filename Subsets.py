
    def subsets(self, nums: List[int]) -> List[List[int]]:
      l=[[]]
      for i in nums:
        l+=[j+[i] for j in l]
      return l