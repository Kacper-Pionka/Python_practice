end = 'no'


options = ('rock', 'paper', 'scissors')

while end != "y":

    p1 = ''
    p2 = ''
    
    while p1 not in options:
        p1 = input('p1 type rock, paper or scissors ')
        
    while p2 not in options:
        p2 = input('p2 type rock, paper or scissors ')
    
    if p1 == 'rock' and p2 == 'paper': print('p2 wins')
    if p1 == 'paper' and p2 == 'rock': print('p1 wins')
    
    if p1 == 'rock' and p2 == 'scissors': print('p1 wins')
    if p1 == 'scissors' and p2 == 'rock': print('p2 wins')
    
    if p1 == 'paper' and p2 == 'scissors': print('p2 wins')
    if p1 == 'scissors' and p2 == 'paper': print('p1 wins')
    
    if p1 == 'rock' and p2 == 'rock': print('Draw')
    if p1 == 'paper' and p2 == 'paper': print('Draw')
    if p1 == 'scissors' and p2 == 'scissors': print('Draw')
    
    end = input('end game? (y/n)\n')
