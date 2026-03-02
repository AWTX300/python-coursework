#Week 4: Case Study
#AveryWalker--Batting average--1/28/25
#program takes input from users and calculates batting average
print('=' * 50)
text = "Baseball Team Manager"
print(text.center(50))

while True:
    print('MENU OPTIONS')
    print('1 - Calculate Batting average')
    print('2 - Exit Program')
    print('=' * 50)
    try:
        menu_option = int(input('Menu option: ')) #convert menu option to integer

        if menu_option == 1:
            at_bats = int(input('Official number of at bats: '))
            hits = int(input('Number of hits: '))
    
            if at_bats == 0: #prevent division by 0
                print('Batting average is undefined. (0 at bats)\n')
            else:
                avg = hits / at_bats
                print(f'Batting average: {avg:.3f}\n')
        
        elif menu_option == 2: #to exit program (option 2)
            print('Exiting Program...goodbye!\n')
            break #exit loop
        else: #in case they enter a number that's not 1/2
            print('Invalid input. Please try a number (1 or 2)!\n')
    except ValueError:
        print('Invalid input. Please try a number (1 or 2)!\n')
        





