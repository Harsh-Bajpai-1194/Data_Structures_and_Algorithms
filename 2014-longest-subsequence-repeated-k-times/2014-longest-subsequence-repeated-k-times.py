from collections import deque
class Solution(object):  
    def longestSubsequenceRepeatedK(self, s, k):  
        counts = {}  
        for char in s:  
            counts[char] = counts.get(char, 0) + 1

        possible_chars = [char for char, count in counts.items() if count >= k]  
        possible_chars.sort(reverse=True)

        q = deque([""])  
        ans = ""

        def is_subsequence(subsequence, full_string, k_times):  
            k_string = subsequence * k_times  
            i = 0  
            j = 0  
            while i < len(full_string) and j < len(k_string):  
                if full_string[i] == k_string[j]:  
                    j += 1  
                i += 1  
            return j == len(k_string)

        while q:  
            subsequence = q.popleft()

            if len(subsequence) > len(ans):  
                ans = subsequence  
            elif len(subsequence) == len(ans) and subsequence > ans:  
                ans = subsequence

            for char in possible_chars:  
                new_subsequence = subsequence + char  
                if is_subsequence(new_subsequence, s, k):  
                    q.append(new_subsequence)

        return ans