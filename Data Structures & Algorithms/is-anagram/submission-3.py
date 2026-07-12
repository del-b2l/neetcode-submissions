class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for character in s:
            if character not in s_freq:
                s_freq[character] = 0
            s_freq[character] += 1
        for character in t:
            if character not in t_freq:
                t_freq[character] = 0
            t_freq[character] += 1
        if s_freq == t_freq:
            print(s_freq, t_freq)
            return True
        return False