🧮 Calculators
Utility programs that take real-world user input and compute meaningful results. Each program emphasizes clean input handling, exception safety, and readable output.

💵 pay_check_calculator.py — Pay Check Calculator
Calculates weekly gross pay, tax deduction (18%), and take-home pay from hours worked and hourly rate. Runs in a loop so multiple employees can be calculated in one session.

Concepts: while loop, try/except for ValueError, f-strings with 2 decimal formatting, early exit with break
Run: python pay_check_calculator.py

Hours Worked (or 0 to exit program): 40

Hourly Pay Rate: 22.50

Gross Pay: $900.00

Tax Rate: 18%

Tax Amount: $162.00

Take Home Pay: $738.00

🥾 hike_calculator.py — Hike Distance Calculator
Converts miles walked into feet. Uses a function-based design with a dedicated input validator — a clean example of separating user input logic from computation logic.

Concepts: Functions (calc_feet, user_input, main), try/except, negative number rejection, early exit on 0
Run: python hike_calculator.py

How many miles did you walk?: 3.5

You walked 18480.0 feet.

⚾ batting_average.py — Baseball Batting Average Calculator
A menu-driven program for a baseball team manager. Calculates batting average (hits ÷ at-bats) with explicit handling for zero at-bats (division by zero prevention) and formatted 3-decimal output.

Concepts: Menu-driven loop, try/except, division-by-zero guard, f-string formatting, int() conversion
Run: python batting_average.py

==================================================

         Baseball Team Manager
         
MENU OPTIONS

1 - Calculate Batting average

2 - Exit Program

==================================================

Batting average: 0.325

➕ basic_arithmetic.py — Basic Arithmetic Operations
Takes two integers from the user and prints the result of multiplication, addition, division, and subtraction. A Week 1 assignment focused on core Python syntax and output formatting.

Concepts: input(), int() conversion, arithmetic operators, print()
Run: python basic_arithmetic.py

Number 1: 12

Number 2: 4

number 1 * number 2 =  48

number 1 + number 2 =  16

number 1 / number 2 =  3.0

number 1 - number 2 =  8

💡 Key Concepts Across All Calculators

try/except ValueError to catch non-numeric input without crashing
Loop-based programs that let users run multiple calculations per session
f-string formatting for clean, professional-looking numeric output (:.2f, :.3f)
Division-by-zero prevention before performing calculations
