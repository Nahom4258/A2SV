class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counter = [[0] * 26 for i in range(len(words))]

        for i in range(len(words)):
            for char in words[i]:
                counter[i][ord(char)-97] += 1

        ans = []

        for i in range(26):
            minim = inf
            for w in range(len(words)):
                minim = min(minim, counter[w][i])

            if minim > 0:
                char = chr(i+97)

                while minim > 0:
                    ans.append(char)
                    minim -= 1

        return ans