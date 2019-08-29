"""
This problem was asked by Amazon.

There exists a staircase with N steps,
and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number
of unique ways you can climb the staircase.
 The order of the steps matters.
 this was given to me by Daily coding problem
for the purpose of showing my coding skills
"""

def take_the_Stairs(N):# N equals the number of steps in the staircase
    if N == 1:
        return 1 #smallest case possible
    return take_the_Stairs(N-1) + take_the_Stairs(N-2)
