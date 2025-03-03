#creates string constant "WEEK" which is assigned the days of the week. Prints Tuesday, Wednesday, Friday, then Saturday.
WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(WEEK[1])
print(WEEK[2])
print(WEEK[4])
print(WEEK[6])

#creates dictionary of student accounts with student ID's attached to each account. Then prints two of those dictionaries out.
students = {123456:"u123456@utah.edu", 223456:"u223456@utah.edu", 323456:"u323456@utah.edu", 456789:"u456789@utah.edu", 567890:"u567890@utah.edu"}
print(students[123456])
print(students[567890])

#creats a dictionary of strings and ID numbers that connect eachother respectively, e.g 1 is "one". Checks for 7 for printing, however, there is no 7 in the dictionary so it prints out an error statment for user.
test = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}
print(test.get(7, "THERE IS NO SEVEN"))

#creats seperate dictionaries so we can update the second one with all non same values as the first one.
dic1 = {1:"one", 2:"two", 3:"three"}
dic2 = {3:"three", 4:"four", 5:"five"}
dic2.update(dic1)
print(dic2)

#creates a dictionary then assigns ids with blank strings.
studentDic = {}
studentDic[14235] = " "
studentDic[384829] = " "

#creats array list containing personal info for alice and mark, then assigns the previous blank dictionary ids with the alice and mark arrays.
alice = ["Alice", 20, 80420, "Undergrade"]
mark = ["Mark", 24, 80120, "Graduate"]
studentDic[14235] = alice
studentDic[384829] = mark

#prints alice's and mark's zip codes from the array under the dictonary ids.
print(studentDic.get(14235)[2])
print(studentDic.get(384829)[2])