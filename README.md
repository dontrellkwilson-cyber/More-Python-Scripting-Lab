<h1>More Python Scripting Lab</h1>

<h2>Description:</h2>
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its built-in data structures and dynamic typing support rapid application development. Python also allows developers to import libraries, which reduces the amount of code required to complete tasks.
<br />

<h2>Languages and Technologies Used:</h2>

- <b>Python</b> 
  
<h2>Environments Used:</h2>

- <b>Kali Linux</b>
  
<h2>Lab Walk-Through:</h2>

**Task 1**:

<p align="center">
Creating and Using Functions: <br />


<p align="center">
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/e5384b58-9ec9-4447-a537-57c88d185c38" />
<br><br>
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/5351429c-2d9b-471e-9c83-4a42f9c7d046" />
<br><br>
</p>
 
**` Instructions `**
- Open a terminal in Kali (**` CTRL + ALT + T `**) and create a new document with nano.
- **Type the following**:
   - nano Sample01.py
   - #!/usr/bin/python3
   - number = int(input("Enter a number: "))
   - def calculation(number):
   - if number < 5:
      - print(number, "is less than 5")
    - elif number >= 5:
        - print(number, "is greater than or equal to 5")
    - else:
        - print("Error")
    - return
    - calculation(number)
- Save this file and exit.
   - **Save**: CTRL + O
   - **Exit**: CTRL + X

**` Let’s break down what this script is doing `**:
- 1. The first line is creating a variable that will store an integer when the user enters one after they are prompted.
- 2. This is our definition (or function) and uses the number variable throughout the definition.
- 3. This section contains simple calculations.
- 4. This line is returning the result of the calculations back to the definition in section 3 and is updating the number variable inside the definition.
- 5. This is printing the “number” variable after the definition has performed some function on it.

**` Making a Python Script Executable: `**
- chmod +x Sample01.py
- ./Sample01.py

**` Tasks Completed `**
- A function was created and executed. User input was passed into the function, and conditional logic was applied to produce output.
  
**` Overview `**
- In this task, a Python function is created and executed. The function evaluates a number provided by the user and prints a result based on defined conditions. Functions group related code into reusable blocks. This approach reduces redundancy and improves code organization.

**Task 2**:
 <p align="center">
Understanding Parameters: <br/>

<p align="center">
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/4585cf87-be34-4c16-b5e5-3df782355bb8" />
<br><br>
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/76851c12-6165-4e02-9d8f-dffdc165aa35" />
</p>

- Note that the number parameter is merely there for accessing the data within the function, and that parameters and variable names don’t have to match.
- In the above screenshot, we are passing number to the definition calculation even though the parameter is named integer. 
- The parameter name is merely there for accessing the data within the definition.

**` Making a Python Script Executable: `**
- chmod +x Sample02.py
- ./Sample02.py
  
**` Tasks Completed `**
- A variable was passed into a function with a different parameter name, and the function executed successfully.

**` Overview `** 
-  This task demonstrates the use of parameters within functions. The parameter name inside the function does not need to match the variable name passed into it. A parameter serves as a placeholder for the value provided when the function is called.

 **Task 3**:
<p align="center">
Using Logical Operators:<br/>

<p align="center">
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/75f23e88-4eb9-407a-9207-8dd01493818c" />
 <br><br>
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/6396f155-af65-441a-b288-ec2d040fc8a8" />

**` Instructions `**
- Open a terminal in Kali (**` CTRL + ALT + T `**) and create a new document with nano.
- **Type the following**:
   - nano Sample03.py
   - #!/usr/bin/python3
   - def calculation(num):
   - if number < 5 and number 0:
      - print(number, "is between 0 and 5")
    - elif number >= 5 and num < 10:
        - print(number, "is equal or greater than 5 less than 10")
   - elif num > 10 or num < 0:
      - print(num,"That number is not between 1 and 10!")
    - else:
        - print("out of range")
    - return
    - number = int(input(“Enter a number:”))
    - calculation(number)
- Save this file and exit.
   - **Save**: CTRL + O
   - **Exit**: CTRL + X
 
**` Making a Python Script Executable: `**
- chmod +x Sample03.py
- ./Sample03.py
  
 **` Tasks Completed `**
- Multiple conditions were combined using logical operators. Different inputs were tested to observe how the program responded.

**` Overview `** 
-  This task introduces logical operators within conditional statements. Logical operators expand the functionality of decision-making in code. The AND operator requires both conditions to be true. The OR operator requires at least one condition to be true.


**` Key Takeaways `** 
- Functions were used to organize code into reusable blocks.
- Parameters were used to pass data into functions.
- Logical operators were applied to control program flow and decision-making.


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
