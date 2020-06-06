import random
class Hero:
    def __init__(self, name: str, hp: int, damage: int ):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('Hi i am', self.name)

    def attack(self) -> int:
        return self.damage
    def attacked(self, damage: int) -> bool: 
        if self.hp - damage <= 0:
            print(self.name, 'died...')
            return False
        else: 
            self.hp = self.hp - damage
            print(self.name, self.hp)
            return False

you = Hero('You', 100,20)
monster = Hero('Monster',100,10)

while True:
    is_died = False
    togloom = random.randrange(1, 3)
    too = int(input('Тоо оруулна уу? '))
    if togloom == too:
        is_died = monster.attacked(you.attack())
    else:
        is_died = you.attacked(monster.attack())
    if is_died:
        break 
    else: 
        print('You died...')

