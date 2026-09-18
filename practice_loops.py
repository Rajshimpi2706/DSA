# Reverse a Number
# Given a positive integer N, reverse its digits. Leading zeros in the reversed number should not be printed.
# Input
# 12340
# Output
# 4321
# num = 123450
# reverse_num = int(str(num)[::-1])
# print(reverse_num)
marks = int(input("Enter a positive integer:"))
if marks <= 100 and marks >= 90 :
    print("A Grade")
elif marks <= 90 and marks >= 75 :
    print("B Grade")
elif marks <= 75 and marks >= 50 :
    print("C Grade")
elif marks <= 50 and marks >= 35 :
    print("D Grade")
else :
    print("fail") 