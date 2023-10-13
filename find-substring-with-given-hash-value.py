class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = [1]
        # generating the power values as using pow(x, i) or x**i causes Time Limit Exceeded
        # now we can access the values of power**i using the array in O(1) time comp
        for _ in range(k-1):
            powers.append(powers[-1] * power)

        def val(ch):
            return ord(ch) - ord('a') + 1

        def hash(string):
            ans = 0
            for i in range(len(string)):
                ans += (val(string[i]) * (powers[i]))

            return ans

        left = 0
        right = k-1

        start = hash(s[:k])

        # check if first substring equals hashValue
        if (start%modulo) == hashValue:
            return s[:k]

        while right < len(s)-1:
            # remove previous prev_ch*power**0 and add next next_ch * power**(k-1)
            start = ((start - (val(s[left]))) // power) + (val(s[right+1])*(powers[k-1]))
            if (start%modulo) == hashValue:
                return s[left+1:right+2]

            left += 1
            right += 1

        return ''