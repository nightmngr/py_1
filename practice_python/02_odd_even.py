#
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#
#%%
# function for checking
def check_mod(a, b):
    if a % b == 0:
        print("ok")
    else:
        print("not ok")
#%%
# check mod 4
def check_mod_4(a):
    if a % 4 == 0:
        return True
    else:
        return False
#%%
num = int(input("first number: "))
check = int(input("second number: "))

check_mod(num, check)
if check_mod_4(num):
    print(str(num) + " is also divisible by 4.")