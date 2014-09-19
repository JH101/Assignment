#Jamie Hilton
#19/09/14
#Currency notes v1.1

money=int(input("Please enter the amount of money you wish to convert into coins and notes: "))

notes20 = money//20

remainder20 = money%20

notes10 = remainder20//10

remainder10 = remainder20%10

notes5 = remainder10//5

remainder5 = remainder10%5

coin2 = remainder5//2

remainder2 = remainder5%2

coin1 = remainder2//1

print("Your total notes and coins are {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins, {4} £1 coins.".format(notes20, notes10, notes5, coin2, coin1)) 
