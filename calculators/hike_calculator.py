#Avery Walker--Lab Assignment
#program takes input (miles walked) from user and calculates how many feet they walked

print('Hike Calculator')
print('Enter 0 to exit program')
print()

def calc_feet(miles):
    #convert miles to feet
    return miles * 5280

def user_input():
#get user input for miles walked
    while True:
        try:
            miles = float(input('How many miles did you walk?: '))
            
            if miles < 0:
                print('Please enter a positive number.')
                continue
                
            else:
                return miles
            
            return miles 
        except ValueError:
            print('Invalid input. Please enter numbers only.')

def main(): 
    while True:
        miles = user_input()
        
        if miles == 0:
            print()
            print('exiting program...')
            break
        
        feet = calc_feet(miles)
        print(f'You walked {feet} feet.')
        
main()