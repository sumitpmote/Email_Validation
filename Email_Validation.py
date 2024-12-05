
import re

email_condition= r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"   #Regular Expression
user_email= input("Enter Your Email: ")

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")



