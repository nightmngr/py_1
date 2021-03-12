#
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#
# finding all divisors - brute force way
# %%
# import libraries
import math as m
# %%
a = int(input("Insert number: "))
divisor_list = []
# %%
for i in range(1,m.floor(a/2)+1):
    if a % i == 0:
        divisor_list.append(i)
divisor_list.append(a)
# %%
