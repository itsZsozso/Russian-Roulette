import random

bullet_position = 4

def spin_chamber():
    chamber_position = random.randint(1,6)
    return chamber_position

def fire_gun():
    if bullet_position == spin_chamber():
        return '''
              _  _____________________,     
               \ \@([       ]_________)                             ___        _                ___
             _/\----[______]                X        X             |   |      / |     /|   /  /
           //   / ((   )                       -                   |__/      /__|    / |  /  |   __
         /_____|’------’                                           |   |    /   |   /  | /   |     |
         \_____/                                                   |___/   /    |  /   |/     \___/
  '''
    else:
        return '''
              _  _____________________,     
               \ \@([       ]_________)                              ___            ___
             _/\----[______]                >        <              /   \  |    |  /   \  |  /   
           //   / ((   )                       -                   |       |    | |       |/
         /_____|’------’                                           |       |    | |       |\ 
         \_____/                                                    \___/  |___ |  \___/  |  \ '''

while True:
    print(fire_gun())
    input()
