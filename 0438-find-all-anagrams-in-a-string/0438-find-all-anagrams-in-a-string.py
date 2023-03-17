class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        dict_p = Counter(p)
        new_str = defaultdict(int)
        ans = []

        # edge case where 'p' is greater than given string 's'
        if len_p > len_s:
            return []

        # the first sliding window
        for i in range(len_p):
            new_str[s[i]] += 1
        if new_str == dict_p:
            ans.append(0)

        # continue from the previous sliding window
        for i in range(1, len_s - len_p + 1):
            # remove previous letter
            if new_str[s[i-1]] == 1:
                del new_str[s[i-1]]
            else:
                new_str[s[i-1]] -= 1
            # add current letter
            new_str[s[i+len_p-1]] += 1

            # check new created string
            if new_str == dict_p:
                ans.append(i)

        return ans
