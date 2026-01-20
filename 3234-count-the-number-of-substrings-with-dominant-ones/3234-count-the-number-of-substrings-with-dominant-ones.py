class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, c in enumerate(s) if c == '0']
        zeros.append(n)
        
        res = 0
        z_ptr = 0
        
        for i in range(n):
            while z_ptr < len(zeros) - 1 and zeros[z_ptr] < i:
                z_ptr += 1
            
            res += (zeros[z_ptr] - i)
            
            for k in range(z_ptr, len(zeros) - 1):
                num_zeros = k - z_ptr + 1
                if num_zeros * num_zeros > n:
                    break
                
                curr_zero_idx = zeros[k]
                next_zero_idx = zeros[k+1]
                
                min_len = num_zeros * num_zeros + num_zeros
                min_end = i + min_len - 1
                
                lower = max(curr_zero_idx, min_end)
                upper = next_zero_idx - 1
                
                if lower <= upper:
                    res += (upper - lower + 1)
                    
        return res