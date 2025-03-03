#exit var loop, who else misses exit++? You can just make the while loop stop at 8 as well, totally valid way of doing it. E.g. "while exit < 8". 
exit = 0
while exit < 10:
    exit += 1
    print(f"Int {exit}", end=" ")
    if exit == 8:
        break

print("\n")

#count evens to 100.
num = 0
while num <= 100:
    
    if (num % 2) == 0:
        print(f"{num} ", end="")
        num += 1
    else:
        num += 1
        continue
        
print("\n") 
       
#count odds t0 101, look at the lists together and go, from left to right, up and down and count to 101 with the lists. :D
for num in range(102):
    if (num % 2) == 0:
        continue
    else:
        print(f"{num} ", end="")
        
print("")

#user inputed try "except" block...
#"except" being in place of "catch" makes me irrationally angry for some reason. I want to try and catch something dang it!
exit = 0
while exit == 0:
    uNum = input("\nPlease enter any number, or type \"exit\" to exit the program: ")
    
    if uNum in ("exit", "quit"):
        break

    try:
        uNum = int(uNum)
        print("\nYou entered the number", uNum)
        
    except ValueError:
        print("That was not a number! Make sure to only type a number, no spaces, letters, or any other symbols of any kind!")
        continue
    except:
        print("There was some kind of error! Please ask your local programmer to write a bug fix for this program and commit it to the github! Otherwise, refrain from this unintended activity!")
        continue
        
#Ask for a password containing atleast one number, if not program shames user for poor password etiquette.
noNum = 0

uPass = input("Please enter a user password containing a MINIMUM of one number: ")
        
for char in uPass:               
    try:
        int(char) 
        print(f"The number {char} has been detected! We all thank you for using good password etiquette.")
        noNum = 0
        break
    except ValueError:
        noNum = 1
        continue
    
if noNum == 1:
    print("Your password did not contain a number! Shame on you for improper password etiquette!")