class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        dict_t = {}
        
        if len(s) != len(t):
            return False
        else:   
            for s_value,t_value in zip(s,t):
                if s_value not in dict_s:
                    dict_s[s_value] = 1
                else:
                    dict_s[s_value] += 1
                
                if t_value not in dict_t:
                    dict_t[t_value] = 1
                else:
                    dict_t[t_value] += 1
                
            if dict_s == dict_t:
                return True 
            else:
                return False