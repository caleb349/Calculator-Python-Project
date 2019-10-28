#!/usr/bin/en python3
# -*- coding: utf-8 -*-
"""
#title: Exercise 4

@desc: This is a Python program that allows users 
to guess words from a book title of their choosing. 

@created:  sun jan 20 18:15:11 2019
@author:   Caleb obi
@course:   Introduction to programming
@univ:     Wayne state University
@assign:   Exercise 4 (Caculator)
@pyVerrsion: 3.7x
"""
import datetime
# declare variables

# Get todays's date fromt the datetime library i imported above
currentDate = datetime.date.today()
currentYear = currentDate.year # # I am using the CurrentDate value and...
# extracting the year; We can access the day, month and year with attributes:
# currentDate.day   currentDate.month   currentDate.year

# Here i will print out a welcome message for my Guessing game  to the user
# What the progam is doing and what to expect 
print("\n"*3) # for new lines
print("*"*72) # asterisks
# Python program that allows users to input two numbers, choose a mathematical operator, 
# and return the results of the calculation. 
print("\n"*2)
 

# A user defined function that accepts two numbers
def add(A, B):
   return A + B

# A user defined function that subtracts two numbers
def subtract(A, B):
   return A - B

# A user defined function that multiply two numbers
def multiply(A, B):
   return A * B

# # A user defined function that Divide two numbers
def divide(A, B):
   return A / B 
print("\n"*2) 
# Describe Application to the user 
print("Select the type of operation you want to use")
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division") 
# prompt user for response
choice1 = input("chose what operation(1,2,3,4): ")
# Ask user for numbers
num1 = int(input("Enter first number: "))
while num1 > 100000000000000:
   print("number is too big try a smaller number! ")
   break

num2 = int(input("Enter second number: "))
print("\n"*1)

if choice1 == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice1 == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice1 == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice1 == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")    

