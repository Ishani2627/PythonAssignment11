#Que1
print("1. find valid email address")
import re
email = input("enter an email address : ")
if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$', email):
    print("valid email address")
else:
    print("invalid email address")
print("\n")

#Que2
print("2. find valid indian phone number")
import re
phone_no = input("enter a phone number : ")
if re.match("(?:(?:\\+|0{0,2})91(\\s*[\\-]\\s*)?|[0]?)?[6789]\\d{9}", phone_no) and len(phone_no) == 13 :
    print("valid phone number")
else:
    print("invalid phone number")