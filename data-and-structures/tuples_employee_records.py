employees = [
    ("Avery", "Walker", "Liv", "Female", "123-45-678", "Part Time"),
    ("Ali", "Perez", "Rey", "Female", "910-11-121", "Full Time"),
    ("Laura", "Barrantes", "Cat", "Female", "314-15-161", "Part Time"),
    ("Addie", "Briscoe", "Lee", "Female", "718-19-202", "Full Time"),
    ("Jess", "Smith", "Steven", "Male", "122-23-242", "Part Time"),
    ("Mary", "Adams", "Nicole", "Female", "526-27-282", "Full Time"),
    ("Kyle", "Ken", "Kim", "Male", "930-31-323", "Part Time"),
    ("Dan", "Robertson", "Sam", "Male", "334-35-363", "Full Time"),
    ("Daniel", "Antonio", "frias", "Male", "738-39-404", "Part Time"),
    ("Amy", "Roberts", "Anne", "Female", "142-43-444", "Full Time") ]

search = input("Search Employee Records: ")

hit=[]
for record in employees:
    if search.lower() in [records.lower() for records in record[:5]]:
        hit.append(record)
        
if hit:
    print("Results:")
    print("{:<10} {:<10} {:<10} {:<5} {:<10} {:<10}".format(
        "Last Name", "First Name", "Middle Name", "Gender", "SSN", "Employment Status"))
    for record in hit:
        print("{:<10} {:<10} {:<10} {:<5} {:<10} {:<10}".format(*record))
else:
    print("There is no match for your search.")

