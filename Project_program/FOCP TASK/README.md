TASK 1
BECKETT PIZZA PLAZA CALCULATOR

FOLDER STRUCTURE 

Final_focp/

Project Program/

FOCP TASK/

Pizza_calculator.py

README.md

Programs Overview

This program calculates the total cost for a pizza order with a special discount offer: Buy 4 pizzas, pay for only 3! The Cheapest pizza is FREE.

Name: Beckett Pizza Plaza 4 for 3 offer Calculator

Objective: Calculate order total and discount for a 4-pizza order

Discount system: The cheapest of the 4 pizzas is free

How to Run

1.	Open your terminal or command prompt
   
2.	Navigate to the Task 1 folder
   
Example: 

cd path/to/Task1

5.	Run the program:
6.	
Python pizza_calculator.py

Required Inputs:

•	The program will ask you to enter 4 pizzas price one at a time

Enter a number (12 or 15)
•	Must be positive number 

•	If you add an invalid input like negative number then the program will ask you to add the number again.

Example:

Enter Price of Pizza #1: 12

Enter Price of Pizza #2: 12

Enter Price of Pizza #3: 12

Enter Price of Pizza #4: 12


Output 


1.	Order Total: Final price after removing the cheapest pizza
   
2.	Total Discount %: How much Discount was given.
3.	
Example:

Order Total is £36.00, a fabulous discount of 25%

Calculation Process:

1.	Adds all 4-pizza process together
   
Example: 12 + 12 + 12 = 48

2.	Finds the cheapest pizza
   
Example: cheapest = 12

3.	Subtracts the cheapest from the total

Example: 48 – 12 = 36

5.	Calculates discount Percentage
   
Example: (12/48) x 100 = 25%

Example Scenarios

Scenario 1: All same price

Input: 12, 12, 12, 12

Output: Order Total is £ 36.00, a fabulous discount of 25%

All Pizza have the same cost, so the total amount a customer saves on discount is 25%

Scenario 2: One cheapest Pizza 

Input: 12, 12, 12, 11

Output: Order Total is £36.00, a fabulous discount of 24%

The £11 is free, as it’s the cheapest pizza on order list ultimately Resulting in a discount less than 25%

Scenario 3: All Different Prices.

Input : 14.99, 16.99, 15.99, 11.00

Output: Order total is £ 47.77, a fabulous discount of 19%!

The £ 11 pizza is free, you pay for the three most expensive ones


Error Handling

The program handles the following mistakes:

Invalid Input                                   What Happens

0                                                       “Please enter a valid price!”

Negative number like -5               “ Please enter a valid price!”

Text (like pepperoni)                      “ Please enter a valid price!”

The program will keep asking until you enter a valid price.

Key features

•	Validates all user input

•	Handles decimal price (like £14.99)

•	Automatically finds the cheapest pizza

•	Calculates discount percentage accurately

•	User friendly error messages 

Requirements met

•	Accepts 4 Pizza prices

•	Calculates total after discount

•	Displays discount percentage

•	Handles invalid input gracefully

•	Follows the exact output format from assignment 

Program concept and functions used:

get_pizza_price()  - Gets and validates each pizza price 

calculate_order() – Main calculation and display logic 

Lists to store prices

Built in functions: sum (), min ()

Strings formatting for currency display

Invalid validation with try/expect 

