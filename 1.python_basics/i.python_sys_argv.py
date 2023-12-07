# 
# range(start, stop, step)
# istart 	Optional. An integer number specifying at which position to start. Default is 0
# 

import sys

print("\nArguments passed:", sys.argv )
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
#type of sys.argv
print(type(sys.argv))
# Arguments passed
print("\nName of Python script:", sys.argv[0])

for i in range(1, n):
    print(sys.argv[i])

# Addition of numbers
sum_val = 0
for i in range(1, n):
  sum_val = sum_val + int(sys.argv[i])

print("\n\nResult:", sum_val)