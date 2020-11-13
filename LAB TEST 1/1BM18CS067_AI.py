# Parag Gattani ||  USN - 1BM18CS067
from collections import defaultdict 

aim = int(input('Enter the aim : '))
jug1 = int(input('Enter capacity of Jug 1 : '))
jug2 = int(input('Enter capacity of Jug 2 : '))

visited = defaultdict(lambda: False) 
  
# Recursive function which prints the  
# intermediate steps to reach the final  
# solution and return boolean value  
# it returns True if solution is possible, otherwise False). 
# amt1 and amt2 are the amount of water present in both jugs at a certain point of time. 
def waterJugSolverdfs(amt1, amt2):  
  
    if (amt1 == aim and amt2 == 0): 
        print('Amount of water in Jug 1 : ',amt1, '|  Amount of water present in Jug 2 : ',amt2) 
        return True
      
    # Checks if we have already visited the 
    # combination or not. If not, then it proceeds further. 
    if visited[(amt1, amt2)] == False: 
        print('Amount of water in Jug 1 : ',amt1, '|  Amount of water present in Jug 2 : ',amt2) 
      
        # Changes the boolean value of 
        # the combination as it is visited.  
        visited[(amt1, amt2)] = True
      
        # Check for all the 6 possibilities and  
        # see if a solution is found in any one of them. 
        return (waterJugSolverdfs(0, amt2) or
                waterJugSolverdfs(amt1, 0) or
                waterJugSolverdfs(jug1, amt2) or
                waterJugSolverdfs(amt1, jug2) or
                waterJugSolverdfs(amt1 + min(amt2, (jug1-amt1)), 
                amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolverdfs(amt1 - min(amt1, (jug2-amt2)), 
                amt2 + min(amt1, (jug2-amt2))))
      
    # Return False if the combination is  
    # already visited to avoid repetition otherwise 
    # recursion will enter an infinite loop. 
    else: 
        return False

def dfs(aim,target,visited_states):
    
    if aim==target:
        return True

    
    visited_states.append(aim)
    
    adj = visited_states(aim,visited_states)
    
    for aim in adj:
        if dfs(aim,target,visited_states):
            return True
    return False

amt1 = int(input('Enter initial amount of water present in jug 1 : '))
amt2 = int(input('Enter initial amount of water present in jug 2 : '))
print('** Final State will be in Jug 1 only !! **')
print("Steps: ")

waterJugSolverdfs(amt1, amt2)