#I miss prototyping so much
#Here is where my list of prototype functions would be if I could make them: :(


#prints Hello World 10 times
def helloWorld():
    for i in range(10):
        print("Hello World")

#takes a num param and subs it by 4
def subFour(num):
    num = num - 4
    return num
    
#creats local varible     
def functionOne():
    f=99
    return f
    
def functionTwo(f):
    print(f)
    


def lSum(list):
    sum = 0
    for pos in list:
        sum += pos
        
    return sum
    
LIST = (5.00, 6.50, 7.25, 3.15)

print(lSum(LIST))

helloWorld()

print(subFour(10))
    
functionTwo(functionOne())
    


# for(i = 0; i < length(list); i++) {
    # x += list[i]
# }


# do{
# i = 0
# i++
# }
# while(i < 5)