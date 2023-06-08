class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def is_valid(string):
            for num in ''.join(string).split('.'):
                if not num or int(num) > 255 or int(num) < 0 or len(str(int(num))) != len(num):
                    return False
            return True

        def place(at, string):
            ret = []
            for i in range(len(string)):
                if at == i:
                    ret.append('.')

                ret.append(string[i])
            return ret

        def place_dots(string, point):
            if point > 2:
                # print('ip add: ', ''.join(string))
                if is_valid(string):
                    ans.append(''.join(string))
                return

            if point == 0:
                for i in range(1, len(s)):
                    place_dots(place(i, string), point+1)
            else:
                for i in range(''.join(string).rfind('.')+1, len(s)+point):
                    place_dots(place(i, string), point+1)

            return

        place_dots(list(s), 0)
        # print('asn: ', ans)

        return ans