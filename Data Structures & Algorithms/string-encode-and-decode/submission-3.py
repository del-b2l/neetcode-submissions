class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            size = 0
            for c in s:
                size += 1
            encoded_str += f'{size}#{s}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[i:i + length] 
            decoded_str.append(word)
            i = i + length
        
        return decoded_str