import random

end = False

count = 0

def guess_pl():
    guess = input('Gib me 4 digit number pls: \n')
    guess_list = [i for i in guess]
    if len(guess_list) > 4:
        print('INVALID INPUT')
        guess_pl()
    elif len(guess_list) < 4:
        print('INVALID INPUT')
        guess_pl()
    return guess_list

def rando_num():
    rando = random.randrange(999,10000)
    rando_list = [i for i in str(rando)]
    return rando_list

    
def cow_thing(rando_list, guess_list):

    c = 0

    for i in range(4):
        if rando_list[i] == guess_list[i]:
            c += 1
    return c


def bull_thing(rando_list, guess_list):

    b = 0

    for i in range(4):
        if rando_list[i] in guess_list and rando_list[i] != guess_list[i]:
            b += 1
    return b

if __name__ == "__main__":

    baab = rando_num()

    bab = ''.join(baab)

    print(bab)


    while end == False:

        brb = guess_pl()
        bob = ''.join(brb)
        
        cow = cow_thing(baab, brb)

        bull = bull_thing(baab, brb)

        print('Cows: ', cow, 'Bull: ', bull)

        count += 1

        if cow == 4:
            print('Broavo it took you', count,'times to guess number')
            ye = input('Do you want to play again: (y/n)\n')
            if ye == 'n':
                print('Oi wasn\'t that fun?')
                end = True
            else:

                count = 0
                
                baab = rando_num()

                bab = ''.join(baab)

                print(bab)

            


