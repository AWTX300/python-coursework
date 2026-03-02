#Avery Walker, Final Project Pt. 2
#program calculates weekly gross and take home pay

print('Pay Check Calculator')
print()

while True:
    try: 
        hours = int(input('Hours Worked (or 0 to exit program): '))
        
        if hours == 0:
            print('Exiting Pay Check Calculator.')
            break
        
        hourly_rate = float(input('Hourly Pay Rate: '))
        print()

        tax_rate = 0.18

        gross = hours * hourly_rate
        tax_amnt = gross * tax_rate
        take_home = gross - tax_amnt

        print(f'Gross Pay: ${gross:.2f}')
        print('Tax Rate: 18%')
        print(f'Tax Amount: ${tax_amnt:.2f}')
        print(f'Take Home Pay: ${take_home:.2f}')
        print('-----------------------------------')
        
    except ValueError:
        print('Invalid input. Please enter numbers only.')

