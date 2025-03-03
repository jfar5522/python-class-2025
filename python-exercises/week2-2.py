#creates multiple "num" varibles with their respective number meaning their assigned int value. It then prints out the varibles individually.
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)

#creates multiple "float" variables with their respective number meaning their assigned float value. It then prints out the varibles individually.
float1, float2, float3, float4, float5, float6, float7, float8, float9, float10 = 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.12
print(float1, float2, float3, float4, float5, float6, float7, float8, float9, float10)

#creates multiple "string" variables with their respective number meaning their assigned string. It then prints out the varibles individually.
string1, string2, string3, string4, string5, string6, string7, string8, string9, string10 = "string1", "string2", "string3", "string4", "string5", "string6", "string7", "string8", "string9", "string10"
print(string1, string2, string3, string4, string5, string6, string7, string8, string9, string10)

#creates then combines and prints the following variables.
years, since = "Many years have passed", " since I was born."
print(years + since)

#creates base varibles for future use.
myName = "Barbara"
bankAccount = 155

#creates person var with string statement which references earlier base vars "myName" and "bankAccount".
person = "I am %s and my bank account has $%d in it."%(myName,bankAccount)
print(person) 

#creates 2 vars which are then printed out with a string statement attached.
myProf, profMoney = "Professor", 14
print("My %s has $%d in his pocket."%(myProf,profMoney))

#assigns previously made variable with float value which then prints with another string attached.
profMoney = 14.32
print("My %s has $%.2f in his pocket."%(myProf, profMoney))

#assigns constant "PIE" which then prints up to 5 decimal places of PIE with string attached.
PIE = 3.1415926
print("Pie has the value %.5f in it"%(PIE))

#creates and assigns two vars which are then attached to a string and then printed. 
accountAmount, accountNumber = 845.65, "032410"
print("A bank account with the number %s has $%0.2f in it"%(accountNumber, accountAmount))
