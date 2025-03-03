#count down
i = 10
while i > 0:
    print(i)
    i -= 1
print("")

list = []
counter = 0

#append counter numbers to list
while counter < 5:
    counter += 1
    list.append(counter)
        
print(list)

list = []
counter = 0
for counter in range(5):
    list.append(counter)
       
print(list)

#Guessing game!
answerNum = 7
userNum = int(input("I'm thinking of a number between 1 and 10 what is it?: "))

while userNum != answerNum:
    if userNum < answerNum:
        print("Too low!")
    elif userNum > answerNum:
        print("Too high!")
        
    userNum = int(input("Nope that is the incorrect number! Please try again!: "))
    
print(f"Congrats! You guessed the number correctly, the number was {answerNum}!")

#prints user inputed string backwards!
userSent = input("Please enter a sentence with atleast 5 words in it!: ")
character = len(userSent) - 1
#backwardsList = []
backwardsSent = ""

while character >= 0:
    #backwardsList.append(userSent[character])
    backwardsSent += userSent[character]
    character -= 1
    
print(backwardsSent)    
#print(backwardsList)