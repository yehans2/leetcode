class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]:
                ans += roman[s[i]]
            else:
                ans -= roman[s[i]]
        ans += roman[s[len(s) - 1]]
        return ans
        