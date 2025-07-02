# Sample ( Moosali2367@gmail.com)
# a-z
# 1-9
# (. _ ) Can only be used Once
# ( @ ) Can be used Once
# ( . ) is used before "com" so be atleast 3 alphabet before ending email
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Your Email : ")
if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
