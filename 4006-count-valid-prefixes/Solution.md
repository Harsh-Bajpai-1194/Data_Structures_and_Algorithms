# Count Valid Prefixes (LeetCode 4006) Solution: 2ms Runtime

# Intuition

An alternating string or valid prefix requires the number of `0`s and `1`s to be as balanced as possible. A prefix can be of even or odd length:

* **Even length examples:** `"10"`, `"0101"`
* **Odd length examples:** `"101"`, `"010"`

So, we need to find a common thing in all these valid strings.
The difference between number of `0`s and the number of `1`s is less than 2 always for all the valid strings, which means: `abs(zero - one) < 2`

# Approach

1. Initialize three variables: `c` to keep track of the total count of valid prefixes, `zero` to count the occurrences of the character `'0'`, and `one` to count the occurrences of the character `'1'`.
2. Iterate through each character `i` in the input string `s` from left to right.
3. Update the frequency of the current character by incrementing `zero` if `i == '0'`, or incrementing `one` otherwise.
4. Check if the absolute difference between the counts of zeros and ones is less than 2 (`abs(zero - one) < 2`). If this condition holds true, it means the prefix is balanced, so we increment our valid prefix counter `c`.
5. After completing the iteration over the entire string, return the final count `c`.

# Complexity

* **Time complexity:** $O(N)$
* **Space complexity:** $O(1)$

# Code

```python
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c,zero,one=0,0,0
        for i in s:
            if i=='0': zero+=1
            else: one+=1
            if abs(zero-one)<2: c+=1
        return c

```

# Code Efficiency Results

![Screenshot 2026-08-01 221822.png](https://assets.leetcode.com/users/images/f23f853c-198b-4583-b514-a5b1a28c10f9_1785602931.7214441.png)

