📊 Data & Structures
Programs focused on working with data — collecting it, storing it, searching it, and presenting it clearly. These assignments cover Python's core data structures: lists, tuples, and strings.

📝 test_scores.py — Test Score Tracker
Collects an arbitrary number of test scores from the user (entering x to stop), then calculates and displays the total and average score. Validates that each score is between 0 and 100.

Concepts: while True loop, sentinel value ('x'), running total, input validation, round()
Run: python test_scores.py

Sample output:

Enter test score (or 'x' to quit): 88

Enter test score (or 'x' to quit): 92

Enter test score (or 'x' to quit): 75

Enter test score (or 'x' to quit): x

======================

Total Score: 255

Average Score: 85

🔤 strings_word_count.py — String Word Counter
Takes a multi-line string from the user and counts the number of words using Python's built-in split() method, which handles variable spacing and newlines automatically.

Concepts: String input, split(), len(), basic string manipulation
Run: python strings_word_count.py

Sample output:
Enter a string of multi-line text: Hello world this is Python
Word Count:  5

🔍 functions_char_finder.py — Character Position Finder
Given a string and a target character, finds and returns all positions where that character appears. Positions are returned as a 1-indexed list so they're human-readable.

Concepts: Functions, for loop with range(len()), list append(), index offset (0→1 based)
Run: python functions_char_finder.py

Sample output:
Enter the string: programming
Enter the character you would like to locate: g
[4, 11]

👥 tuples_employee_records.py — Employee Records Search
Stores a set of employee records as a list of tuples and implements a search function that finds matching records across any field (first name, last name, middle name, gender, SSN). Results are printed in a formatted table.

Concepts: Tuples, list of tuples, list comprehension for search, str.format() for column-aligned output, case-insensitive comparison with .lower()
Run: python tuples_employee_records.py

Sample output:
Search Employee Records: walker
Results:
Last Name  First Name Middle Name  Gender SSN        Employment Status
Walker     Avery      Liv          Female 123-45-678 Part Time

💡 Key Concepts Across This Section

Lists — dynamic collections used for accumulating results (test_scores.py, functions_char_finder.py)
Tuples — immutable records used for structured data storage (tuples_employee_records.py)
String methods — split(), lower(), count(), find(), join() used across all programs
Formatted output — str.format() with width specifiers for aligned table output
Search logic — iterating over collections and filtering with conditions
