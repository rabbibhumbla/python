#!/usr/bin/python3

num=int(input("enter number"))

if num%2==0:
	if num%3==0:
		print ('divisible by 3 and 2')
	else:
		print ('divisible by 2 not by 3')
else:
	if num%3==0:
		print ('divisible by 3 not by 2')
	else:
		print ('not divisible by 2 and 3 both')

