import random

suits = ["clubs", "diamonds", "hearts", "spades"]

faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A","2"]

keep_going = True
cpu_score = 0
player_score = 0
ties = 0
hands = 0

def cardgame():

    keep_going = True
    cpu_score = 0
    player_score = 0
    ties = 0
    hands = 0

    for x in range(0, 100):
        my_face = random.choice(faces)
        my_suit = random.choice(suits)

        your_face = random.choice(faces)
        your_suit = random.choice(suits)

        print("I have the", my_face, "of", my_suit)
        print("You have the", your_face, "of", your_suit)

        if faces.index(my_face) > faces.index(your_face):    #added precedence of suits
            print("I win by greater face value!")
            cpu_score += 1
            hands += 1
        elif faces.index(my_face) < faces.index(your_face):
            print("You win by greater face value!")
            player_score += 1
            hands += 1
        elif faces.index(my_face) == faces.index(your_face) and suits.index(my_suit) > suits.index(your_suit):
            print("I win by precedence of suit!")
            cpu_score += 1
            hands += 1
        elif faces.index(my_face) == faces.index(your_face) and suits.index(my_suit) < suits.index(your_suit):
            print("You win by precedence of suit!")
            player_score += 1
            hands += 1
        elif faces.index(my_face) == faces.index(your_face) and suits.index(my_suit) == suits.index(your_suit):
            print("Tie, both face and suit values are the same!")
            ties += 1
            hands += 1
        

        print("\nScore (Player:Computer:Ties)" ,player_score, ":", cpu_score, ":", ties)
        print("Hands played so far:", hands)

        continuation = input("Deal? y/n")

        
if player_score > cpu_score:
    print("You're currently winning! :)")
elif cpu_score > player_score:
    print ("CPU is currently winning! :(")
else:
    print("Tie currently.")

continuation = input("Deal? y/n")
if continuation == "y":
    cardgame()
elif continuation == "n":
    pygame.quit()
else:
    pygame.quit()




    






                            

