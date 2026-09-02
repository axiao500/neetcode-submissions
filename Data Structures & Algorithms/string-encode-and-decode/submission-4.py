class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        current_length = 0
        for i in strs:
            current_length = len(i)
            encoded_string = encoded_string + str(current_length) + "#" + i 
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_list
        

