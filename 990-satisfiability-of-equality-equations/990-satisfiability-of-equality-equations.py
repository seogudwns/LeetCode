class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        word_dict = {chr(i+97):i for i in range(26)}
        dif = []
        for i in equations:
            xy = sorted([i[0],i[3]])
            if i[1] == '!':
                dif.append(xy)
            else:
                num = word_dict[xy[0]]
                chan = word_dict[xy[1]]
                for j in word_dict:
                    if word_dict[j] == chan:
                        word_dict[j] = num
            
        for i,j in dif:
            if word_dict[i] == word_dict[j]:
                return False
        
        return True

        