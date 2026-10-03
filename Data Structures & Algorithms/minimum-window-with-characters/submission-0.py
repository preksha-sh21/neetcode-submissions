class Solution:
        def minWindow(self, s: str, t: str) -> str:
            left=0
            count={}
            have=0
            need={}
            min_len = float("inf")
            start=0

            for char in t:
                need[char]=need.get(char,0)+1
            for right in range(len(s)):
                if s[right] in need:
                    count[s[right]]=count.get(s[right],0)+1

                    if count[s[right]]==need[s[right]]:
                        have+=1

                        if have==len(need):
                            while have==len(need):

                                if right-left+1 < min_len:
                                    min_len=right-left+1
                                    start=left

                                if s[left] in need:
                                    count[s[left]]-=1

                                    if count[s[left]]< need[s[left]]:
                                        have-=1
                                left+=1

            if min_len==float('inf'):
                       return ""

            return s[start:start+min_len]
                                        




                
