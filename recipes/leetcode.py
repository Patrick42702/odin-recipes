

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        
        encoded_str = ""
        
        for string in strs:
            
            encoded_str += string
            
            encoded_str += ":;"
            
        return encoded_str
        
        # write your code here

    """
    @param: str: A string
     @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        
        final_list = []
        
        temp = ""
        
        for idx,char in enumerate(str):
            
            if char == ":" and str[idx + 1] == ";":
                
                final_list.append(temp)
                
                temp = ""
                
            elif char == ";":
                
                continue
            
            else:
                
                temp += char
            
        return final_list
        
        # write your code here
    

if __name__ == "__main__":
    input = ["we", "say", ":", "yes"]
    
    sol = Solution()
    
    print(sol.encode(input))
    
    encode = sol.encode(input)
    
    decode = sol.decode(encode)
    
    print(decode)
    
    