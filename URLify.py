class Solution:
    def replaceSpace(self, s: str ) -> str:
        s = s.strip()
        s = s.replace(" ", "%20")
        print(s)
        return s

#try another solution without strip and replace

sol = Solution()
rel = sol.replaceSpace("Mr John Smith      ")