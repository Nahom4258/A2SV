class Solution:
    def maxProduct(self, words: List[str]) -> int:
        encode = []
        maxim = 0
        for i in range(len(words)):
            binary = 0
            for char in words[i]:
                alpha = ord(char) - 97
                binary |= (1 << alpha)

            encode.append(binary)

        for i in range(len(encode)):
            for j in range(len(encode)):
                if i != j and not (encode[i] & encode[j]):
                    maxim = max(maxim, len(words[i]) * len(words[j]))

        return maxim