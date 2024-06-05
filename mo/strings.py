weight = int(input("weight:"))
unit_input = input('(L)bs or (K)g:')

if unit_input.upper() == 'L':
    your_weight = weight / 0.45
    print(f'you are {your_weight} kilos')
else:
    your_weight = weight * 0.45
    print(f' you are {your_weight} pounds')
    
