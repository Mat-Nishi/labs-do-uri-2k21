# -*- coding: utf-8 -*-

vals = []
for i in range(4):
    vals.append(float(input()))

print("Media = {:.2f}".format(sum(vals)/4))
