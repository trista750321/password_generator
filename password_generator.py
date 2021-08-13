import random
pass_len = int(input("Please enter the length of your password "))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
result = "".join(random.sample(s, pass_len))
print(result)