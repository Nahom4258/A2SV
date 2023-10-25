class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = set(list('aeiou'))

        ans = 0
        for i in range(n):
            ch = word[i]
            if ch in vowels:
                ans += (i+1) * (n-i)

        return ans