class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = False
        allowed = set(['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'])
        # temp = queryIP
        if '.' in queryIP and ':' not in queryIP:
            ipv4 = True
        elif '.' not in queryIP and ':' in queryIP:
            ipv4 = False
        else:
            return 'Neither'

        def has_leading(str):
            return len(str) > 1 and str[0] == '0'

        def contains_alpha(str):
            for s in str:
                if not s.isdigit():
                    return True

            return False

        def contains_illegal_alpha(str):
            for ch in str:
                if ch not in allowed and not ch.isdigit():
                    return True

            return False

        if ipv4:
            # check the digits 0 <= num <= 255 by splitting the string using '.' delimiter
            # also check that there are no leading zeros
            temp = queryIP.split('.')
            if len(temp) != 4:
                return 'Neither'
            for val in temp:
                if contains_alpha(val) or len(val) < 1 or not (0 <= int(val) <= 255) or has_leading(val):
                    return 'Neither'
            return 'IPv4'
        else:
            # check that length of each string between ':' are 1 <= len <= 4
            temp = queryIP.split(':')
            if len(temp) != 8:
                return 'Neither'
                
            for val in temp:
                if not (1 <= len(val) <= 4) or contains_illegal_alpha(val):
                    return 'Neither'
            return 'IPv6'

        return 'Neither'