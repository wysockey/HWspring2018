#Goals
#Divide by two for every number
#every twentieth side is a loss

import random


anime1 = raw_input("What is weeb 1's  name!")

anime2 = raw_input("What is weeb 2's  name!")

 

begin = 1.0

end = 100.0 

weeb1 = (begin * 0.50 ,end * 0.50)

weeb2 = (begin * 0.50 ,end *  0.50)

weeb3 = (begin * 0.50,end  * 0.50 )

weeb4 = (begin * 0.50 ,end  * 0.50)

weeb5 = (begin * 0.50,end * 0.50)

weeb6 = (begin * 0.50,end * 0.50)

weeb7 = (begin * 0.50,end  * 0.50)

weeb8 = (begin * 0.50,end * 0.50)

 

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

def GameOver(rollresult1,rollresult2):
	if(rollresult1 = [20,40,60,80,100]):
		return(anime1) + "You All Lose"

	elif (rollresult2 = [20,40,60,80,100]):
		return(anime2) + "You All Lose"







 
gamerun = 3

while(gamerun >= 0):

        rollresult1 = roll(begin,end)

        rollresult2 = roll(begin,end)

        rollwin = RoundWinner(rollresult1,rollresult2)

        if(rollresult1 > rollresult2):

                score1 += 1

        elif(rollresult2 > rollresult1):

                score2 += 1

        gamerun -= 1

        print(rollresult1,rollresult2,rollwin)
 

gamewin = GameWinner(score1,score2)
 

print(gamewin)

