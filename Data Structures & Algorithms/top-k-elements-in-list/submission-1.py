class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Safely count frequencies
        counts = {}
        for num in nums:
            # .get(num, 0) returns 0 if the key doesn't exist yet
            counts[num] = counts.get(num, 0) + 1
            
        # 2. Sort the dictionary by values in DESCENDING order
        # .items() gives us a list of (key, value) pairs. 
        # key=lambda x: x[1] tells Python to sort based on the value (index 1).
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Extract the top 'k' numbers
        res = []
        for i in range(k):
            # We append x[0] because index 0 is the actual number
            res.append(sorted_items[i][0])
            
        return res