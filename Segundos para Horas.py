# -*- coding: utf-8 -*-

from math import floor

n = int(input())
h = floor(n/3600)
n = n%3600
m = floor(n/60)
n = n%60

print("{} : {} : {}".format(h,m,n))
