import random

suits = ["clubs", "diamonds", "hearts", "spades"]

faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A","2"]

keep_going = True
cpu_score = 0
player_score = 0
ties = 0
hands = 0

for x in range(0, 28):

    my_face = random.choice(faces)
    my_suit = random.choice(suits)

    your_face = random.choice(faces)
    your_suit = random.choice(suits)

    print("I have the", my_face, "of", my_suit)
    print("You have the", your_face, "of", your_suit)

    if faces.index(my_face) > faces.index(your_face): #index tells you the number of the face
        print("I win!")
        cpu_score += 1
        cpu_score + ties
        hands += 1
    elif faces.index(my_face) < faces.index(your_face):
        print("You win!")
        player_score +=1
        player_score + ties
        hands += 1

    else:
        print("The round is a tie!")
        ties +=1
        hands += 1
        

    print("Score (Player:Computer" ,player_score, ":", cpu_score)

if player_score > cpu_score:
    print("You're currently winning!")
elif player_score == cpu_score:
    print("It's a tie.")
else:
    print("You're losing. :(")

    






                            

