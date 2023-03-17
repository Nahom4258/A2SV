class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left_ptr, right_ptr = 0, 0
        p = dict(Counter(p))
        new_str = defaultdict(int)
        ans = []

        while right_ptr < len(s):
            # if both pointers are on the same letter
            if left_ptr == right_ptr:
                new_str = defaultdict(int)
                curr = s[right_ptr]
                # if current letter is in 'p' and needs more to equal 'p'
                if curr in p and new_str[curr] < p[curr]:
                    new_str[curr] += 1
                    if new_str == p:
                        ans.append(left_ptr)
                        new_str[curr] -= 1
                        left_ptr += 1
                    right_ptr += 1
                else:
                    left_ptr += 1
                    right_ptr += 1
                continue

            curr = s[right_ptr]
            # if current letter is in 'p' and needs more to equal 'p'
            if curr in p and new_str[curr] < p[curr]:
                new_str[curr] += 1
                if new_str == p:
                    ans.append(left_ptr)
                    new_str[s[left_ptr]] -= 1
                    left_ptr += 1
                right_ptr += 1
            else:
                new_str[s[left_ptr]] -= 1
                left_ptr += 1

        return ans
