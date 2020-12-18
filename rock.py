def check(choice1 , choice2):    
    if choice1 == 'r' and choice2 == 'r':
        return "Tie"
        
    if choice1 == 'r' and choice2 == 'p':
        return "Player 2 won"
        
    if choice1 == 'r' and choice2 == 's':
        return "Player 1 won" 
    
        
    if choice1 == 'p' and choice2 == 'r':
        return "Player 1 won"
        
    if choice1 == 'p' and choice2 == 'p':
        return "Tie"
        
    if choice1 == 'p' and choice2 == 's':
        return "Player 2 won" 
        
    
    if choice1 == 's' and choice2 == 'r':
        return "Player 2 won"
        
    if choice1 == 's' and choice2 == 'p':
        return "Player 1 won"
        
    if choice1 == 's' and choice2 == 's':
        return "Tie" 