#handling input as string for namee
name = input("Enter student name")

#recieving input of marks between 0 to 100
marks = int(input("Enter your marks"))

#Executing the if else conditional statements
if(marks >= 90):
    print("A+")
elif(marks >=80 and marks < 90):
    print("A")
elif(marks >=70 and marks < 80):
    print("B")
elif(marks >= 60 and marks < 70):
    print("C")
elif(marks >= 50 and marks < 60):
    print("D")
elif(marks >=40 and marks < 50):
    print("E")
else:
    print("Fail")

#using while conditional loop
while True:
    if(marks < 40):
      print("you have failed")
    else:
        print("Congratulations on passing the exam")
    break

#using function as a message to user
def message():
    if(marks >= 80):
        print("Message: You are outstanding performer")
    elif(marks >= 60 and marks <80):
        print("Message: very good! keep it up!")
    else:
        print("Message: Good work!! better can be made")
    
#calling the function
message()

