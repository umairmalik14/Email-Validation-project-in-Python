# a-z  wscube@gmail.com
# 0-9
# . _ time 1
# @ time 1
# . 2,3

import re
email_Condition = "^[a-z]+[\._]?[a-z 0-1]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email: ")

if re.search(email_Condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
