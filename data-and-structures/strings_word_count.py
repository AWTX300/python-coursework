t = input("Enter a string of multi-line text: ")

if "\n" in t:
    t.replace('\n', ' ')
    newline = t.count('\n')

if "  " in t:
    t.replace('  ', ' ')
    spaces = t.count(' ')
    newline = t.count('\n')

word_count = t.split()
count=len(word_count)

print("Word Count: ", count) 