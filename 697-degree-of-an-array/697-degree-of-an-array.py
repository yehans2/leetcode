class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {} # start, end, count
        degree = 1
        
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = {'start': index, 'end': index, 'count': 1}
            else:
                dic[num]['end'] = index
                dic[num]['count'] += 1
                degree = max(degree, dic[num]['count'])
        
        res = len(nums)
        #[1,1,1,1,1] => 5
        #[1,1,1,1,1,1,1]
        for i in dic:
            # [1,2,2,3,1] => len = 5 or len = 2
            if dic[i]['count'] == degree:
                res = min(res, dic[i]['end'] - dic[i]['start'] + 1)
        return res
