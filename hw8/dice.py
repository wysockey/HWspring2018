#Goals
#Divide by two for every number
#every twentieth side is a loss

import random


anime1 = raw_input("What is weeb 1's  name!")

anime2 = raw_input("What is weeb 2's  name!")

 

begin = 1.0

end = 100.0 

weeb1 = (begin,end)

weeb2 = (begin,end)

weeb3 = (begin,end)

weeb4 = (begin,end)

weeb5 = (begin,end)

weeb6 = (begin,end)

weeb7 = (begin,end)

weeb8 = (begin,end)

 

score1 = 0

score2 = 0

rollresult1 = weeb1

rollresult2 = weeb2

rollresult3 = weeb3

rollresult4 = weeb4

rollresult5 = weeb5

rollresult6 = weeb6

rollresult7 = weeb7

rollresult8 = weeb8

 

def roll(begin,end):

        return random.randint(begin,end)

def RoundWinner(rollresult1,rollresult2):

        if(rollresult1 > rollresult2):

                return (anime1) + " loses this round!"

        elif(rollresult2 > rollresult1):

                return (anime2) + " loses this Round!"

        else:

                return "Tie, now Re-roll"

def GameWinner(score1,score2):

        if(score1 > score2):

                return (anime1) + " loses this game!"

        elif(score2 > score1):

                return (anime2) + " loses this game!"

        else:

                return "No winner!"

def GameOver(rollresult):
	if(rollresult = [20,40,60,80,100]):
		return "You All Lose"
	elif rollresult == 20 or rollresult == 40 or rollresult == 60 or rollresult == 80 or rollresult == 100
	if true print "Game Over"
	if false print "Game Countinues"






 
gamerun = 3

while(gamerun >= 0):

        rollresult1 = roll(begin,end)
	if(GameOver(rollresult1) == "You All Lose"):
		gamerun =-1
		print("Player 1 has lost" , rollresult," was rolled")
	
	elif(GameOver(rollresult2) ==  "You All Lose"):
		gamerun =-1
		print("Player 2 has lost", rollresult, " was rolled")

        rollresult2 = roll(begin,end)

        rollwin = RoundWinner(rollresult1,rollresult2)

        elif(rollresult1 > rollresult2):

                score1 += 1

        elif(rollresult2 > rollresult1):

                score2 += 1

        gamerun -= 1

        print(rollresult1,rollresult2,rollwin)
 

gamewin = GameWinner(score1 * 0.50 ,score2 * 0.50)
 

print(gamewin)

