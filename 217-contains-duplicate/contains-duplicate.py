class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A set stores only unique elements
        seen = set()
        
        for n in nums:
            # If the number is already in the set, we found a duplicate
            if n in seen:
                return True
            # Otherwise, add it to the set and keep looking
            seen.add(n)
            
        return False