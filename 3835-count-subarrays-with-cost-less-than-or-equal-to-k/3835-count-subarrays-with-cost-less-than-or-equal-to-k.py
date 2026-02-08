class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans,l,max_q,min_q=0,0,deque(),deque()
        for i in range(len(nums)):
            while (min_q and nums[min_q[-1]]>=nums[i]): min_q.pop()
            min_q.append(i)
            while (max_q and nums[max_q[-1]]<=nums[i]): max_q.pop()
            max_q.append(i)
            while (l<=i and (nums[max_q[0]]-nums[min_q[0]])*(i+1-l)>k):
                if min_q[0]==l: min_q.popleft()
                if max_q[0]==l: max_q.popleft()
                l+=1
            ans=ans+i+1-l
        return ans