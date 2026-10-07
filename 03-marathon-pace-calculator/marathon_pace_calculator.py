# Welcome to Pace Calculator for Marathon !

name=str(input("What is your name? "))
distance=int(input("Enter your desired Marathon Distance (Kms): "))
time=int(input("Enter your desired Marathon Time (Mins): "))
pace=time/distance
finishtime=time

print("Your Running Pace should be", round(pace,2),"Min/Km")
print("Your finished time should be", round(finishtime,2),"Minutes")
if pace < 4:
    print("Thats an amazing pace",name)
elif pace <= 7:
        print("Thats an strong pace",name)
else:
    print("Thats a decent pace",name)

