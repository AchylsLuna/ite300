while True:
    quan = int(input('Enter a number: '))
    if quan <= 1 or quan >= 50:
        return "not available"
else: 
    multiply = []
#ginamitan ko ng loop na 1-51 para mag stop siya sa 50
        for i in range(1, 51):
            multiply = quan * i
            print(multiply)
        
else:
    print('error')
