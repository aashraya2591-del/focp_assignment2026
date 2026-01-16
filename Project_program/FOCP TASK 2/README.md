TASK 2

PASSWORD SECURITY CHECKER

FOLDER STRUCTURE 

final_focp/

Project Program/

FOCP TASK2/

password_checker.py

README.md



Program Overview

This program simulates a security verification system. First of all, it checks if you’re password is long enough or not based on that it commands you to type 3 random characters from your password to prove that you know your password.

Name: Password Security Checker

Purpose: Verify user identity by checking random characters from their password.

Security check: Password must be at least 9 characters long, verify 3 random positions

How to Run

1.	Open your terminal or command prompt
   
2.	Navigate to the Task2 folder:

Cd path/to/ Task2
Run the program:

python password_checker.py

Required Inputs

Step 1 

 Enter your password
 
Type a password that is at least 9 characters long

Press Enter

The password will appear on screen (This is intentional for the assignment)

Step 2: Verify Random characters

The program will ask for 3 random characters from your password:

It will tell you which position (like “position 5”)

Type only ONE Letter and press Enter

Must match exactly (case sensitive)


Example :

Enter your password: Camembert

Enter letter at position 4: e

Enter letter at position 5: r

Enter letter at position 3:m

Output

The program can output different messages

Password Too Short 

Enter your password: cheese

Password too short.

Wrong Character

Enter your password: wensleydale

Enter letter at position 11: e

Correct

Enter letter at position 9: a

Correct

Enter letter at position 10: d

Security check failed.

All correct




Enter your password: camembert

Enter letter at position 4: e

Correct

Enter letter at position 8:r

Correct

Enter letter at position 3:m

Correct

Security check passed.

How it works

Step by Step Process

1.	Get Password from user
   
User types their password 

2.	Check length
   
If less than 9 characters – Exit with “Password too short.”

If 9 or more – Continue to verification 

4.	Generate 3 random positions
   
Program picks 3 random numbers between 1 and password length
These positions are checked one by one

5.	Verify each character

Ask user for character at that position

If correct – print “Correct” and continue

If wrong – Print “Security check failed.” And exit immediately 

6.	All checks pass
   
Print “Security check passed.”

Understanding Positions

If your password is “camebert”

Position: 1 2 3 4 5 6 7 8 9

  Letter: c a m e m b e r t 
 
	
So, when asked:

Position 1: c

Position 2: e

Position 3: t


Key features

•	Length validation (minimum 9 characters)

•	Random position selection

•	Immediate Failure on wrong answer

•	Case sensitive character checking 

•	Clear feedback after each check 

Requirements Met 

•	Prompts user to enter password

•	Checks password length (minimum 9 characters)

Exist if password too short

•	Asks for 3 rando characters 


