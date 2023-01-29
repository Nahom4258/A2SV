class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        counter = 0

        for i, char in enumerate(chars):
            if len(s) > 0:
                if char == s[len(s) - 1]:
                    counter += 1
                    if (i == len(chars) - 1 and counter != 1):
                        for digit in str(counter):
                            s.append(str(digit))
                else:
                    if counter != 1:
                        for digit in str(counter):
                            s.append(str(digit))
                    s.append(str(char))
                    counter = 1
            else:
                s.append(str(char))
                counter += 1

        chars[:len(s)] = s
        return len(s)