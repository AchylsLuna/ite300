#Jonas J. Enriquez
#BSIT1-06
while True:
    quan = int(input('Enter a number: '))
    if not quan <= 0 or quan >=50:
        print("multiply {number}:")  
        for i in range(1, 51):
            multiply = quan * i
            print(multiply)
        
    else:
        print('error')
        break