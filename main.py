# Lets make a password strength analyzer
import re
print("No matter how strong is youur password , there would be someone who would be able to  crack it!\n")
print("Score<2 : Weak Password")
print("Score>2 and Score<=5 : Medium Password")
print("Score>5 : Strong Password")
print("\n")
passy=input("Enter your password:")
leny=len(passy)
score=0

# First lets work on the lenth checking...
if(leny>0 and leny<=5):
    print("Weak Password!, try increasing the length... ")
    score+=1
elif(leny>5 and leny<=8):
    print("Medium Passsword, want more security ?, try increasing length...")
    score+=2
elif(leny>8):
    score+=3
else:
    print("Invalid Input!!")

# Lowercase checking...
if(re.search('[a-z]',passy)):
    score+=1
else:
    print("Buddy! add atleast 1 lowercase letter!")

# Uppercase checking...
if(re.search('[A-Z]',passy)):
    score+=1
else:
    print("Buddy! add atleast 1 uppercase letter!")

# Numerical checking...
if(re.search('[0-9]',passy)):
    score+=1
else:
    print("Buddy! add atleast 1 numerical character!")

# Special symbol checking
if(re.search('[^A-Za-z0-9]',passy)):
    score+=1
else:
    print("Buddy! add atleast 1 special character!")

#Score checking
print(f"Your Score:{score}")
if(score>0 and score<=2):
    print("Your password strengthis weak!")
elif(score>2 and score<=5):
    print("Your password strength is medium!")
elif(score>5 and score<7):
    print("Just a little more and your password  strength wwill be high!")
elif(score>=7):
    print("Your password strength is High!")
    with open("passwords.txt","a") as f:
        f.write(passy)
        f.write("\n")
     
else:
    print("Invalid!")