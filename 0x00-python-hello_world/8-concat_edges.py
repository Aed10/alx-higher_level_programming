#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(" ".join(str.split()[5:7]), end = " ")
print(" ".join([str.split()[12],str.split()[0]]))
