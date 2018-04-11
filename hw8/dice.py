#Dice.py
''''
Create a dice rolling game. The game has players take turns rolling a 6 sided dice
, where the higher number is the winner of the round. The game is won by best 2 of 3 matches.

Implement the following functions:

roll
-Parameters: beginning, end
-Returns: an integer between beginning and end 
determineWinnerRound
-Parameters: rollresult1, rollresult2
-Returns: the name of the player that won the round
determineWinnerGame
-Parameters:score1,score2
-Returns: the name of the player that won the game, if any
''''




[1,6]
x = int(raw_input("enter a number"))
y = 10


print(x,y)
#swaps
def swap(first,second):
        z = first
        first = second
        second = z


#endswap
swap(x,y)

print (x,y)



import swap

ten=10
fifteen=15
print(x,y)
print(swap.swap(x,y))


nums = [1,2,3,4,5,6]
x= 0
while(x < len(nums)):
        print(x,nums[x])
        x = x+1
        if(num[x]>num[x+1]):
                swap.swap(num[x],num[x+1])



print(nums)
print(nums)
print(nums)
