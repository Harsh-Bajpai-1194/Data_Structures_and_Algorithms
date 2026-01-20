class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowel_list = [ch for ch in s if ch in vowels]
        vowel_list.sort()
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[idx])
                idx += 1
            else:
                result.append(ch)
        return ''.join(result)