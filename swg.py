import random
import time
print("Let's Start the game.")
print("Time:",time.asctime(time.localtime(time.time())))
game=["snake","water","gun"]
you=0;
comp=0;
while(True):
    you1 = [];
    comp1 = [];
    your = input("Enter your choice between 0 and 2 [0 for snake,1 for water,2 for gun]:")
    try:
        if (int(your) > 2 or int(your) < 0):
            print("Invalid choice.Try Again.")
            continue

        you1.append(game[int(your)])
        print("You have",game[int(your)])
        compu = random.choice(game)
        comp1.append((compu))
        print("Computer has", compu)
        if ((you1 == ["snake"] and comp1 == ["water"]) or (you1 == ["gun"] and comp1 == ["snake"]) or
                (you1 == ["water"] and comp1 == ["gun"])):
            you = you + 1;
            print("You get a point")
        elif ((comp1 == ["snake"] and you1 == ["water"]) or (comp1 == ["gun"] and you1 == ["snake"]) or
              (comp1 == ["water"] and you1 == ["gun"])):
            comp = comp + 1;
            print("Computer get a point")
        if (you == 10):
            print("You won.")
            print("Your point:", you)
            print("Computer point:", comp)
            break;
        elif (comp == 10):
            print("Computer won.")
            print("Your point:", you)
            print("Computer point:", comp)
            break;
        else:
            print("Your point:", you)
            print("Computer point:", comp)
    except ValueError as e:
        print("Invalid input.Try Again.")
        continue

