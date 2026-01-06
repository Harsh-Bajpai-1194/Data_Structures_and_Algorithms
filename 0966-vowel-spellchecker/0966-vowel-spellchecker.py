class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)  
        case_map,vowel_map={},{}
        def devowel(word): return ''.join('*' if ch in 'aeiou' else ch for ch in word)
        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word
            dv = devowel(lower)
            if dv not in vowel_map: vowel_map[dv] = word
        result = []
        for q in queries:
            if q in word_set: result.append(q)
            elif q.lower() in case_map: result.append(case_map[q.lower()])
            elif devowel(q.lower()) in vowel_map: result.append(vowel_map[devowel(q.lower())])
            else: result.append("")
        return result