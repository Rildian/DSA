"""two point"""
def reverseWords(s):
    
    if len(s) == 0:
        return s

    s = list(s)
    left = 0

    for right in range(len(s)):
        if s[right] == " " or right == len(s) - 1:
            
            temp_r = right - 1
            temp_l = left
            
            if right == len(s) - 1:
                temp_r = right
            
            while temp_l < temp_r:
                aux = s[temp_r]
                
                s[temp_r] = s[temp_l]
                s[temp_l] = aux

                temp_r -= 1
                temp_l += 1
            
            left = right + 1
        
    return "".join(s)
            


string = "Let's take LeetCode contest"

print(reverseWords(string))
            

        

