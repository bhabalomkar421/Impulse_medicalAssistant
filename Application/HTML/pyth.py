import random

info = {}



s = "abcdefghijklnmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_password = int(input("Enter number of letters in password: "))

password ="".join(random.sample(s,len_password))
print(password)

answer = input("Do you wnat to keep this password: ")
if("yes" in answer):
	account_name = input("enter  account name: ")
	info[account_name] = password
	print(info)
else:
	print("okay")
