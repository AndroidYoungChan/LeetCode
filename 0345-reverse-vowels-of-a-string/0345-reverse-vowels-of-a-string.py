import copy
class Solution:
    def reverseVowels(self, s: str) -> str:
        k = copy.deepcopy(s)
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        box = []
        temp =''
        for i in range(len(s)):
            if s[i] in vowels:
                box.append(i)
        if len(box) == 0:
            return k
        if len(s) == 1:
            return k
        elif len(s) == 2 and len(box)==2:
            s[0], s[1] = s[1], s[0]
        elif len(s) == 2 and len(box)!=2:
            return k
        else:
            for i in range(len(box)//2):
                s[box[i]], s[box[-1-i]] = s[box[-1-i]], s[box[i]]
     
        return "".join(s)