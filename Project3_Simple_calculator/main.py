#project-3
#Simple Calculator


#Step1 :- Get User INput For Two Numbers
number_1 = float(input("Enter your First Number :- "))
number_2 = float(input("Enter Your Second Number :- "))

#Step2 :- Perform arthemetic operations

Addition = number_1 + number_2
Subtraction = number_1 - number_2
Multiplication = number_1 * number_2
Division = number_1 / number_2


#Step3 :- Display the result
print(f"Addition of {number_1} + {number_2 } =  {Addition}")
print(f"Subtraction  of {number_1} + {number_2 } = {Subtraction}")
print(f"Multiplication  of {number_1} + {number_2 } = {Multiplication}")
print(f"Division  of {number_1} + {number_2 } =  {Division}") if number_2 != 0 else "cannot dicicded by zero"
