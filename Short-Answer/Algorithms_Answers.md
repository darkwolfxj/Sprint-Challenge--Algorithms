#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    looping through range n^3
    O(n^3) 

b)
    looping through range n and then looping from 0 to n by incrementing in 2n
    O(n) + O(n/2) 
    


c) 
    Starts at n, loops down to Zero, then works back up to n
    O(2n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Need to find the floor at which the least number of eggs are dropped and also the least number of eggs are broken. Loop through building height and check that 
Use one egg and test each floor until egg breaks, then return previous floor

# start at zero, loop through n
# if break = True return prev floor
def did_it_break(torf):
    torf = input("Did it break? Enter True or False")
    if torf == "True":
        return True
    else:
        return False
def egg_drop(n):
    for floor in n:
        if did_it_break == True:
            return floor - 1
