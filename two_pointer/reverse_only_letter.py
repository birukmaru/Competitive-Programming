class Solution:
    def reverseOnlyLetters(self, s):
        temp = list(s)
        r = len(temp) - 1
        res = ""  

        for l in range(len(temp)):  
            if not temp[l].isalpha():
                res += temp[l]
            else:
                while not temp[r].isalpha():
                    r -= 1
                res += temp[r]
                r -= 1  
        
        return res
