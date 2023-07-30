import math
import os
import random
import re
import sys


n = int(input().strip())
 
# l1=[2,4]
# l2=[6,8,10,12,14,16,18,20]
# if n in l1:
#     print("Not Weird")
# elif n in l2:
#     print("Weird")
# elif n>=20:
#     print("Weird")
# else:
#     print("Not Weird")
if n%2!=0:
   print("Weird")
elif n>=2 and n<=5:
    print("Not Weird")
elif n>=6 and n<=20:
    print("Weird")
elif n>20:
    print("Not Weird")
