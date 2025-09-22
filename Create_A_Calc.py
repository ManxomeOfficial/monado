
"""
Calculator Assignment
==========================================================

YOUR MISSION: Complete the calculator functions below!

Each function has specific requirements that you must implement.
Read the docstrings and requirements carefully before coding.

GRADING:
- Each function is worth points based on complexity
- Bonus points for creative enhancements
- Code must be tested and working to receive full credit

RESOURCES YOU CAN USE:
- Python arithmetic operators: +, -, *, /, %, **
- Conditional statements: if, elif, else
- Loops: while, for
- Built-in functions: abs(), int(), float()
"""

def addition(a, b):
    """
    Add two numbers together and display the result.
    
    Parameters:
    a (float): First number
    b (float): Second number
    
    Returns:
    float: Sum of a and b
    
    REQUIREMENTS:
    1. Calculate the sum of a and b
    2. Print the result in the format: "a + b = result"
    3. Return the calculated sum
    
    EXAMPLE:
    addition(5, 3) should print: "5.0 + 3.0 = 8.0" and return 8.0
    """
    # TODO: Write your code here
    Result = a + b
    print(str(a) + " + " + str(b) + " = " + str(Result))
    return(Result)
    # As basic as it gets here, adds the two numbers and craps out the result in format.


def subtraction(a, b):
    """
    Subtract the second number from the first number.
    
    Parameters:
    a (float): First number (minuend)
    b (float): Second number (subtrahend)
    
    Returns:
    float: Difference of a and b
    
    REQUIREMENTS:
    1. Calculate a minus b
    2. Print the result in the format: "a - b = result"
    3. Return the calculated difference
    
    EXAMPLE:
    subtraction(10, 4) should print: "10.0 - 4.0 = 6.0" and return 6.0
    """
    # TODO: Write your code here
    Result = a - b
    print(str(a) + " - " + str(b) + " = " + str(Result))
    return(Result)
    # Same deal as addition just a basic print out


def multiplication(a, b):
    """
    Multiply two numbers together.
    
    Parameters:
    a (float): First number
    b (float): Second number
    
    Returns:
    float: Product of a and b
    
    REQUIREMENTS:
    1. Calculate the product of a and b
    2. Print result using × symbol: "a × b = result"
    3. Return the calculated product
    
    EXAMPLE:
    multiplication(6, 7) should print: "6.0 × 7.0 = 42.0" and return 42.0
    """
    # TODO: Write your code here
    Result = a * b
    print(str(a) + " x " + str(b) + " = " + str(Result))
    return(Result)
    # Not putting many impressive comments here I know but when it's simple you don't need to overexplain it.


def division(a, b):
    """
    Divide the first number by the second number.
    
    Parameters:
    a (float): Dividend (number being divided)
    b (float): Divisor (number dividing by)
    
    Returns:
    float: Quotient of a divided by b, or None if division by zero
    
    REQUIREMENTS:
    1. Check if b is zero - if so, print error message and return None
    2. If valid, calculate a divided by b
    3. Print result using ÷ symbol: "a ÷ b = result"
    4. Return the calculated quotient
    
    ERROR MESSAGE: "Error: Cannot divide by zero!"
    
    EXAMPLES:
    division(15, 3) should print: "15.0 ÷ 3.0 = 5.0" and return 5.0
    division(10, 0) should print: "Error: Cannot divide by zero!" and return None
    """
    # TODO: Write your code here
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        Result = a / b
        print(str(a) + " ÷ " + str(b) + " = " + str(Result))
        return(Result)
    # Same here.


def modulo(a, b):
    """
    Find the remainder when first number is divided by second number.
    
    Parameters:
    a (float): Dividend
    b (float): Divisor
    
    Returns:
    float: Remainder of a divided by b, or None if division by zero
    
    REQUIREMENTS:
    1. Check if b is zero - if so, print error message and return None
    2. If valid, calculate a mod b (remainder)
    3. Print result: "a mod b = result"
    4. Print explanation: "(This means a ÷ b leaves a remainder of result)"
    5. Return the calculated remainder
    
    ERROR MESSAGE: "Error: Cannot find remainder when dividing by zero!"
    
    EXAMPLES:
    modulo(17, 5) should print:
    "17.0 mod 5.0 = 2.0"
    "(This means 17.0 ÷ 5.0 leaves a remainder of 2.0)"
    and return 2.0
    """
    # TODO: Write your code here
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        Result = a % b
        print(str(a) + " mod " + str(b) + " = " + str(Result))
        return(Result)
    # Same here, keeping it simple.


def exponentiation(a, b):
    """
    Raise the first number to the power of the second number.
    
    Parameters:
    a (float): Base number
    b (float): Exponent (power)
    
    Returns:
    float: a raised to the power of b
    
    REQUIREMENTS:
    1. Calculate a to the power of b
    2. Print result using ^ symbol: "a^b = result"
    3. Return the calculated result
    
    EXAMPLE:
    exponentiation(2, 3) should print: "2.0^3.0 = 8.0" and return 8.0
    
    HINT: Use the ** operator for exponentiation
    """
    # TODO: Write your code here
    Result = a ** b
    print(str(a) + "^" + str(b) + " = " + str(Result))
    return(Result)


def greatest_common_factor(a, b):
    """
    Find the Greatest Common Factor (GCF) of two numbers using the Euclidean algorithm.
    
    Parameters:
    a (int): First number
    b (int): Second number
    
    Returns:
    int: Greatest Common Factor of a and b
    
    REQUIREMENTS:
    1. Convert inputs to positive integers using int(abs(a)) and int(abs(b))
    2. Handle special cases: if a is 0, return b; if b is 0, return a
    3. Use the Euclidean algorithm:
       - While b is not zero:
         - Calculate remainder = a % b
         - Print step: "Step X: a = b × (a // b) + remainder"
         - Set a = b, then b = remainder
         - Continue until b becomes 0
    4. Print final result: "GCF of original_a and original_b = final_a"
    5. Return the GCF (final value of a)
    
    EXAMPLE:
    greatest_common_factor(48, 18) should print:
    "Finding GCF of 48 and 18:"
    "  Step 1: 48 = 18 × 2 + 12"
    "  Step 2: 18 = 12 × 1 + 6"
    "  Step 3: 12 = 6 × 2 + 0"
    "GCF of 48 and 18 = 6"
    and return 6

    HINT: Save the original values before starting the algorithm for display
    """
    # TODO: Write your code here
    if a == 0:
        print("GCF of " + str(a) + " and " + str(b) + " = " + str(b))
    elif b == 0:
        print("GCF of " + str(a) + " and " + str(b) + " = " + str(a))
    else:
        OG_a = a
        OG_b = b
        a = int(abs(a))
        b = int(abs(b))
        x = 1
        while b > 0:
            r = a % b
            print("Step " + str(x) + ": " + str(a) + " = " + str(b) + " × (" + str(a) + " // " + str(b) + ") + " + str(r))
            a = b
            b = r
            x += 1
            continue
        print("GCF of " + str(OG_a) + " and " + str(OG_b) + " = " + str(a))

    


def get_number(prompt):
    """
    Get a valid number from the user with error handling.
    
    Parameters:
    prompt (str): Message to show the user
    
    Returns:
    float: Valid number entered by user
    
    REQUIREMENTS:
    1. Use a while loop that continues until valid input is received
    2. Use input(prompt) to get user input
    3. Use try-except to catch ValueError when converting to float
    4. If invalid input, print: "Invalid input! Please enter a valid number."
    5. Return the valid float value when successfully converted
    
    EXAMPLE INTERACTION:
    >>> get_number("Enter a number: ")
    Enter a number: abc
    Invalid input! Please enter a valid number.
    Enter a number: 5.5
    (returns 5.5)
    """
    # TODO: Write your code here
    num = None
    while 1==1:
        num = str(input())
        try:
            num = float(num)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        else:
            print(num)
            break




def display_menu():
    """
    Display the calculator menu options in a formatted way.
    
    Returns:
    None
    
    REQUIREMENTS:
    1. Print a header with "PYTHON CALCULATOR" 
    2. Use "=" characters for decoration (at least 50 characters wide)
    3. List all 8 options:
       - 1. Addition (+)
       - 2. Subtraction (-)
       - 3. Multiplication (×)
       - 4. Division (÷)
       - 5. Modulo/Remainder (%)
       - 6. Exponentiation (^)
       - 7. Greatest Common Factor (GCF)
       - 8. Quit
    4. Use "-" characters for a separator line
    
    EXACT FORMAT REQUIRED:
    ==================================================
    PYTHON CALCULATOR
    ==================================================
    Choose an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (×)
    4. Division (÷)
    5. Modulo/Remainder (%)
    6. Exponentiation (^)
    7. Greatest Common Factor (GCF)
    8. Quit
    --------------------------------------------------
    """
    # TODO: Write your code here
    print("==================================================\n"
    "PYTHON CALCULATOR\n"
    "==================================================\n"
    "Choose an operation:\n"
    "1. Addition (+)\n"
    "2. Subtraction (-)\n"
    "3. Multiplication (×)\n"
    "4. Division (÷)\n"
    "5. Modulo/Remainder (%)\n"
    "6. Exponentiation (^)\n"
    "7. Greatest Common Factor (GCF)\n"
    "8. Quit\n"
    "--------------------------------------------------\n")
   

def calculator():
    """
    Main calculator function - the heart of the program!
    
    This function should handle all user interaction and call other functions.
    
    Returns:
    None
    
    REQUIREMENTS:
    1. Print welcome message: "Welcome to the Python Calculator!"
    2. Use a while loop to keep the program running until user quits
    3. In each iteration:
       a. Call display_menu() to show options
       b. Get user's menu choice (1-8)
       c. Validate the choice - if invalid, show error and continue
       d. If choice is 8, print goodbye message and break the loop
       e. Get two numbers from user using get_number()
          - For GCF (choice 7): mention it needs whole numbers
          - For other operations: get any numbers
       f. Call the appropriate function based on user's choice
       g. Ask if user wants to continue: "Would you like to perform another calculation? (yes/no): "
       h. If answer is not yes/y/yeah/yep, break the loop
    
    MENU CHOICE VALIDATION:
    - Only accept choices '1' through '8'
    - For invalid choices, print: "Invalid choice! Please enter a number between 1 and 8."
    
    GOODBYE MESSAGES:
    - When user chooses 8: "Thank you for using the Python Calculator! \nGoodbye!"
    - When user chooses not to continue: "Thank you for using the Python Calculator!"
    
    
    HINT: Use if-elif-else statements to call the right function:
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    # ... and so on
    """
    # TODO: Write your code here
    active = True
    print("Welcome to the Python Calculator!")
    while active == True:
        display_menu()
        step = "zero"
        while step == "zero":
            select = input()
            try:
                select = int(select)
            except:
                print("Invalid choice! Please enter a number between 1 and 8.")
            else:
                select = int(select)
                if select > 0 and select < 8:
                    step = "first"
                elif select == 8:
                    print("Thank you for using the Python Calculator! \nGoodbye!")
                else:
                    print("Invalid choice! Please enter a number between 1 and 8.")
        while step == "first" or step == "second": # Combined the two steps into one variable step.
            print("Please enter the " + step + " number (whole numbers only):") if select == 7 else print("Please enter the " + step + " number:")
            in_t = input()
            try:
                if select == 7:
                    in_t = int(in_t)
                else:
                    in_t = float(in_t)
            except:
                print("You must insert a valid number!")
            else:
                in_t = float(in_t)
                if step == "first":
                    in_a = in_t
                    step = "second"
                else:
                    in_b = in_t
                    step = "final"
        if step == "final":
            if select == 1:
                addition(in_a, in_b)
            elif select == 2:
                subtraction(in_a, in_b)
            elif select == 3:
                multiplication(in_a, in_b)
            elif select == 4:
                division(in_a, in_b)
            elif select == 5:
                modulo(in_a, in_b)
            elif select == 6:
                exponentiation(in_a, in_b)
            elif select == 7:
                greatest_common_factor(in_a, in_b)
            print("Would you like to perform another calculation? (yes/no): ")
            would = input()
            if would == "yes" or would == "y" or would == "yeah" or would == "yep":
                step = "zero"
            else:
                print("Thank you for using the Python Calculator!")
                active = False
                
        # add short wait before calc asks for next calculation


            
calculator()


# ===================================================================
# TESTING CODE - DO NOT MODIFY THIS SECTION!
# ===================================================================

def test_your_functions():
    """
    Test function to check if your implementations work correctly.
    Run this after completing your functions to verify they work!
    """
    print("TESTING YOUR CALCULATOR FUNCTIONS")
    print("=" * 50)
    
    # Test basic operations
    print("Testing Addition:")
    try:
        result = addition(5, 3)
        print(f"Returned: {result}")
        assert result == 8, "Addition test failed!"
        print("Addition test passed!\n")
    except Exception as e:
        print(f"Addition test failed: {e}\n")
    
    print("Testing Division by Zero:")
    try:
        result = division(10, 0)
        assert result is None, "Division by zero should return None!"
        print("Division by zero test passed!\n")
    except Exception as e:
        print(f"Division by zero test failed: {e}\n")
    
    print("Testing GCF:")
    try:
        result = greatest_common_factor(48, 18)
        print(f"Returned: {result}")
        assert result == 6, "GCF test failed!"
        print("GCF test passed!\n")
    except Exception as e:
        print(f"GCF test failed: {e}\n")
    
    print("If all tests passed, your functions are working correctly!")
    print("Now test the full calculator by running: calculator()")


# ===================================================================
# SUBMISSION CHECKLIST
# ===================================================================
"""
BEFORE SUBMITTING, MAKE SURE:
☐ All functions have code (no 'pass' statements remaining)
☐ All functions print output in the required format
☐ Error handling works for division and modulo
☐ GCF function shows step-by-step process
☐ get_number() handles invalid input gracefully
☐ display_menu() matches the required format exactly
☐ calculator() function has a complete menu system
☐ You tested your calculator with different inputs
☐ All print statements use the exact format specified
☐ Your code has comments explaining your logic

Requirement Breakdown
- Basic operations (add, subtract, multiply, exponent)
- Division and Modulo with error handling  
- GCF with Euclidean algorithm
- get_number() with error handling
- display_menu() with exact formatting
- calculator() main function
- Code quality and comments
- Bonus for enhancements"""