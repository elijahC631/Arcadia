import time
import random
import sys
import os

class Weapon:
    def __init__(self):
        self.base = 8.0
        self.katana = 7.0
        self.scythe = 6.0
        self.trident = 5.0
        self.scepter = 4.0
        self.flamed_katana = 3.5
        self.flamed_scythe = 3.0
        self.flamed_trident = 2.5
        self.flamed_scepter = 2.0
        self.infrared_katana = 1.75
        self.infrared_scythe = 1.5
        self.infrared_trident = 1.25
        self.infrared_scepter = 1.0
        self.transluscent_katana = .80
        self.transluscent_scythe = .70
        self.transluscent_trident = .60
        self.transluscent_scepter = .50
        self.arcadia_blade = .1
weapon = Weapon()

class Enemy:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.strength = 0
        self.speed = 0
        self.weapon = weapon.base
        self.coin = random.randint(1,2)
        self.wpdrop = random.randint(1,2)
        self.hpdrop = random.randint(1,2)
    def accuracy(self):
        acc = (0.5 * self.speed) + 30
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
enemy = Enemy()

class Build:
    def __init__(self):
        self.name = 'Player'
        self.health = 0.0
        self.strength = 0.0
        self.speed = 0.0
        self.hpcount = 3
        self.weapon = weapon.base
    
    def choose_build(self):
        print('\nWelcome to Arcadia!\n')
        time.sleep(1)
        clas = input('Choose your class:\n1 = Brute\n2 = Mage\n3 = Assassin\n\nEnter Here: ')
        clas = str(clas)
        if clas == '1':
            print('\nYou have selected: Brute\n')
            self.health = 80.0
            self.strength = 120.0
            self.speed = 60.0
            self.name = 'Brute'
            print(f'{self.name} Stats:')
            print(f'Health: {self.health}\nStrength: {self.strength}\nSpeed: {self.speed}')
        elif clas == '2':
            print('\nYou have selected: Mage\n')
            self.health = 100.0
            self.strength = 60.0
            self.speed = 80.0
            self.hpcount = 5
            self.name = 'Mage'
            self.acc = (-11/24 * enemy.speed) +96.25
            print(f'{self.name} Stats:')
            print(f'Health: {self.health}\nStrength: {self.strength}\nSpeed: {self.speed}')
        elif clas == '3':
            print('\nYou have selected: Assassin\n')
            self.health = 60.0
            self.strength = 70.0
            self.speed = 110.0
            self.weapon = weapon.katana
            self.name = 'Assassin'
            self.acc = (-1/2 * enemy.speed) +105
            print(f'{self.name} Stats:')
            print(f'Health: {self.health}\nStrength: {self.strength}\nSpeed: {self.speed}')
        elif clas == '':
            print('\nInvalid Choice, Try Again.\n')
            return self.choose_build()
        else:
            print('\nInvalid Choice, Try Again.\n')
            return self.choose_build()
build = Build()
build.choose_build()

class Char:
    def __init__(self):
        self.name = build.name
        self.health = build.health
        self.strength = build.strength
        self.speed = build.speed
        self.coins = 0
        self.hpcount = build.hpcount
        self.weapon = build.weapon
        self.weapon_name = 'Base Weapon'
        
    weapon_dict = {
        weapon.base: 'Rusty Sword',
        weapon.katana: 'Katana',
        weapon.scythe: 'Scythe',
        weapon.trident: 'Trident',
        weapon.scepter: 'Scepter',
        weapon.flamed_katana: 'Flamed Katana',
        weapon.flamed_scythe: 'Flamed Scythe',
        weapon.flamed_trident: 'Flamed Trident',
        weapon.flamed_scepter: 'Flamed Scepter',
        weapon.infrared_katana: 'Infrared Katana',
        weapon.infrared_scythe: 'Infrared Scythe',
        weapon.infrared_trident: 'Infrared Trident',
        weapon.infrared_scepter: 'Infrared Scepter',
        weapon.arcadia_blade: 'The Mythic Arcadia Blade'
    }
    
    def weapon_name(self):
        self.weapon_name = self.weapon_dict.get[self.weapon]

    def accuracy(self):
        if self.name == 'Brute':
            acc = ((-5/12) * enemy.speed) +87.5
        elif self.name == 'Mage':
            acc = ((-11/24) * enemy.speed) +96.25
        elif self.name == 'Assassin':
            acc = ((-1/2) * enemy.speed) +105
        else:
            acc = 0
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
char = Char()

class Cont:
    def prompt1(self):
        c = input('\nContinue? (Y/N): ')
        if c.capitalize() == 'Y':
            print('Continuing, please wait.')
            time.sleep(2)
        elif c.capitalize() == 'N':
            print('Going Back!')
            time.sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print('Invalid Choice, Try Again.')
            return self.prompt1()
        
    def prompt2(self):
        c = input('\nContinue? (Y/N): ')
        if c.capitalize() == 'Y':
            print('Continuing, please wait.')
            time.sleep(2)
        elif c.capitalize() == 'N':
            print('Going Back!')
            time.sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print('Invalid Choice, Try Again.')
            return self.prompt2()
        
cont = Cont()
cont.prompt1()

class Goblin:
    def __init__(self):
        self.name = 'Goblin'
        self.base_health = 30
        self.health = self.base_health
        self.strength = 30
        self.speed = 30
        self.weapon = weapon.base
        self.coin = random.randint(5,15)
        self.wpdrop = random.randint(1,12)
        self.hpdrop = random.randint(0,2)
    def accuracy(self):
        acc = (-3/10 * char.speed) + 68
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
goblin = Goblin()

class Wolf:
    def __init__(self):
        self.name = 'Fiendish Werewolf'
        self.base_health = 90
        self.health = self.base_health
        self.strength = 80
        self.speed = 90
        self.weapon = weapon.base
        self.coin = random.randint(15,40)
        self.wpdrop = random.randint(1,15)
        self.hpdrop = random.randint(0,2)
    def accuracy(self):
        acc = (-2/5 * char.speed) + 109
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
wolf = Wolf()

class FireGoblin:
    def __init__(self):
        self.name = 'Fire Goblin'
        self.base_health = 130
        self.health = self.base_health
        self.strength = 100
        self.speed = 100
        self.weapon = weapon.trident
        self.coin = random.randint(40,70)
        self.wpdrop = random.randint(9,20)
        self.hpdrop = random.randint(0,3)
    def accuracy(self):
        acc = ((-1/3) * char.speed) + (365/3)
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
fire_goblin = FireGoblin()

class TorchedZombie:
    def __init__(self):
        self.name = 'Torched Zombie'
        self.base_health = 110
        self.health = self.base_health
        self.strength = 70
        self.speed = 150
        self.weapon = weapon.scythe
        self.coin = random.randint(40,70)
        self.wpdrop = random.randint(9,20)
        self.hpdrop = random.randint(0,3)
    def accuracy(self):
        acc = 90
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
torched_zombie = TorchedZombie()

class FireLord:
    def __init__(self):
        self.name = 'Fire Lord'
        self.base_health = 170
        self.health = self.base_health
        self.strength = 150
        self.speed = 120
        self.weapon = weapon.flamed_katana
        self.coin = random.randint(70,100)
        self.wpdrop = random.randint(6,30)
        self.hpdrop = random.randint(1,3)
    def accuracy(self):
        acc = 90
        return acc
    def damage(self):
        dmg = (self.speed + (1.2 * self.strength))/self.weapon
        return dmg
fire_lord = FireLord()


class Battle:
   def __init__(self, char, enemy):
    self.char = char
    self.enemy = enemy
   
   def start_battle(self):
    time.sleep(1)
    self.enemy.health = self.enemy.base_health
    while self.char.health > 0 and self.enemy.health > 0:
        time.sleep(1)
        choice = input(f'\nPress 1 to attack, Press 2 to use a healing potion ({self.char.hpcount}x remaining.) : ')
        if choice== '1':
            print('You swing...')
            time.sleep(1)
            hit = random.randint(1, 100)
            if hit <= self.char.accuracy():
                self.enemy.health = self.enemy.health - self.char.damage()
                print(f'\nYour attack did {self.char.damage()} damage.\n{self.enemy.name} has {self.enemy.health} health remaining.')
            else:
                print('Your attack MISSED!')
            if self.enemy.health > 0:
                hit = random.randint(1, 100)
                time.sleep(1)
                print(f'\n{self.enemy.name} swings...')
                time.sleep(1)
                if hit <= self.enemy.accuracy():
                    self.char.health = self.char.health - self.enemy.damage()
                    print(f'\n{self.enemy.name}s attack did {self.enemy.damage()} damage.' )
                    print(f'Your current health is now: {self.char.health}')
                else:
                    print(f'{self.enemy.name} attack MISSED!')
        elif choice == '2':
            if self.char.hpcount > 0 :
                self.char.hpcount = self.char.hpcount - 1
                print('1x Health Potion consumed.')
                self.char.health = self.char.health + 15
                time.sleep(.5)
                print(f'Current health is now: {self.char.health}')
                if self.enemy.health > 0:
                    hit = random.randint(1, 100)
                    time.sleep(1)
                    print(f'\n{self.enemy.name} swings...')
                    time.sleep(1)
                    if hit <= self.enemy.accuracy():
                        char.health = self.char.health - self.enemy.damage()
                        print(f'\n{self.enemy.name}s attack did {self.enemy.damage()} damage.' )
                        print(f'Your current health is now: {self.char.health}')
                    else:
                        print(f'{self.enemy.name} attack MISSED!')
            else:
                time.sleep(0.5)
                print('Out of health potions!')
        else:
            print('Invalid Choice, Try Again.')
        if self.char.health <= 0:
            time.sleep(1)
            print('\nGame Over.')
            ng = int(input('\nNew Game?\n1- New Game\n2- Game Over\n\nEnter Here: '))
            if ng == 1:
                os.execv(sys.executable, ['python'] + sys.argv)
            elif ng == 2:
                sys.exit()
        elif self.enemy.health <= 0:
            time.sleep(1)
            print(f'\nYou have successfully defeated the {self.enemy.name}!')          
            self.char.coins = self.char.coins + self.enemy.coin
            time.sleep(0.75)
            print(f'\nYou received {self.enemy.coin} coins.')
            print(f'Total: {self.char.coins} coins.')
            if self.enemy.wpdrop >= 100 and self.char.weapon > weapon.arcadia_blade:
                self.char.weapon = weapon.arcadia_blade
                time.sleep(.5)
                print('\nOh My God. You are the true Arcadian.')
                print('\nYou picked up the Legendary Arcadia Blade after the battle! You are cemented in history forever.')
            elif self.enemy.wpdrop >= 75 and self.char.weapon > weapon.infrared_scepter:
                self.char.weapon = weapon.infrared_scepter
                time.sleep(.5)
                print('\nYou picked up a "Infrared Scepter" after the battle!')
            elif self.enemy.wpdrop >= 65 and self.char.weapon > weapon.infrared_trident:
                self.char.weapon = weapon.infrared_trident
                time.sleep(.5)
                print('\nYou picked up a "Infrared Trident" after the battle!')
            elif self.enemy.wpdrop >= 55 and self.char.weapon > weapon.infrared_scythe:
                self.char.weapon = weapon.infrared_scythe
                time.sleep(.5)
                print('\nYou picked up a "Infrared Scythe" after the battle!')
            elif self.enemy.wpdrop >= 45 and self.char.weapon > weapon.infrared_katana:
                self.char.weapon = weapon.infrared_katana
                time.sleep(.5)
                print('\nYou picked up a "Infrared Katana" after the battle!')
            elif self.enemy.wpdrop >= 35 and self.char.weapon > weapon.flamed_scepter:
                self.char.weapon = weapon.flamed_scepter
                time.sleep(.5)
                print('\nYou picked up a "Flamed Scepter" after the battle!')
            elif self.enemy.wpdrop >= 30 and self.char.weapon > weapon.flamed_trident:
                self.char.weapon = weapon.flamed_trident
                time.sleep(.5)
                print('\nYou picked up a "Flamed Trident" after the battle!')
            elif self.enemy.wpdrop >= 25 and self.char.weapon > weapon.flamed_scythe:
                self.char.weapon = weapon.flamed_scythe
                time.sleep(.5)
                print('\nYou picked up a "Flamed Scythe" after the battle!')
            elif self.enemy.wpdrop >= 20 and self.char.weapon > weapon.flamed_katana:
                self.char.weapon = weapon.flamed_katana
                time.sleep(.5)
                print('\nYou picked up a "Flamed Katana" after the battle!')
            elif self.enemy.wpdrop >= 15 and self.char.weapon > weapon.scepter:
                self.char.weapon = weapon.scepter
                time.sleep(.5)
                print('\nYou picked up a "Scepter" after the battle!')
            elif self.enemy.wpdrop >= 12 and self.char.weapon > weapon.trident:
                self.char.weapon = weapon.trident
                time.sleep(.5)
                print('\nYou picked up a "Trident" after the battle!')
            elif self.enemy.wpdrop >= 9 and self.char.weapon > weapon.scythe:
                self.char.weapon = weapon.scythe
                time.sleep(.5)
                print('\nYou picked up a "Scythe" after the battle!')
            elif self.enemy.wpdrop > 6 and self.char.weapon > weapon.katana:
                self.char.weapon = weapon.katana
                time.sleep(.5)
                print('\nYou picked up a "Katana" after the battle!')
            self.char.weapon_name = self.char.weapon_dict[self.char.weapon]
            self.char.hpcount = self.enemy.hpdrop + self.char.hpcount
            time.sleep(.5)
            if self.enemy.hpdrop > 0:
                print(f'\nYou picked up {self.enemy.hpdrop}x Health Potion(s) after the battle!')

class History:
    def goblin(self):
        gob_beat = 0
        if goblin.health <= 0:
            gob_beat = gob_beat + 1
        return gob_beat
    def wolf(self):
        wolf_beat = 0
        if wolf.health <= 0:
            wolf_beat = wolf_beat + 1
        return wolf_beat
history = History()        

class Shop:
    def shop(self):
        print('\nWelcome to the shop! What would you like to purchase?')
        time.sleep(.25)
        p = input('1 = Weapons\n2 = Health Potions\n3 = Go Back\n\nEnter Here: ')
        time.sleep(.5)
        if p == '1':
            purchase = input('\nWhich weapon would you like to purchase?\n1 = Katana (20c)\n2 = Scythe (40c)\n3 = Trident (80c)\n4 = Scepter (100c)\n5 = Go back\nEnter Here: ')
            if purchase == '0':
                time.sleep(.5)
                print('\nOkay, going back!')
                time.sleep(1)
                return self.shop()
            elif purchase == '1':
                purchase_total = 20
                if purchase_total > char.coins:
                    print('\nInsufficient Funds.')
                    return self.shop()
                else:
                    char.coins = char.coins - purchase_total
                    char.weapon = weapon.katana
                    print('\nYou have successfully purchased the "Katana"!')
                    time.sleep(1)
                    print('\nNow Exiting Shop...')
            elif purchase == '2':
                purchase_total = 40
                if purchase_total > char.coins:
                    print('\nInsufficient Funds.')
                    return self.shop()
                else:
                    char.coins = char.coins - purchase_total
                    char.weapon = weapon.scythe
                    print('\nYou have successfully purchased the "Scythe"!')
                    time.sleep(1)
                    print('\nNow Exiting Shop...')
                    return self.shop()
            elif purchase == '3':
                purchase_total = 80
                if purchase_total > char.coins:
                    print('\nInsufficient Funds.')
                    return self.shop()
                else:
                    char.coins = char.coins - purchase_total
                    char.wepaon = weapon.trident
                    print('\nYou have successfully purchased the "Trident"!')
                    time.sleep(1)
                    print('\nNow Exiting Shop...')
                    return self.shop()
            elif purchase == '4':
                purchase_total = 100
                if purchase_total > char.coins:
                    print('\nInsufficient Funds.')
                    return self.shop()
                else:
                    char.coins = char.coins - purchase_total
                    char.weapon = weapon.scepter
                    print('\nYou have successfully purchased the "Scepter"!')
                    time.sleep(1)
                    print('\nNow Exiting Shop...')
                    return self.shop()
            else:
                return self.shop()
        while p == '2':
            purchase = int(input('\nHealth Potions cost 25 coins. How many would you like to purchase? (0 to go back.)\nEnter Here:'))
            if purchase == 0:
                time.sleep(.5)
                print('\nOkay, going back!')
                time.sleep(1)
                return self.shop()
            elif purchase < 0:
                print('\nCannot purchase negative amounts!')
            else:
                purchase_total = purchase *25
                if purchase_total > char.coins:
                    print('\nInsufficient Funds.')
                else:
                    char.coins = char.coins - purchase_total
                    char.hpcount = char.hpcount + purchase
                    print('\nYou have successfully purchased ' + str(purchase) + 'x Health Potion(s)!')
                    time.sleep(1)
                    print('\nNow Exiting Shop...')
                    return self.shop()
        if p == '3':
            print('\nReturning...')
            time.sleep(0.5)
            travel.travel()
shop = Shop()

class Dungeon:
    def dungeon(self):
        d = input('\nWelcome to the dungeon! Who would you like to rebattle? (Rebattle cost varies)\n1 = Goblin (7c)\n2 = Wolf(10c)\n3 = Go Back\n\nEnter Here: ')
        if d == '1':
            price = 7
            if price > char.coins:
                print('\nInsufficient Funds.')
                return self.dungeon()
            else:
                char.coins = char.coins - price
                enemy = goblin
                battle = Battle(char, enemy)
                print(f'\nA {enemy.name} approaches...')
                battle.start_battle()
                return self.dungeon()
        elif d == '2':
            if history.wolf() >= 1:
                price = 10
                if price > char.coins:
                    print('\nInsufficient Funds.')
                    return self.dungeon()
                else:
                    char.coins = char.coins - price
                    enemy = wolf
                    battle = Battle(char, enemy)
                    print(f'\nA {enemy.name} approaches...')
                    battle.start_battle()
                    return self.dungeon()
            else:
                print('Locked.')
                time.sleep(1.5)
            return self.dungeon()
        elif d == '3':
            return travel.travel()
        else:
            print('Invalid Option')
            return self.dungeon()

dungeon = Dungeon()

class Stats:
    def stats(self):
        print(f'\nHealth: {char.health}')
        print(f'Strength: {char.strength}')
        print(f'Speed: {char.speed}')
        print(f'Health Potion Count: {char.hpcount} Health Potions')
        print(f'Coin Count: {char.coins} Coins')
        print(f'Weapon: {char.weapon_name}')
        print(f'Tower Floor: Floor {tower.floor}, the {tower.floor_name}.')
        time.sleep(3)
        travel.travel()
stats = Stats()

class Travel:
    def __init__(self):
        self.tower = '1'
        self.shop = '2'
        self.dungeon = '3'
        self.stats = '4'
    
    def travel(self):
        c = input('\nWhere would you like to travel?\n1 = Tower\n2 = Shop\n3 = Dungeon\n4 = View Stats\n\nEnter Here: ')
        if c == self.tower:
            ''
        elif c == self.shop:
            shop.shop()
        elif c == self.dungeon:
            dungeon.dungeon()
        elif c == self.stats:
            stats.stats()
        else:
            print('Invalid Option')
            return self.travel()
travel = Travel()

class Tower:
    def __init__(self):
        self.floor = 0
        self.floor_name = 'Floor of Stone'
    
    
    def go(self):
        print("\n\nYou slowly approach a tower that promises fortune's at the top, however a goblin jumps in your way")
        enemy = goblin           
        battle = Battle(char, enemy)
        battle.start_battle()
        self.floor = self.floor + 1
        time.sleep(1)
        print('\nCongratulations on defeating the Goblin! You now have unlocked the shop and dungeon.')
        time.sleep(1.5)
        travel.travel()
        print('\nYou move up the tower, two Goblins outnumber you. They state that you cannot continue up the tower without')
        print('first beating them, and then their boss, a fiendish werewolf.')
        battle.start_battle()
        time.sleep(1)
        print('\nThe Second Goblin Decides to Approach...')
        battle.start_battle()
        print('\nAfter defeating the Goblins, the shadow of a monster emerges. A werewolf rushes towards you.')
        enemy = wolf
        battle = Battle(char, enemy)
        battle.start_battle()
        print('\nCongratulations on defeating the Fiendish Wolf! You have now unlocked the Fiendish Wolf in the Dungeon.')
        self.floor = self.floor + 1
        self.floor_name = 'Floor of Fire'
        time.sleep(1)
        travel.travel()
        print('You proceed to the next floor of the tower and you can feel the heat radiating from it...')
        time.sleep(1.5)
        print('A Fire Goblin is gurading the floor not even allowing you access to explore the floor...')
        enemy = fire_goblin
        battle = Battle(char, enemy)
        battle.start_battle()
        time.sleep(1)
        travel.travel()
        print('\nAs you continue to discover the floor you find a health potion.')
        char.hpcount += 1
        time.sleep(.5)
        print('You continue to scale the floor, when two Fire Goblins jump out...')
        time.sleep(1)
        battle.start_battle()
        time.sleep(.5)
        print('The other one charges at you...')
        time.sleep(1)
        battle.start_battle()
        travel.travel()

tower = Tower()
tower.go()