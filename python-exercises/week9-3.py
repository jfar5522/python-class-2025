import game
import myreadfile

# file=open("WriteOutput.txt", "w")
# for line in range(1000):
#     file.write(f"This is a random number: {game.rollDice()}\n")
# file.close()

with open("WriteOutput.txt", "w") as file:
    for line in range(1000):
        file.write(f"This is a random number: {game.rollDice()}\n")

with open("sentences.txt", "a") as file:
    while(1):
        sentence = input("Please enter a sentence to add to the file: ")
        if sentence in "done, Done":
            break
        print(f"You have added {sentence}\n")
        file.write(f"{sentence}\n")

        

