def split_it(string):
    """Returns a tuple. On the left, all lower case letters, 
    underlines, and dots. On the right, upper case letters, spaces, and pipes"""
    
    string_first=""
    
    string_second=""
    
    len_str=len(string) #Checks the length of str

    for char in string: #Checks every charachter
        
        underline = char == '_'
        dot = char =='.'
        space = char ==" "
        pipes = char == "|"
        
        if char.islower() or underline or dot:
            string_first += char #Saves charachter in a variable
            

        if char.isupper() or space or pipes:
            string_second += char #Saves charachter in a variable
            
    return string_first,string_second


def split_rec(string):
    """The function returns a tuple. 
    On the left, all lower case letters, underscores and dots are placed. 
    On the right upper case letters, spaces and horizontal lines are saved"""

    if string=="": #If empty, return an empty tuple
        return ('','')

    else:
    
        underline = string[0] == '_'
        dot = string[0] =='.'
        space = string[0] ==" "
        pipes = string[0] == "|"
        
        if string[0].islower() or underline or dot:
            
            split_first = string[0] 
            
            split_1,split_2 = split_rec(string[1:])#Save similar charachters 
            
            return ((split_first + split_1), split_2) #Save str in the left tuple
         
        elif string[0].isupper() or space or pipes:
            
            split_second = string[0]
            
            (split_1,split_2) = split_rec(string[1:])#Save similar charachters
            
            return (split_1, (split_second + split_2)) #Save str in the right tuple
        
        else:
            return split_rec(string[1:]) #Continue to check!
            
