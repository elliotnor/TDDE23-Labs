def interpret(seq, di):
    """The function checks if the list is TRUE or FALSE depending if its an AND / NOT / OR function""" 
    if isinstance(seq, str): #If seq is a string, the function returns retruns TRUE or FALSE. 
        if seq=='true':
            return 'true'
        elif seq=='false':
            return 'false'
        else:
            return di[seq]
      

    elif isinstance(seq, list): #If seq is a list then the function will check the length of the list and then evaluate the value        
        if len(seq)==2: #if length is two then its a NOT function. Check for nestled lists. 

            if seq[0]=='NOT':
                if interpret(seq[1], di)=='true':  #For nestled lists, run function until its a string. 
                    return 'false'
                else:
                    return 'true'

        elif len(seq)==3:     #If three, check middle value, its either AND/OR

            if seq[1]=='AND':
                if interpret(seq[0], di)==interpret(seq[2], di)=='true': 
                    return 'true'
                else:
                    return 'false'
            

            elif seq[1]=='OR':
                if interpret(seq[0], di)==interpret(seq[2], di)=='false':
                    return 'false'
                else:
                    return 'true'
