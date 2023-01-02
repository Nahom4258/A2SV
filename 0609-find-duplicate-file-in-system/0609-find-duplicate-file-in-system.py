def extract_word(x):
    ans = x.split('(')
    ans[1] = ans[1][:len(ans[1]) - 1]
    return ans

class Solution:        
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for path in paths:
            temp = path.split()
            dir_name = temp[0]
            file_content = temp[1:]

            files = list(map(extract_word, file_content))
            
            for file in files:
                _dict[file[1]].append(str(dir_name) + '/' + file[0])
            
        ans = []
        for key in _dict:
            if len(_dict[key]) > 1:
                ans.append(_dict[key])
            
        return ans