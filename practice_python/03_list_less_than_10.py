#
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#
#%%
# import libraries
import numpy as np
#%%
# list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
avg = np.average(a)
avg = round(avg,2)
#%%
#
print("The string has " + str(len(a)) + " elements and the average is " + str(avg))
print("The following numbers are lower than the average:")
#%%
# print elements that are under the average
#
for i in a:
    if i < avg:
        print(i)