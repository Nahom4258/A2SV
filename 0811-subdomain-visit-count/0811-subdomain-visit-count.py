class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        _dict = defaultdict(int)
        
        for cpdomain in cpdomains:
            temp = cpdomain.split()
            num = int(temp[0])
            first_point = temp[1].find('.') + 1
            second_point = temp[1].find('.', first_point + 1)
            if temp[1].count('.') == 2:
                _dict[temp[1]] += num
            if temp[1].count('.') >= 1:
                _dict[temp[1][first_point:]] += num
            _dict[temp[1][second_point + 1:]] += num
            
        ans = []
        for key in _dict:
            ans.append(str(_dict[key]) + ' ' + str(key))
            
        return ans