#task 5
# Program to find the largest of three numbers
print("Program to find the largest of three numbers")
#task5.1
# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))  
#task5.2
# Comparing the three numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
#task5.3
# Displaying the result
print("The largest number is:", largest)    
