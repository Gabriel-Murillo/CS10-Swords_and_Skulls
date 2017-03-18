# -*- coding: utf-8 -*-
import random
import sys
import pickle

while True:
    print "------------------------------------------------------------------------"
    print "Remember to scroll up! The screen is only so big."
    break
    
while True:
    print
    print "What is your name?"
    name = raw_input("> ")
    print 
    print "------------------------------------------------------------------------"
    print
    
    if len(name) > 10:
        print "Name can be no longer than 10 characters."
        print
    elif len(name) < 1:
        print "Name has to be longer than 1 character."
    else:
        break
        print "------------------------------------------------------------------------"

print "------------------------------------------------------------------------"
print "%s the Monster Hunter" %name
print "------------------------------------------------------------------------"
#"\"Without reflection, we go blindly on our way, creating more unintended \
#consequences, and failing to achieve anything useful.\" -Margaret J. Wheatley" 
print "Our protagonist is named %s the Monster Hunter. Where ever there are \
monsters, %s is sure to be there. Most of the time, %s will accept a task and \
complete it with no hassle. Some times, however, there is more depth to the task \
than expected. %s has traveled far and wide searching for adventures to partake in." %(name, name, name, name)
print 
print "Your escapade begins in Grey Village, a small village located in the Grey \
Forest. The villagers called for you and asked for your help in dealing with the \
predator that has been killing the inhabitants of the forest. The Grey Baron has \
entrusted you with this task. "
print "------------------------------------------------------------------------"
#------------------------------------------------------------------------------- 
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

#Empty is used to identify which nodes do not have any loot available at any given time        
Empty = Item("","")
#Empty 2 is used to identify which nodes used to have loot in them
Empty2 = Item("","")
#-------------------------------------------------------------------------------
class Key(Item):
    def __init__(self, name, description):
        super(Key, self).__init__(name, description)
        
Empty_Key = Key("None", "No description")

Key1 = Key("Key", "Opens a lock nearby.")
#-------------------------------------------------------------------------------
class Counter(Item):
    def __init__(self, name, description, number):
        super(Counter, self).__init__(name, description)
        self.number = number

Movement_Counter = Counter("Movement Counter", "Used to keep track of how many \
times the player has moved.", 0)

Enemy_Counter = Counter("Enemy Counter", "Used to keep track of how many enemies \
the player has killed.", 0)

Inventory_Counter = Counter("Inventory Counter", "Used to keep track of how many \
times the player has opened their inventory.", 0)

Stats_Counter = Counter("Stats Counter", "Used to keep track of how many times \
the player has opened their inventory.", 0)

Help_Counter = Counter("Help Counter", "Used to keep track of how many times \
the player has asked for help.", 0)

Map_Counter = Counter("Map Counter", "Used to keep track of how many times \
the player looked at their map.", 0)

Misc_Counter = Counter("Misc Counter", "Used to keep track of how many misc items \
the player has collected.", 0)

Damage_Dealt = Counter("Damage Counter", "Keeps track of damage dealt by the \
player", 0)

MDamage_Dealt = Counter("Magic Damage Counter", "Keeps track of the magic damage \
dealt by the player", 0)

Damage_Taken = Counter("Damage Counter", "Keeps track of the damage taken by the \
player", 0)

MDamage_Taken = Counter("Damage Counter", "Keeps track of the magic damage taken \
by the player", 0)

Bar_Counter = Counter("Mar's Bar Counter", "Used to check if the player has obtained a \
drink or not from Mar.", 0)

Candle_Counter = Counter("Candle Counter", "Used to keep track of how many puzzles \
the player has solved", 0)

APuzzle = Counter("Puzzle A Counter", "I'm too lazy to write a description", 0) #The "counter" descriptions will never be read in game.

BPuzzle = Counter("Puzzle A Counter", "I'm too lazy to write a description", 0)

CPuzzle = Counter("Puzzle A Counter", "Descriptions don't matter for counters.", 0)
#-------------------------------------------------------------------------------
class Misc(Item):
    def __init__(self, name, description):
        super(Misc, self).__init__(name, description)
        
Flower_Pot = Misc("Flower Pot", "A small container, typically with sloping sides \
and made from plastic or earthenware, used for growing a plant in.")

Bed = Misc("Bed", "A piece of furniture for sleep or rest, typically a framework \
with a mattress and coverings.")

Blanket = Misc("Blanket", "A large piece of woolen or similar material used as a \
bed covering or other covering for warmth.")

Book = Misc("Book", "A written or printed work consisting of pages glued or sewn \
together along one side and bound in covers.")

Bookcase = Misc("Bookcase", "A set of shelves for books set in a surrounding frame \
or cabinet.")

Shotglass = Misc("Shot glass", "A small glass used for serving liquor.")

Rug = Misc("Rug", "A floor covering of thick woven material or animal skin, \
typically not extending over the entire floor.")

Sofa = Misc("Sofa", "A long upholstered seat with a back and arms, for two or more \
people.")

Apple = Misc("Apple", "The round fruit of a tree of the rose family, which typically \
has thin red or green skin and crisp flesh. Many varieties have been developed as \
dessert or cooking fruit or for making cider.")

Gnome = Misc("Gnome", "A legendary dwarfish creature supposed to guard the earth's \
treasures underground.")

Spatula = Misc("Spatula", "an implement with a broad, flat, blunt blade, used for \
mixing and spreading things, especially in cooking and painting.")

Chair = Misc("Chair", "a separate seat for one person, typically with a back and \
four legs.")

Human_Skull = Misc("Human Skull", "A skull belonging to a human being.")
#-------------------------------------------------------------------------------       
class Quest(Item):
    def __init__(self, name, description):
        super(Quest, self).__init__(name, description)

Empty_Quest = Quest("None", "You are currently not in a quest.")

WerewolfQ = Quest("Dire Wolves", "The werewolves of Grey Forest have been causing \
immense unrest among the population of Grey Village. First, they started killing anyone \
who dared exit the safety of the village. The next thing you know, they raided the village, \
killing off half of its population. You have been hired by the Grey Baron to \
hunt down and kill the leader of the pack, thus causing the rest to disperse and bother \
the village no more. You will be rewarded for completing the task. The leader of \
the pack is hiding out in The Wolf's Den. However, if you go there now you will be \
killed, you need better armor. Rumors floating around state that a set of dryad \
armor lies in Lake Azure...")

PhoenixQ = Quest("Conflagration Termination", "The monsters of Red Mountain have \
relentlessly attempted destroying all of Red Town. The only thing standing in \
their way is the Red Chief's Army. However, it will not last, it will perish if \
something is not done immediately. You will go into Red Mountain, north of Red Town, \
and kill the beasts that populate it. There must be a leader commanding the monstrous \
forces. More likely than not, it will be at the summit of Red Mountain.")

PhoenixQ_Updated = Quest("Conflagration Termination", "The monsters of Red Mountain \
have relentlessly attempted destroying all of Red Town. The only thing standing \
in their way is the Red Chief's Army. However, it will not last, it will perish \
if something is not done immediately. You will go into Red Mountain, north of Red \
Town, and kill the beasts that populate it. There must be a leader commanding the \
monstrous forces. More likely than not, it will be at the summit of Red Mountain. \
UPDATE: Go to the Chief's Palace to receive your reward.")
#-------------------------------------------------------------------------------
class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)
#-------------------------------------------------------------------------------        
class Physical(Weapon):
    def __init__(self, name, description, damage):
        super(Physical, self).__init__(name, description)
        self.damage = damage

Empty_Physical = Physical("None", "No description", 0)

Claw = Physical("Claw", "Sharp claws capable of cutting a human body in half with one swing", 10)

Player_Sword = Physical("%s's Sword" %name, "%s's razor-edged sword." %name, 0)

Viper_Sword = Physical("Viper Sword", "Deadly and agile, just like a viper. Crafted \
by the blacksmiths of Grey Village for you as a reward for the Werewolf Quest.", 10)

Red_Sword = Physical("Red's Knight Sword", "Great at killing things.", 20)

Obsidian_Sword = Physical("Obsidian Sword", "An ancient weapon used by the Knights \
of Red to repel the beasts of The Mountain.", 20)

Phoenix_Sword = Physical("Phoenix Sword", "Conceived by the Fire Elementals of The \
Mountain. This weapon of yore is able to kill the Corrupted Phoenix.", 30)
#-------------------------------------------------------------------------------
class Magical(Weapon):
    def __init__(self, name, description, magic_damage):
        super(Magical, self).__init__(name, description)
        self.magic_damage = magic_damage

Empty_Magical = Magical("None","",0)

Player_Skull = Magical("%s's Lifedraining Skull" %name, "%s's artifact used in draining health." %name, 0)

Emerald_Skull = Magical("Emerald Skull", "A dwarven skull enchanted with necrotic \
life draining magic by the mages of the forest.", 10)

Ruby_Skull = Magical("Ruby Skull", "A phoenix's skull infused with necrotic life \
draining magic by the witches of Red Mountain", 20)
#-------------------------------------------------------------------------------
class Armor(Item):
    def __init__(self, name, description, defense):
        super(Armor, self).__init__(name, description)
        self.defense = defense
#-------------------------------------------------------------------------------
class Headgear(Armor):
    def __init__(self, name, description, defense):
        super(Headgear, self).__init__(name, description, defense)
        
Empty_Helmet = Headgear("None", "No headgear equipped.", 0) 

Werewolf_Mask = Headgear("Legendary Werewolf Mask", "A mask carved from the face \
of The Grey Wolf. A trophy for your adventure.", 20)

Phoenix_Mask = Headgear("Phoenix Mask", "A mask carved from the face of a black \
phoenix. Strong and sturdy.", 30)
#-------------------------------------------------------------------------------    
class Chest(Armor):
    def __init__(self, name, description, defense):
        super(Chest, self).__init__(name, description, defense)

Empty_Chest = Chest("None", "No chest piece equipped.", 0)  

Starter_Chest = Chest("%s's Chestpiece" %name, "%s's chain link chestpiece." %name, 0)      

Dryad_Chest = Chest("Dryad's Chestplate", "Crafted by the dryads of the forest. \
Only the finest and strongest oak wood was used in the making of this chestplate.", 10)

Red_Chest = Chest("Red's Chest", "This legendary chestplate belonged to the Red \
Knight.", 20)

Red_Chest2 = Chest("Red's Improved Chest", "This improved legendary chestplate \
belonged to the Red Knight. You found it!", 21)
#-------------------------------------------------------------------------------    
class Gauntlets(Armor):
    def __init__(self, name, description, defense):
        super(Gauntlets, self).__init__(name, description, defense)

Empty_Gauntlets = Gauntlets("None", "No gauntlets equipped.", 0)   

Starter_Gauntlets = Gauntlets("%s's Gauntlets" %name, "%s's chain link gauntlets." %name, 0) 

Dryad_Gauntlets = Gauntlets("Dryad's Gauntlets", "Crafted by the dryads of the forest. \
Only the finest and strongest oak wood was used in the making of these gauntlets.", 10)

Red_Gauntlets = Gauntlets("Red's Gauntlets", "These gloves, crafted with the fire \
crystals of the mountain, were worn by the Red Knight himself.", 20)

Red_Gauntlets2 = Gauntlets("Red's Improved Gauntlets", "These improved gloves, \
crafted with the fire crystals of the mountain, were worn by the Red Knight himself.", 21)
#-------------------------------------------------------------------------------
class Boots(Armor):
    def __init__(self, name, description, defense):
        super(Boots, self).__init__(name, description, defense)

Empty_Boots = Boots("None", "No boots equipped.", 0)

Starter_Boots = Boots("%s's Boots" %name, "%s's chain link boots." %name, 0) 

Dryad_Boots = Boots("Dryad's Boots", "Crafted by the dryads of the forest. Only \
the finest and strongest oak wood was used in the making of these boots.", 10) 

Red_Boots = Boots("Red's Boots", "According to legend, these boots were worn by \
the Red Knight during the Siege of Red Summit. Crafted with the sturdiest fire \
crystals of the mountain.", 20)

Red_Boots2 = Boots("Red's Improved Boots", "According to legend, these improved boots were \
worn by the Red Knight during the Siege of Red Summit. Crafted with the sturdiest \
fire crystals of the mountain.", 21)
#-------------------------------------------------------------------------------  
#Contains the constructor for the "player"
class Player(object):
    def __init__(self, name, level, xp, health, max_health, magic, max_magic, defense, damage, magic_damage, physical, magical, headgear, chest, gauntlets, boots, quest, other, miscellaneous):
        
        self.name = name
        self.xp = xp
        self.level = level
        self.health = health
        self.magic = magic
        self.max_magic = max_magic
        self.max_health = max_health
        self.defense = defense
        self.damage = damage 
        self.magic_damage = magic_damage
        self.physical = physical
        self.magical = magical
        self.headgear = headgear
        self.chest = chest
        self.gauntlets = gauntlets
        self.boots = boots
        self.other = other
        self.quest = quest
        self.miscellaneous = miscellaneous
#------------------------------------------------------------------------------- 
#Stops the player from healing themselves more than they are allowed to.    
    def balance_health(self):
        if self.health > self.max_health:
            self.health = self.max_health            
#-------------------------------------------------------------------------------        
    def enemy_xp(self, enemy):
        '''
        You will earn a certain amount of experience points (xp) depending on the level of the enemy that you defeated.
        The higher their level, the higher the amount of xp you will obtain.
        '''
        self.xp += enemy.exp
#------------------------------------------------------------------------------- 
#After the end of every enemy encounter, the player will receive certain xp           
    def xp_earned(self, enemy):
        print "player earned %s XP" %enemy.exp
#-------------------------------------------------------------------------------                            
    def turn_based(self, enemy):
        '''
        The combat system. The player will attack first and then the enemy will attack. The player will 
        exit combat when either the player or the enemy have been defeated. A defeat will result in a GAME OVER.
        UPDATE: 3.18.2017. I forgot to delete "--WIP--" when I finished the project. Now it is deleted.
        '''
            
        if enemy.health > 0:
            
            physical = self.physical
            magical = self.magical
            headgear = self.headgear
            chest = self.chest
            gauntlets = self.gauntlets
            boots = self.boots
            
            e_physical = enemy.physical
            e_magical = enemy.magical
            e_headgear = enemy.headgear
            e_chest = enemy.chest
            e_gauntlets = enemy.gauntlets
            e_boots = enemy.boots
                
            print
            print "%s VS %s" %(self.name, enemy.name)
            print "----------------------------------------------"
            self.balance_health()
            print "> %s the Monster Hunter <" %name 
            print "LV: %s" %self.level
            print "HP: %s / %s" %(self.health, self.max_health)
            print "MP: %s" %self.magic 
            print "DEF: %s" %(self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
            print "DMG: %s" %self.damage
            print "Magic DMG: %s" %self.magic_damage
            print "Physical Weapon: %s" %physical.name
            print "Magical Weapon: %s" %magical.name
            print "headgear: %s" %headgear.name
            print "Chest: %s" %chest.name
            print "Gauntlets: %s" %gauntlets.name
            print "Boots: %s" %boots.name
            print "----------------------------------------------"
            enemy.e_balance_health()
            print "> %s <" %enemy.name
            print "LV: %s" %enemy.level
            print "HP: %s / %s" %(enemy.health, enemy.max_health)
            print "DEF: %s" %enemy.defense
            print "DMG: %s" %enemy.damage
            print "Magic DMG: %s" %enemy.magic_damage
            print "Description: %s" %enemy.description
            print "Physical Weapon: %s" %e_physical.name
            print "Magical Weapon: %s" %e_magical.name
            print "Helmet: %s" %e_headgear.name
            print "Chest: %s" %e_chest.name
            print "Gauntlets: %s" %e_gauntlets.name
            print "Boots: %s" %e_boots.name
            print "----------------------------------------------"
            
            while enemy.health > 0:
                print
                print "Available options: "
                print "1: Attack"
                print "2: Life Steal"
                print "3: Randomality" 
                print
                print "Select an option by typing 1, 2, or 3."
                command = raw_input("> ").strip().lower()
                
                if "1" in command:
                    print "----------------------------------------------"
                    print "%s attacked with the %s" %(name, physical.name)
                    #(random_n) dictates which option the enemy will attack with. 
                    #There is a total of three options
                    n = [1, 2, 3]
                    random_n = random.choice(n)
                    p_damage = self.damage - (enemy.defense + e_headgear.defense + e_chest.defense + e_gauntlets.defense + e_boots.defense) + physical.damage
                    enemy.health -= round(p_damage)
                    
                    Damage_Dealt.number += round(p_damage)
                    
                    if random_n == 1:
                        e_damage = (enemy.damage + e_physical.damage) - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s attacked with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                        
                    if random_n == 2:
                        modified_damage = (enemy.magic_damage + e_magical.magic_damage)*.70
                        hp_gain = modified_damage*.30
                        e_damage = modified_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        enemy.e_balance_health()
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        enemy.health += round(hp_gain)
                        print "----------------------------------------------"
                        print "%s drained your HP with the %s" %(enemy.name, e_magical.name)
                        MDamage_Taken.number += round(e_damage)
                        
                    if random_n == 3:
                        numbers = [3, 4, 5]
                        random_n = random.choice(numbers)
                        modified1 = (enemy.damage + e_physical.damage) / 5
                        modified2 = modified1*.25 + modified1
                        e_damage = modified2 * random_n
                        e_damage = e_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s used randomality with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                    print "----------------------------------------------"
                    enemy.e_balance_health()
                    print "%s dealt %s DMG" %(self.name, round(p_damage))
                    print "%s has %s HP" %(enemy.name, round(enemy.health))
                    print "----------------------------------------------"
                    self.balance_health()
                    print "%s dealt %s DMG" %(enemy.name, round(e_damage))
                    print "%s has %s HP" %(self.name, round(self.health))
                    print "----------------------------------------------"  
                
                if "2" in command and self.magic <= 0:  
                    print "------------------------------------------------------------------------"  
                    print "You do not have enough magic to drain your opponent's life"
                    print "------------------------------------------------------------------------"
                          
                if "2" in command and self.magic > 0:
                    self.magic -= 25
                    print "----------------------------------------------"
                    print "%s used the %s for lifedrain" %(name, magical.name)
                    n = [1, 2, 3]
                    random_n = random.choice(n)
                    modified_damage = (self.magic_damage + magical.magic_damage)*.70
                    hp_gain = modified_damage*.32
                    p_damage = modified_damage - (enemy.defense + e_headgear.defense + e_chest.defense + e_gauntlets.defense + e_boots.defense)
                    
                    enemy.health -= round(p_damage)
                    self.health += round(hp_gain)
                    
                    MDamage_Dealt.number += round(p_damage)
                    
                    if random_n == 1:
                        e_damage = (enemy.damage + e_physical.damage) - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s attacked with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                    if random_n == 2:
                        
                        modified_damage = (enemy.magic_damage + e_magical.magic_damage)*.70
                        hp_gain = modified_damage*.30
                        e_damage = modified_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        enemy.e_balance_health()
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        enemy.health += round(hp_gain)
                        print "----------------------------------------------"
                        print "%s drained your HP with the %s" %(enemy.name, e_magical.name)
                        MDamage_Taken.number += round(e_damage)
                        
                    if random_n == 3:
                        numbers = [3, 4, 5]
                        random_n = random.choice(numbers)
                        modified1 = (enemy.damage + e_physical.damage) / 5
                        modified2 = modified1*.25 + modified1
                        e_damage = modified2 * random_n
                        e_damage = e_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s used randomality with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                    print "----------------------------------------------"
                    self.balance_health()
                    enemy.e_balance_health()
                    print "%s dealt %s DMG" %(name, round(p_damage))
                    print "%s drained %s HP from %s" %(name, round(hp_gain), enemy.name)
                    print "%s has %s HP" %(enemy.name, enemy.health)
                    print "----------------------------------------------"
                    self.balance_health()
                    print "%s dealt %s DMG" %(enemy.name, round(e_damage))
                    print "%s has %s HP" %(self.name, self.health)
                    print "----------------------------------------------"
                    
                if "3" in command:
                    print "----------------------------------------------"
                    print "%s used randomality with the %s" %(name, physical.name)
                    n = [1, 2, 3]
                    random_n = random.choice(n)
                    
                    numbers = [3.8, 3.9, 4, 4.1, 4.2, 4.3, 4.4, 4.5]
                    random_num = random.choice(numbers)
                    modified1 = (self.damage + physical.damage)/ 5
                    modified2 = modified1*.20 + modified1
                    e_damage = modified2 * random_num
                    p_damage = e_damage - (enemy.defense + e_headgear.defense + e_chest.defense + e_gauntlets.defense + e_boots.defense)
                    enemy.health -= round(p_damage)
                    
                    Damage_Dealt.number += round(p_damage)
                    
                    if random_n == 1:
                        e_damage = (enemy.damage + e_physical.damage) - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s attacked with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                    if random_n == 2:
                        modified_damage = (enemy.magic_damage + e_magical.magic_damage)*.70
                        hp_gain = modified_damage*.30
                        e_damage = modified_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        enemy.e_balance_health()
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        enemy.health += round(hp_gain)
                        print "----------------------------------------------"
                        print "%s drained your HP with the %s" %(enemy.name, e_magical.name)
                        MDamage_Taken.number += round(e_damage)
                        
                    if random_n == 3:
                        e_numbers = [3, 4, 5]
                        random_num = random.choice(e_numbers)
                        modified1 = (enemy.damage + e_physical.damage) / 5
                        modified2 = modified1*.25 + modified1
                        e_damage = modified2 * random_num
                        e_damage = e_damage - (self.defense + headgear.defense + chest.defense + gauntlets.defense + boots.defense)
                        if e_damage < 0:
                            e_damage = 1
                        self.health -= round(e_damage)
                        print "----------------------------------------------"
                        print "%s used randomality with the %s" %(enemy.name, e_physical.name)
                        Damage_Taken.number += round(e_damage)
                        
                    enemy.e_balance_health()
                    print "----------------------------------------------"
                    print "%s dealt %s DMG" %(name, round(p_damage))
                    print "%s has %s HP" %(enemy.name, enemy.health)
                    print "----------------------------------------------"
                    self.balance_health()
                    print "%s dealt %s DMG" %(enemy.name, round(e_damage))
                    print "%s has %s HP" %(self.name, self.health)
                    print "----------------------------------------------"
                    
                if 'failsafe' in command:
                    break
                    
                if self.health <= 0:
                    print "Game Over"
                    sys.exit(0)
            
            else:
                Enemy_Counter.number += 1 
                print
                self.enemy_xp(enemy)
                numbers = [1,2,3,4,5]
                r_numbers = random.choice(numbers)
                if r_numbers == 1:
                    print "%s was slayed by %s" %(enemy.name, self.name)
                    
                if r_numbers == 2:
                    print "%s was annihilated by %s" %(enemy.name, self.name)
                    
                if r_numbers == 3:
                    print "%s was massacred by %s" %(enemy.name, self.name)
                    
                if r_numbers == 4:
                    print "%s was demolished by %s" %(enemy.name, self.name)
                    
                if r_numbers == 5:
                    print "%s was killed by %s" %(enemy.name, self.name) 
                    
                player.xp_earned(enemy)
                player.magic = player.max_magic
                
#-------------------------------------------------------------------------------  
#NAME LEVEL XP HEALTH MAXHEALTH MAGIC MAXMAGIC DEFENSE DAMAGE MAGICDAMAGE 
#Here lies the player's stats                             
player = Player(name, 1, 0, \
200.0, 200.0, 50.0, 50.0, 50.0, 100.0, 100.0, Player_Sword, Player_Skull, Empty_Helmet, Starter_Chest, Starter_Gauntlets, Starter_Boots, WerewolfQ, Empty_Key, [])
#-------------------------------------------------------------------------------   
#Contains the constructor for the "enemy"
class Enemy(object):
    def __init__(self, name, level, exp, description, health, max_health, defense, damage, magic_damage, physical, magical, headgear, chest, gauntlets, boots):
        self.name = name
        self.level = level
        self.exp = exp
        self.description = description
        self.health = health
        self.max_health = max_health
        self.defense = defense
        self.damage = damage
        self.magic_damage = damage
        self.physical = physical
        self.magical = magical
        self.headgear = headgear
        self.chest = chest
        self.gauntlets = gauntlets
        self.boots = boots
#-------------------------------------------------------------------------------  
#Stops an enemy from healing more health than they should      
    def e_balance_health(enemy):
        if enemy.health > enemy.max_health:
            enemy.health = enemy.max_health
#-------------------------------------------------------------------------------
#NAME EXP DESCRIPTION 
#HEALTH MAXHEALTH DEFENSE DAMAGE MAGICDAMAGE 

#CHAPTER ONE ENEMIES
Werewolf1 = Enemy("Werewolf", 1, 20, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
100.0, 100.0, 50.0, 60.0, 70.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Dryad1 = Enemy("Dryad", 1, 10, "Normally bashful, they will act exceedingly \
hostile to anyone or anything that poses a threat to their forest.",
100.0, 100.0, 50.0, 70.0, 70.0, Empty_Physical, Emerald_Skull, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Werewolf2 = Enemy("Werewolf", 1, 10, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
105.0, 105.0, 50.0, 60.0, 70.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Werewolf3 = Enemy("Werewolf", 2, 10, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.", 
105.0, 105.0, 50.0, 100.0, 110.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Werewolf4 = Enemy("The Grey Wolf", 3, 20, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
165.0, 165.0, 55.0, 100.0, 110.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Sorcerer1 = Enemy("One the Sorcerer", 1, 10, "A human possesing magical attributes. ",
105.0, 105.0, 45.0, 90.0, 80.0, Empty_Physical, Emerald_Skull, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Sorcerer2 = Enemy("Two the Sorcerer", 1, 10, "A human possesing magical attributes. ",
105.0, 105.0, 45.0, 90.0, 80.0, Empty_Physical, Emerald_Skull, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

#CHAPTER TWO ENEMIES
Phoenix1 = Enemy("Injured Phoenix", 3, 10, "Once believed to be a myth and a symbol \
of hope. The harprognatus exincendia was found residing in Red Mountain and it was \
awoken by the populace of Red Town. As a result, they now leave their homes to \
hunt those who dared disturb them.",
90.0, 110.0, 50.0, 105.0, 90.0, Empty_Physical, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Phoenix2 = Enemy("Phoenix", 3, 10, "Once believed to be a myth and a symbol of hope. \
The harprognatus exincendia was found residing in Red Mountain and it was awoken \
by the populace of Red Town. As a result, they now leave their homes to hunt those \
who dared disturb them.",
120.0, 120.0, 50.0, 110.0, 110.0, Empty_Physical, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Bat1 = Enemy("Fire Bat", 2, 10, "A huge, ​flying ​animal with ​big ​ears and ​wings of fire & ​skin",
120.0, 120.0, 50.0, 110.0, 110.0, Empty_Physical, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Bat2 = Enemy("Fire Bat", 2, 10, "A huge, ​flying ​animal with ​big ​ears and ​wings of fire & ​skin",
120.0, 120.0, 50.0, 110.0,110.0, Empty_Physical, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Bat3 = Enemy("Fire Bat", 2, 10, "A huge, ​flying ​animal with ​big ​ears and ​wings of fire & ​skin",
120.0, 120.0, 60.0, 110.0, 110.0, Empty_Physical, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Knight1 = Enemy("Eldrith the Red Knight", 4, 20, "A knight belonging to the highest \
rank of the Knights of Red. What is he doing here?", 
150.0, 150.0, 50.0, 100.0, 125.0, Red_Sword, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Knight2 = Enemy("Almerth the Red Knight", 4, 20, "A knight belonging to the highest \
rank of the Knights of Red. What is he doing here?", 
150.0, 150.0, 50.0, 100.0, 125.0, Red_Sword, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Red_Boots)

Knight3 = Enemy("Kanthos the Red Knight", 4, 20, "A knight belonging to the highest \
rank of the Knights of Red. What is he doing here?", 
150.0, 150.0, 60.0, 105.0, 125.0, Red_Sword, Empty_Magical, Empty_Helmet, Empty_Chest, Red_Gauntlets, Empty_Boots)

Knight4 = Enemy("Resmoth the Red Knight", 4, 20, "A knight belonging to the highest \
rank of the Knights of Red. What is he doing here?", 
160.0, 160.0, 60.0, 105.0, 125.0, Red_Sword, Empty_Magical, Empty_Helmet, Red_Chest, Empty_Gauntlets, Empty_Boots)

Avis = Enemy("Nigra Avis", 4, 20, "One of a kind. The Black Bird species was \
pushed to extinction due to their sturdy beaks and beautiful feathers being so \
rare and luxurious. There is only one left!",
200.0, 200.0, 60.0, 120.0, 130.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

Red = Enemy("Red", 5, 50, "A man turned into a demon. His hatred for people led \
him to establishing his base in Red Mountain and selling the world his death and \
the death of his knights. Now, alongside with the Knights of Red, he is a human \
transformed into a monster, a demon. Hatred transforms.",
200.0, 200.0, 30.0, 135.0, 155.0, Phoenix_Sword, Ruby_Skull, Empty_Helmet, Red_Chest, Red_Gauntlets, Red_Boots)

#RANDOM ENCOUNTERS
WerewolfR1 = Enemy("Werewolf", 1, 2, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
55.0, 55.0, 50.0, 45.0, 60.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

WerewolfR2 = Enemy("Werewolf", 1, 2, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
55.0, 55.0, 50.0, 45.0, 60.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

WerewolfR3 = Enemy("Werewolf", 1, 2, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
55.0, 55.0, 50.0, 45.0, 60.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)

WerewolfR4 = Enemy("Werewolf", 1, 2, "A cursed individual, a lycanthrope, with the \
the ability to transmute into a wolf-like creature.",
55.0, 55.0, 50.0, 45.0, 60.0, Claw, Empty_Magical, Empty_Helmet, Empty_Chest, Empty_Gauntlets, Empty_Boots)
#-------------------------------------------------------------------------------   
#Contains the constructor for the various rooms in the game
class Room:
    def __init__(self, domain, name, north, south, east, west, up, down, loot, description):
        self.domain = domain
        self.name = name 
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west             
        self.up= up
        self.down = down
        self.loot = loot
#-------------------------------------------------------------------------------    
#globals() is what makes player movement possible    
    def move(self, direction):
        while True:
            global node
            node = globals()[getattr(self, direction)]   
            break
#-------------------------------------------------------------------------------
#ROOMS1 
#Chapter 1
#NAME NORTH SOUTH EAST WEST UP DOWN LOOT DESCRIPTION

Grey_Baron = Room("Grey Village", "The Grey Baron's Manor", None, None, "Residential", None, None, None, [Flower_Pot, Book],
"You are inside the Grey Baron's manor in the forest. You clutch the parchment \
in your hand. You will hunt down and slaughter the werewolves of Grey Forest. \
The creatures of the forest will not be accepting of your slaughter, you will face \
opposition from the various monsters that populate Grey Forest. Open your inventory \
and examine your current quest.")

Residential = Room("Grey Village", "Residential Area", "Path_Junction", "Burial_Grounds", "Market", None, None, None, [Blanket],
"You are in the residential area of Grey Village. The people of the village are hidden \
away in their homes, fearful for another raid on the village by the beasts of the forest.")

Market = Room("Grey Village", "Marketplace", "Weaponsmith", "Fruit", "Bar", "Residential", None, None, [Chair, Spatula],
"You are in Grey Village's Marketplace, where you can find anything from weapons \
to a cold drink. This place is empty, the werewolves made sure of that.")

Weaponsmith = Room("Grey Village", "The Weaponsmith's", None, "Market", None, None, None, None, [Rug], 
"You are inside The Weaponsmith's, a weapons shop. Polished & metallic swords dangle \
on the wall, they are nothing but aesthetics. Bulky armor fills the stands, it would \
be nearly impossible to move in that. It is obvious that the gear sold in this \
store is crap compared to your monster hunting arsenal.")

Fruit = Room("Grey Village", "The Fruitstands", "Market", None, None, None, None, None, [Apple],
"Imagine a beautiful alignment of colorful fruit, positioned with immense precision. \
Each fruit is perfectly round. Each fruit is vivid and radiating with alluring \
coloration. Now, throw all of that away, and imagine a pathetic assortment of rotten \
crop. Actually, there is no need to imagine the revolting imagery, %s, you are looking \
right at it. " %name)

Bar = Room("Grey Village", "Mar's Bar", None, None, None, "Market", None, None, [Shotglass],
"You are inside the Mar's Bar, the village's most popular social center. Come back \
later for a free drink, eh?")

Burial_Grounds = Room("Grey Village", "Burial Grounds", "Residential", None, None, None, None, None, [Gnome],
"You are in the burial grounds. The death rate of the populace has seen a considerable \
increment in the last couple of weeks. That werewolf has caused great devastation \
among the population. Both the creatures of the forest and the inhabitants of the \
village have been suffering due to the great threat the werewolves have imposed.")

Path_Junction = Room("Grey Village", "Path to the Junction", "Junction", "Residential", None, None, None, None, [Empty],
"You are on the path to the Junction, where four paths meet.")

Path_Junction2 = Room("Grey Forest", "Path to Grey Village", "Junction", "Residential", None, None, None, None, [Empty],
"You are on the path to Grey Village.")

Junction = Room("Grey Forest", "Junction", "Road_Red", "Path_Junction2", "Path_Lake", "Path_Wolf", None, None, [Empty],
"You are in the Junction, where four paths meet. The path to the east leads to Lake \
Azure, Grey Forest's most alluring natural attraction. The path to the west leads to \
The Wolf's Den, Grey Forest's most dangerous cave. The path to the south will take you \
to Grey Village. The road to the north will lead you to Red Mountain.")

Path_Lake = Room("Grey Forest", "Path to Lake Azure", None, None, "West_Lake", "Junction", None, None, [Empty],
"You are on the path to Lake Azure, the lush area of the Grey Forest. ")

Path_Lake2 = Room("Grey's Forest", "Path to the Junction", None, None, "West_Lake", "Junction", None, None, [Empty],
"You are on the path to the Junction, where four paths meet.")

West_Lake = Room("Grey Forest", "West of Lake Azure", "North_Lake", "South_Lake", "Lake_Azure", "Path_Lake2", None, None, [Empty],
"You are west of Lake Azure. The trees are taller than the giants of yore and their \
leaves sharper than the blades of knights. The grass is considerably greener in \
this area than on The Wolves Den. This area is also safer than The Wolves Den. \
You notice footprints leading to the southern area of Lake Azure.")

North_Lake = Room("Grey Forest", "North of Lake Azure", "Flower_Bed", "Lake_Azure", "East_Lake", "West_Lake", None, None, [Empty],
"You are north of Lake Azure. The understory is overpopulated with rich flora & \
fauna. Colorful flowers and rotten corpses situate themselves on the forest's floor.")

Flower_Bed = Room("Grey Forest", "Flower Bed", None, "North_Lake", None, None, None, None, [Dryad_Boots],
"You found the dryad's shrine, a luscious flower bed of various plants and colorful \
flowers. A shrine commemorated by the townspeople of Grey Village to honor the dryad's \
efforts to keep the forest \"safe\". You spot a glassy and viridescent chest. Based \
on the markings and the color of the chest, it belongs to the dryads of the forest.")

East_Lake = Room("Grey Forest", "East of Lake Azure", "North_Lake", "South_Lake", "Cave_East_Lake", "Lake_Azure", None, None, [Empty],
"You are east of Lake Azure. The shadow casted by the canopy is darker than the \
night itself. Although the environment is obscured, you spot footprints leading \
to a cave to the east.")

Cave_East_Lake = Room("Grey Forest", "Cave", "Hidden_Room_Lake", None, None, "East_Lake", None, None, [Empty],
"You are inside a cave found east of Lake Azure. You spot a pair of tattered pants \
on top a stalagmite. Deep scratch marks fill the walls. Taupe colored hair lies on \
the cave's floor. It is apparent that lycanthropy took place here. There are \
eerie sounds emerging deep within the cave, they more than likely belong to a \
lycanthrope...") 

Hidden_Room_Lake = Room("Grey Forest", "Hidden Room", None, "Cave_East_Lake", None, None, None, None, [Dryad_Gauntlets],
"You found the cave's hidden room. It is pitch-black, however you make out a faint \
glow of a polished and verdant chest. Chests like these are scattered everywhere, \
left behind by the monsters of the area. In this case, it appears to be a chest \
belonging to a dryad based on the markings and the color.")

South_Lake = Room("Grey Forest", "South of Lake Azure", "Lake_Azure", "Hut", "East_Lake", "West_Lake", None, None, [Empty],
"You are south of Lake Azure. The darkest night would never be able to out match \
the canopy's shade. Thick roots encapsulate deteoriating corpses, clutching them \
thightly. You identify the same footprints that you saw earlier, this time leading \
to the east of Lake Azure.")

Hut = Room("Grey Forest", "Wooden Hut", "South_Lake", None, None, None, None, "Basement_Hut", [Sofa],
"You are inside what appears to be a hut that once belonged to a citizen on Grey Village. \
He didn't manage to leave the forest alive, or his hut, based on the walls being \
covered in human blood, the werewolves must have taken his body to their den. A \
decapitated dryad lies dead on the floor. There is a trail of blood, monster blood, \
leading downstairs.")

Basement_Hut = Room("Grey Forest", "Basement", None, None, None, None, "Hut", None, [Dryad_Chest],
"You are in the hut's basement. It is rather dark down here. The dryad's head lies on \
the basement's floor. There is a jade colored chest, the dryad must have died protecting \
it. What ever is in it must have been important to it. The stairs will take you \
upstairs.")

Lake_Azure = Room("Grey Forest", "Lake Azure", "North_Lake", "South_Lake", "East_Lake", "West_Lake", None, None, [Empty],
"You are swimming in Lake Azure. The water is pristine, the nymphs of the lake \
do a fantastic job of cleansing it of any blood or dirt that may arrive. From here, \
you can swim to any location around the lake.")

Path_Wolf = Room("Grey Forest", "Path to The Wolf's Den", None, None, "Junction", None, None, None, [Empty],
"You are on the path to The Wolf's Den, the most dangerous area in Grey Forest. \
Your defense is really low, why don't you go explore? *You need better armor*")

Path_Wolf2 = Room("Grey Forest", "Path to the Junction", None, None, "Junction", "Wolf_Totem", None, None, [Empty],
"You are on the path to the Junction, where four paths meet.")

Wolf_Totem = Room("Grey Forest", "Wolf's Totem Pole", "Cave_Entrance", "Bone_Pile", "Path_Wolf2", "Necromancer_Cabin", None, None, [Emerald_Skull],
"You are south of The Wolf's Den. This location is brimming with totem poles of \
wolves. Deep scratch marks cover the totem poles, however a wolf is not strong enough \
to have produced a scrape so deep, it must have been a werewolf. You sense necrotic \
magic nearby, it is emitting from the olive colored emerald skull resting on top \
of one of the totem poles. It seems to be more powerful than your necrotic artifact.")

Necromancer_Cabin = Room("Grey Forest", "Necromancer's Cabin", None, None, "Wolf_Totem", None, "N_Upstairs", "N_Basement", [Empty],
"You are inside a cabin near The Wolf's Den. There is a variety of liquor and tomes \
spread around the room.")

N_Upstairs = Room("Grey Forest", "Upstairs", None, None, None, None, None, "Necromancer_Cabin", [Bed, Bookcase],
"You are on the cabin's second floor.")

N_Basement = Room("Grey Forest", "Basement", None, None, None, None, "Necromancer_Cabin", None, [Empty],
"You are on the cabin's basement.")

Bone_Pile = Room("Grey Forest", "Pile of Bones", "Wolf_Totem", None, None, None, None, None, [Human_Skull],
"You are in a pile of human and dryad corpses. The stench of tensomes of rotting \
bodies fill the air. The rattling of bones as you walk through them dominate the \
hushed locale.")

Cave_Entrance = Room("Grey Forest", "Den's Entrance", "Wolf_Den", "Wolf_Totem", None, None, None, None, [Empty],
"You are at the entrance of The Wolf's Den. The lair appears to be unlit and suprisingly \
quiet. Inside must be the leader of the pack. ")

Wolf_Den = Room("Grey Forest", "The Wolf's Den", None, "Cave_Entrance", None, None, None, None, [Werewolf_Mask],
"You are inside The Wolf's Den. It smells of blood and wet dog, a crippling stench. \
The Grey Wolf lies lifeless on the cave's floor. Carve its face out and wear it \
as a trophy for your exploit.")

Road_Red = Room("Grey Forest / Red Mountain", "Road to Red Mountain", None, "Junction", None, None, None, None, [Empty],
"You are on the road to Red Mountian, a domain dominated by volcanic activity. You \
can not leave Grey Forest until you have completed your quest.")

Road_Red2 = Room("Grey Forest / Red Mountain", "Road to Red Mountain", None, "Junction", None, None, None, None, [Empty],
"You are on the road to the Junction, where four paths meet.")

#-------------------------------------------------------------------------------
#ROOMS2 "CTRL + F" ME
#CHAPTER 2
#NAME NORTH SOUTH EAST WEST UP DOWN LOOT DESCRIPTION

Gate_Red = Room("Red Mountain", "The Gate", "Town_Square", "Road_Red2", None, None, None, None, [Empty],
"After hours of walking down the path, you finally reach the gates of Red Mountain, \
a domain named after the Red Knight, one of the fiercest warriors in existence. \
Go through the gates and speak with the Red Chief, he will have a quest for you.")

Town_Square = Room("Red Town", "Town Square", "Red_Stairway", None, "Chief_Palace", "Red_Market", None, None, [Empty],
"You are in Red Town's, very own, town square. This place used to be a striving \
market for ores and minerals. Now, it is a ravaged and desolate place. The marketplace \
and the Red Chief's palace are nearby.")

Red_Market = Room("Red Town", "Marketplace", "Sword_Shop", "Red_Fruit", "Town_Square", "Red_Bar", None, None, [Empty],
"You are in Red Town's marketplace. The area is on fire, the buildings have been \
demolished, and it seems like monsters have been feeding on whatever and whoever \
they come across. Corpses litter the ground.")

Sword_Shop = Room("Red Town", "The Sword Shop", None, "Red_Market", None, None, None, None, [Empty],
"You are inside what once was The Sword Shop, a place where townspeople used to \
purchase their weaponry, in case an attack from the Beasts of the Mountain occured. \
The few remaining swords are blunt and rusty.")

Red_Fruit = Room("Red Town", "The Fruitstands", "Town_Square", None, None, None, None, None, [Empty],
"You are at the fruitstands, where the people of Red Town came to buy their fresh \
product. The ground is splattered with fruit of all colors, it is a great contrast \
compared to the gray and mundane sky.")

Red_Bar = Room("Red Town", "The Red Bar", None, None, "Red_Market", None, None, None, [Empty],
"You are inside The Red Bar. You won't be receiving any free drinks this time. \
There is no one to serve you, everyone is dead.")

Chief_Palace = Room("Red Town", "Red Chief's Palace", None, None, None, "Town_Square", None, None, [PhoenixQ],
"You are inside the Red Chief's Palace. It is a colossal building with decorum \
appropiate for a wealthy leader like the Red Chief. The place looks intact, as if \
the invasion of Red Town never occured. The remaining population of the town is \
in here, they are afraid. Guards are positioned in every corner, they await the \
looming attack from Red Mountain. The Red Chief points at the coffee colored oak \
table, there is a parchment atop. It is your next quest, pick it up and read it.")

Red_Stairway = Room("Red Mountain", "Stairway to the Mountain's Interior", None , "Town_Square", None, None, None, None, [Empty],
"You are in the stone stairway leading to the dungeon hidden away the inside of \
the mountain. You spot the Burning Tree at the top of the mountain, or Red Summit. \
An inferno awaits. ")

Fog_Room = Room("Red Mountain (First Floor)", "Foggy Room", None, None, "Droppings", "Skulls_Bones", None, None, [Empty],
"You are inside the first room of Red Mountain, many more await. Your surroundings \
are obscured by a thick layer of fog. There is a door ahead, it appears to be locked.")

Droppings = Room("Red Mountain (First Floor)", "Droppings", None, None, None, "Fog_Room", None, None, [Key1],
"You walk into a room populated by harmless bats and piles of bat droppings. The \
stench of a thousand feces fills the air, it strikes your nose and triggers a wave \
of nausea. You make out the faint outline of a key amongst the piles.")

Skulls_Bones = Room("Red Mountain (First Floor)", "Skulls & Bones",  None, None, "Fog_Room", None, None, None, [Empty],
"You walk into a room populated by Fire Bats. Watch your step, the room is filled \
to the brim with skulls and bones belonging to the various adventurers that believed \
that they would be able reach the second floor intact. It is obvious that they, \
instead, met their end inside these walls. ")

Thousand_Steps = Room("Red Mountain (First Floor)", "Thousand Steps", None, None, None, None, "Dark_Room", None, [Empty],
"You are standing where no other adventurer has ever stood before, The Thousand Steps. \
Go up the stairs to reach the second floor.")

Dark_Room = Room("Red Mountain (Second Floor)", "Lights Out", None, None, "Illuminated_Passage", None, None, None, [Empty],
"You made it up the stairs. You are inside a room with only one door leading to \
the east. The torches in the room have all extinguished, no one has made it this \
far in years... and no one made it out alive.")

Illuminated_Passage = Room("Red Mountain (Second Floor)", "Illuminated Passage", "Bone_Piles", None, "Lava_LakeX", "Dark_Room", None, None, [Empty],
"You are inside a cave with no source of light other than the colossal lava lake \
to the east. There appears to be a door at the end of the lake. However, how are \
you going to travel through a lake of molten rock?")

Bone_Piles = Room("Red Mountain (Second Floor)", "Pile of Bones", None, "Illuminated_Passage", "Red_Chest1", None, None, None, [Empty],
"You are near a pile of bones. These bones belonged to the Cavernous Humanoids that \
once lived in the mountain before they were driven to exinction by the phoenixes. \
The ravenous bats have been gnawing on their bones. There is a path to the east. \
that leads to a small opening through the cave's walls.")

Red_Chest1 = Room("Red Mountain (Second Floor)", "The Room With The Boots", None, None, None, "Bone_Piles", None, None, [Red_Boots],
"You are inside a small room with nothing else but a chest. The chest is glowing \
with a bright red aura that seems to be emitting from the contents of within. Maybe \
it will hold the key to walking through the lava lake.")

Lava_LakeX = Room("Red Mountain (Second Floor)", "Lava Lake", "Stairwell", None, None, "Illuminated_Passage", None, None, [Empty],
"You are walking through the lake of fire and as you go you are taking damage. \
It is best that you return and try to find another method of going through, however \
if that is not what you want then you better go through the lake as fast as you can.")

Lava_Lake1 = Room("Red Mountain (Second Floor)", "Lava Lake", "Stairwell", None, None, "Illuminated_Passage", None, None, [Empty],
"The boots allow you to walk on lava! This reminds you of a certain someone who \
could do something similar... Who was it again?")

Stairwell = Room("Red Mountain (Second Floor)", "Stairwell", None, "Lava_LakeX", None, None, "The_Torch", None, [Empty],
"You have reached the stairwell. Climb up the stairs to reach the third floor and \
get one step closer to reaching the summit.")

The_Torch = Room("Red Mountain (Third Floor)",  "The Torch", "Puddles", None, None, None, None, None, [Empty],
"You made it. You are inside a room with a single lit torch. You sense a strange, \
but young, magical force emitting from the torch. It is evident that something \
or someone was recently here.")

Puddles = Room("Red Mountain (Third Floor)", "Puddles", None, "The_Torch", "Guattor", "Pedestal", None, None, [Empty],
"You are inside a room riddled with cracks on the walls. Lava has been slowly seeping \
through them, and puddles of molten rock have been forming.")

Pedestal = Room("Red Mountain (Third Floor)", "Sword on the Pedestal", None, None, "Puddles", None, None, None, [Obsidian_Sword],
"You are inside a room with lava gushing out of the walls, creating lavafalls. \
There is a pedestal in the center of the room, untouched by the molten rock. A \
sword is jammed in it.")

Guattor = Room("Red Mountain (Third Floor)", "Et Guattor Iudicia", "Primus", None, None, "Puddles", None, None, [Empty],
"You are inside the first of the Challenge Nodes, a set of challenges designed to \
kill off the weak. Four monsters await you.")

Primus = Room("Red Mountain (Third Floor)", "In Primo Iudicii", None, None, "Secundo", None, None, None, [Empty],
"You are in the first Challenge Node. The room looks like it could collapse at any \
second, since there is only one pillar sustaining it. You better get a move on before \
it does.")

Secundo = Room("Red Mountain (Third Floor)", "In Secundo Iudicio", None, "Tertium", None, "Primus", None, None, [Empty],
"You are in the second Challenge Node. Along the walls are severed body parts hanging \
from chains on the roof. This must serve as a warning sign for adventurers.")

Tertium = Room("Red Mountain (Third Floor)", "Tertium Temptationis", "Secundo", None, "Quartam", None, None, None, [Empty],
"You are in the third Challenge Node. There are various spikes on the walls and \
on the floor. Several of these hazards are as tall as yourself, you better watch \
where you are going before you poke an eye out.")

Quartam = Room("Red Mountain (Third Floor)", "Quartam Causam", "Reward", None, None, "Tertium", None, None, [Empty],
"You are in the fourth and final Challenge Node. On the floor, puddles of bright, \
crimson blood impede your step. Watch yourself, wouldn't want to slip and die, now?")

Reward = Room("Red Mountain (Third Floor)", "Praemium et Curare", None, None, "TStairs", None, None, None, [Red_Chest],
"You have succesfully completed all of the Challenge Nodes! Your reward lies in the \
glistening, blood soaked red chest lying on the floor. The path to the east leads \
to stairs leading upwards. ")

TStairs = Room("Red Mountain (Third Floor)", "The Stairs Leading Upwards", None, None, None, "Reward", "Three_Crystals", None, [Empty],
"The stairs will take you to the fourth floor of Red Mountain. You did a great job \
back there, it was not easy taking down those four demons. The Knights of Red sure \
put up a good fight...")

Three_Crystals = Room("Red Mountain (Fourth Floor)", "Trois Cristaux", "PuzzleA", "BPhoenix", "PuzzleB", "PuzzleC", None, None, [Empty],
"There are three dull, white crystals hanging from the ceiling. There must be a \
way of activating them somehow and thus enabling your entry to the next location.")

PuzzleA = Room("Red Mountain (Fourth Floor)", "Puzzle A", None, "Three_Crystals", None, None, None, None, [Empty],
"You are inside a room with one glowing, blue crystal hanging from the roof. There \
is also a wooden chair and table with a piece of parchment, quill, and ink.")

PuzzleB = Room("Red Mountain (Fourth Floor)", "Puzzle B", None, None, None, "Three_Crystals", None, None, [Empty],
"You are inside a room with one glowing, green crystal hanging from the roof. There \
is also a wooden chair and table with a piece of parchment, quill, and ink.")

PuzzleC = Room("Red Mountain (Fourth Floor)", "Puzzle C", None, None, "Three_Crystals", None, None, None, [Empty],
"You are inside a room with one glowing, red crystal hanging from the roof. There \
is also a wooden chair and table with a piece of parchment, quill, and ink.")

BPhoenix = Room("Red Mountain (Fourth Floor)", "Nigrum Avem's Cell", "Three_Crystals", None, None, None, None, None, [Phoenix_Mask, Red_Gauntlets, Phoenix_Sword, Ruby_Skull],
"You enter a room to the south. You are inside what appears to have once been a \
treasure room. There is a ginormous red chest in front of you. You are able to \
deduce that this treasure room belongs to the Knights of Red based on the ancient \
markings and carvings on the rim. Gold coins and platinum trophies litter the floor, \
however, none of this filthy currency matters to a monster hunter like you, of course. ")

To_Summit = Room("Red Mountain (Fourth Floor)", "Stairs to Red Summit", None, "Three_Crystals", None, None, "Foot_Prints", None, [Empty],
"You are standing on the phantom stairs. The staircase leads to the summit of Red \
Mountain, also known as Red Summit, the most dangerous location of Red Mountain.")

Foot_Prints = Room("Red Summit", "Bellum", None, "Burning_Tree", None, None, None, None, [Empty],
"You went up the stairs and exited the dungeon within Red Mountain. The boss should \
be around here somewhere. You spot footprints on the ground leading to the south. \
You feel uneasy, like there is something wrong. What have you been doing all of \
this time?")

Burning_Tree = Room("Red Summit", "Tree on Fire", "Foot_Prints", None, "Dark_Figure", "Vanished", None, None, [Empty],
"You are near a burning tree. The sky is darker than it has ever been. The moon, \
like the stars, is absent from the nightime sky. The tree illuminates the surrounding \
area, allowing you to point out footprints leading to the west. You look down the \
mountain and spot Red Town, you can also faintly see the Grey Forest from here. \
eTh aMn hWo Borke Teh ouFrht Wlla si eanr.")

Dark_Figure = Room("Red Summit", "The Man of the Shadows", None, None, None, "Burning_Tree", None, None, [Empty], 
"Why did you come here? Do you like exploring? Did you just happen to type in \"west\"? \
What ever your reason, you don't belong here. You belong in line 553. Who let you \
explore? It was him, was it not? Go back to where you came from, %s. " %name)

Vanished = Room("timmuS deR", "eTh mnA nI hTe iMrorr", "Altar", None, None, None, None, None, [Empty],
"You are west of the Burning Tree. You spot a dark figure, a humanoid, to the north \
near what appers to be an altar. How funny, you remember seeing it before, although \
you don't remember exactly where. Or do you? ")

Altar = Room("Red Summit", "Sacrificial Altar", "Kill", "Vanished", None, None, None, None, [Empty],
"You are alongside the sacrifical altar. There is a trail of blood, monster blood, \
leading to the north and to the west. To the north, you spot the dark figure holding \
a weapon. It seems to be waiting for you to walk up to it.")

Kill = Room("Red Summit", "Finis", None, None, None, None, None, "Red_Stairway", [Empty],
"You are alongside the corpse of Red, leader of the Knights of Red and a warrior \
of legend. The Burning Tree is no longer aflame, it is serene. Head to the Chief's \
Palace to obtain your reward. But first, climb down the mountain.")
#-------------------------------------------------------------------------------
File1_Name = "Empty"
File2_Name = "Empty"
File3_Name = "Empty"

Load1_Name = "Empty"
Load2_Name = "Empty"
Load3_Name = "Empty"
#-------------------------------------------------------------------------------
#Save functions
#Save File Number 1
def save1():
    global File1_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    File1_Name = node.name
    with open('savegame.dat', 'wb') as Save_File1:
       pickle.dump([File1_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill], Save_File1, protocol = 2) #variables that you want to save should be here 
    print
    print "------------------------------------------------------------------------"
    print
    print "/// Save Files %s" %("\\\\\\")
    print "(1) Save File: %s" %File1_Name
    print "(2) Save File: %s" %File2_Name
    print "(3) Save File: %s" %File3_Name
    print
    print "Game succesfully saved!"
#-------------------------------------------------------------------------------
#Save File Number 2
def save2():
    global File2_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    File2_Name = node.name
    with open('savegame.dat', 'wb') as Save_File2:
       pickle.dump([File2_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill], Save_File2, protocol = 2) #variables that you want to save should be here 
    print
    print "------------------------------------------------------------------------"
    print
    print "/// Save Files %s" %("\\\\\\")
    print "(1) Save File: %s" %File1_Name
    print "(2) Save File: %s" %File2_Name
    print "(3) Save File: %s" %File3_Name
    print
    print "Game succesfully saved!"
#-------------------------------------------------------------------------------    
#Save File Number 3
def save3():
    global File3_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    File3_Name = node.name
    with open('savegame.dat', 'wb') as Save_File3:
       pickle.dump([File3_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill], Save_File3, protocol = 2) #variables that you want to save should be here 
    print 
    print "------------------------------------------------------------------------"
    print
    print "/// Save Files %s" %("\\\\\\")
    print "(1) Save File: %s" %File1_Name
    print "(2) Save File: %s" %File2_Name
    print "(3) Save File: %s" %File3_Name
    print
    print "Game succesfully saved!"
#-------------------------------------------------------------------------------
#Load function
#Load File Number 1
def load1():
    global Load1_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    Load1_Name = File1_Name
    with open('savegame.dat', 'rb') as Load_File1:
        Load1_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill = pickle.load(Load_File1)
    print
    print "Game succesfully loaded!"
#-------------------------------------------------------------------------------    
#Load File Number 2
def load2():
    global Load2_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    Load2_Name = File2_Name
    with open('savegame.dat', 'rb') as Load_File2:
        Load2_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill = pickle.load(Load_File2)
    print
    print "Game succesfully loaded!"
#-------------------------------------------------------------------------------    
#Load File Number 3
def load3():
    global Load3_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill
    Load3_Name = File3_Name
    with open('savegame.dat', 'rb') as Load_File3:
        Load3_Name, name, player, node, Movement_Counter, Enemy_Counter, Inventory_Counter, Stats_Counter, Help_Counter, Map_Counter, Misc_Counter, Damage_Dealt, MDamage_Dealt, Damage_Taken, MDamage_Taken, Bar_Counter, Candle_Counter, APuzzle, BPuzzle, CPuzzle, Werewolf1, Dryad1, Werewolf2, Werewolf3, Werewolf4, Sorcerer1, Sorcerer2, Phoenix1, Phoenix2, Bat1, Bat2, Bat3, Knight1, Knight2, Knight3, Knight4, Avis, Red, WerewolfR1, WerewolfR2, WerewolfR3, WerewolfR4, Grey_Baron, Residential, Market, Weaponsmith, Fruit, Bar, Burial_Grounds, Path_Junction, Path_Junction2, Junction, Path_Lake, Path_Lake2, West_Lake, North_Lake, Flower_Bed, East_Lake, Cave_East_Lake, Hidden_Room_Lake, South_Lake, Hut, Basement_Hut, Lake_Azure, Path_Wolf, Path_Wolf2, Wolf_Totem, Necromancer_Cabin, N_Upstairs, N_Basement, Bone_Pile, Cave_Entrance, Wolf_Den, Road_Red, Road_Red2, Gate_Red, Town_Square, Red_Market, Sword_Shop, Red_Fruit, Red_Bar, Chief_Palace, Red_Stairway, Fog_Room, Droppings, Skulls_Bones, Thousand_Steps, Dark_Room, Illuminated_Passage, Bone_Piles, Red_Chest1, Lava_LakeX, Lava_Lake1, Stairwell, The_Torch, Puddles, Pedestal, Guattor, Primus, Secundo, Tertium, Quartam, Reward, TStairs, Three_Crystals, PuzzleA, PuzzleB, PuzzleC, BPhoenix, To_Summit, Foot_Prints, Burning_Tree, Dark_Figure, Vanished, Altar, Kill = pickle.load(Load_File3)
    print
    print "Game succesfully loaded!"
#-------------------------------------------------------------------------------
def savefile_name():
    print "------------------------------------------------------------------------"
    print
    print "/// Save Files %s" %("\\\\\\")
    print "(1) Save File: %s" %File1_Name
    print "(2) Save File: %s" %File2_Name
    print "(3) Save File: %s" %File3_Name
#-------------------------------------------------------------------------------
def level_up():    
    
    if player.xp in range(0, 5):
        player.level = 1
    elif player.xp in range(5, 10):
        player.level = 2
    elif player.xp in range(10, 15):
        player.level = 3
    elif player.xp in range(15, 20):
        player.level = 4
    elif player.xp in range(20, 25):
        player.level = 5
    elif player.xp in range(25, 30):
        player.level = 6
    elif player.xp in range(30, 35):
        player.level = 7
    elif player.xp in range(35, 40):
        player.level = 8
    elif player.xp in range(45, 50):
        player.level = 9
    elif player.xp in range(50, 55):
        player.level = 10
    elif player.xp in range(55, 60):
        player.level = 11
    elif player.xp in range(60, 65):
        player.level = 12
    elif player.xp in range(65, 70):
        player.level = 13
    elif player.xp in range(70, 75):
        player.level = 14
    elif player.xp in range(75, 80):
        player.level = 15
    elif player.xp in range(85, 90):
        player.level = 16
    elif player.xp in range(90, 65):
        player.level = 17
    elif player.xp in range(95, 100):
        player.level = 18
    elif player.xp in  range(100,105):
        player.level = 19
    elif player.xp in range(105,110):
        player.level = 20
    elif player.xp in range(110,115):
        player.level = 21
    elif player.xp in range(115,120):
        player.level = 22
    elif player.xp in range(120, 125):
        player.level = 23
    elif player.xp in range(125,130):
        player.level = 24
    elif player.xp in range(130,135):
        player.level = 25
    elif player.xp in range(135,140):
        player.level = 26
    elif player.xp in range(145,150):
        player.level = 27
    elif player.xp in range(150,155):
        player.level = 28
    elif player.xp in range(155,160):
        player.level = 29
    elif player.xp in range(165,170):
        player.level = 30
    elif player.xp in range(170,175):
        player.level = 31
                
    #If you reach a certain level, you will gain stat upgrades
    
    if player.level == 1:
        player.max_health = 200
        player.max_magic = 50
        player.defense = 50
        player.damage = 100
        player.magic_damage = 100
    
    elif player.level == 2:
        player.max_health = 201 # +1
        player.max_magic = 50
        player.defense = 50
        player.damage = 100
        player.magic_damage = 100
        
    elif player.level == 3:
        player.max_health = 201 # +1
        player.max_magic = 50
        player.defense = 50
        player.damage = 101 # +1
        player.magic_damage = 100 
    
    elif player.level == 4:
        player.max_health = 201 # +1
        player.max_magic = 50
        player.defense = 50 
        player.damage = 101 # +1
        player.magic_damage = 100
        
    elif player.level == 5:
        player.max_health = 201 # +1
        player.max_magic = 50
        player.defense = 50
        player.damage = 101 # +1
        player.magic_damage = 101 # +1
    
    elif player.level == 6:
        player.max_health = 202 # +2
        player.max_magic = 50
        player.defense = 50
        player.damage = 101 # +1
        player.magic_damage = 101 # +1
    
    elif player.level == 7:
        player.max_health = 202 # +2
        player.max_magic = 50
        player.defense = 50
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
    
    elif player.level == 8:
        player.max_health = 203 # +3
        player.max_magic = 50
        player.defense = 51 # +
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
    
    elif player.level == 9:
        player.max_health = 204 # +4
        player.max_magic = 50
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
        
    elif player.level == 9:
        player.max_health = 205 # +5
        player.max_magic = 50
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
    
    elif player.level == 10:
        player.max_health = 205 # +5
        player.max_magic = 50 
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
    
    elif player.level == 11:
        player.max_health = 206 # +6
        player.max_magic = 75 # + 25
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 101 # +1
    
    elif player.level == 12:
        player.max_health = 206 # +6
        player.max_magic = 75 # + 25
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 102 # +2
    
    elif player.level == 13:
        player.max_health = 206 # +6
        player.max_magic = 75 # + 25
        player.defense = 51 # +1
        player.damage = 102 # +2
        player.magic_damage = 103 # +3
    
    elif player.level == 14:
        player.max_health = 206 # +6
        player.max_magic = 75 # + 25
        player.defense = 51 # +1
        player.damage = 103 # +3
        player.magic_damage = 103 # +3
    
    elif player.level == 15:
        player.max_health = 206 # +6
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 104 # +4
        player.magic_damage = 104 # +4
    
    elif player.level == 16:
        player.max_health = 207 # +7
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 104 # +4
        player.magic_damage = 104 # +4
    
    elif player.level == 17:
        player.max_health = 208 # +8
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 104 # +4
        player.magic_damage = 104 # +4
    
    elif player.level == 18:
        player.max_health = 208 # +8
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 104 # +4
        player.magic_damage = 104 # +4
    
    elif player.level == 19:
        player.max_health = 208 # +8
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 104 # +4
        player.magic_damage = 105 # +5
    
    elif player.level == 20:
        player.max_health = 208 # +8
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 21:
        player.max_health = 209 # +9
        player.max_magic = 75 # + 25
        player.defense = 52 # +2
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 22:
        player.max_health = 210 # +10
        player.max_magic = 75 # + 25
        player.defense = 53 # +3
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 23:
        player.max_health = 210 # +10
        player.max_magic = 75 # + 25
        player.defense = 53 # +3
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 24:
        player.max_health = 211 # +11
        player.max_magic = 75 # + 25
        player.defense = 53 # +3
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 25:
        player.max_health = 212 # +12
        player.max_magic = 75 # + 25
        player.defense = 53 # +3
        player.damage = 105 # +5
        player.magic_damage = 105 # +5
    
    elif player.level == 26:
        player.max_health = 212 # +12
        player.max_magic = 75 # + 25
        player.defense = 53 # +3
        player.damage = 105 # +5
        player.magic_damage = 106 # +6
    
    elif player.level == 27:
        player.max_health = 212 # +12
        player.max_magic = 75 # + 25
        player.defense = 54 # +4
        player.damage = 105 # +5
        player.magic_damage = 106 # +6
    
    elif player.level == 28:
        player.max_health = 212 # +12
        player.max_magic = 75 # + 25
        player.defense = 54 # +4
        player.damage = 106 # +6
        player.magic_damage = 106 # +6
    
    elif player.level == 29:
        player.max_health = 213 # +13
        player.max_magic = 75 # + 25
        player.defense = 54 # +4
        player.damage = 106 # +6
        player.magic_damage = 106 # +6
    
    elif player.level == 30:
        player.max_health = 214 # +14
        player.max_magic = 75 # + 25
        player.defense = 54 # +4
        player.damage = 106 # +6
        player.magic_damage = 106 # +6
    
    elif player.level == 31:
        player.max_health = 220 # +20
        player.max_magic = 100 # + 50
        player.defense = 60 # +10
        player.damage = 110 # +10
        player.magic_damage = 110 # +10
        
#-------------------------------------------------------------------------------        
#The first node, where the player "spawns"
node = Grey_Baron
#-------------------------------------------------------------------------------
#The function that starts the game 
def start(): 

    while True:
        
        level_up()
        print
        print "------------------------------------------------------------------------"
        print "> %s, %s" %(node.name, node.domain)
        #print "------------------------------------------------------------------------"
        print "%s" %node.description
        print "------------------------------------------------------------------------"
        movement = ["north", "south", "east", "west", "up", "down"]
        loot = ["loot", "Loot", "l", "L", "pick up", "Pick up", "pick Up"]
        quit = ["q", "quit", "kill yourself"]
        help = ["?", "help", "Help"]
        yes = ["y","Yes","yes"]
        no  = ["n", "No", "no"]
        
        physical = ["Viper Sword", "Obsidian Sword", "Phoenix Sword"]
        magical = ["Emerald Skull", "Ruby Skull"]
        headgear = ["Legendary Werewolf Mask", "Phoenix Mask"]
        chest = ["Dryad's Chestplate", "Red's Chest"]
        gauntlets = ["Dryad's Gauntlets", "Red's Gauntlets"]
        boots = ["Dryad's Boots", "Red's Boots"]
        other = ["Key"]
        save_commands = ["save", "Save"]
        load_commands  = ["load", "Load"]
        #load_commands = ["load", "Load"]
        misc = ["Flower Pot", "Book", "Apple", "Blanket", "Bed", "Shot glass", "Rug", 
        "Sofa", "Spatula", "Bookcase", "Gnome", "Chair", "Human Skull"]
        quest = ["Conflagration Termination"]
        general = ["Viper Sword", "Emerald Skull",  "Legendary Werewolf Mask", 
        "Dryad's Chestplate", "Dryad's Gauntlets", "Dryad's Boots", "Obsidian Sword", 
        "Phoenix Sword", "Ruby Skull", "Phoenix Mask", "Red's Chest", "Red's Gauntlets", 
        "Red's Boots", "Key", "Flower Pot", "Book", "Apple", "Blanket", "Bed", "Rug", 
        "Shot glass", "Sofa", "Spatula", "Bookcase", "Gnome", "Chair", "Human Skull"]
        
        
#-------------------------------------------------------------------------------        
        print "Type \"?\" for help."
        command = raw_input("> ").lower()
#-------------------------------------------------------------------------------
#Ends the game
        if command in quit:
            break
#-------------------------------------------------------------------------------
#Saves the game        
        elif command in save_commands:
            while True:
                savefile_name()
                print 
                print "What file do you want to override?"
                
                teh_input = raw_input(">")

                if teh_input in "1":
                    save1()
                    break
                    
                elif teh_input in "2":
                    save2()
                    break
                    
                elif teh_input in "3":
                    save3()
                    break
                
                elif teh_input in quit:
                    break
#-------------------------------------------------------------------------------
        elif command in load_commands:
            
            while True:
                
                def loadfile_name():
                    print "------------------------------------------------------------------------"
                    print
                    print "/// Save Files %s" %("\\\\\\")
                    print "(1) Save File: %s" %File1_Name
                    print "(2) Save File: %s" %File2_Name
                    print "(3) Save File: %s" %File3_Name
                
                loadfile_name()
                print 
                print "What file do you want to load?"
                
                teh_input = raw_input(">")

                if teh_input in "1":
                    loadfile_name()
                    load1()
                    break
                
                elif teh_input in "2":
                    loadfile_name()
                    load2()
                    break
                
                elif teh_input in "3":
                    loadfile_name()
                    load3()
                    break
                
                elif teh_input in quit:
                    break
#-------------------------------------------------------------------------------
#This is what makes player movement possible            
        elif command in movement:
            try:
                node.move(command)
            except:
                print "You can not go that way..."
                
            Movement_Counter.number += 1
#-------------------------------------------------------------------------------    
#Brings up every possible command (outside of puzzles and combat)            
        elif command in help:
            Help_Counter.number += 1
            print
            print "> To move around the map, type the following: North, South, East, West, Up, or Down"
            print "> To pick up loot, type: loot"
            print "> To view your inventory, type: inventory"
            print "> To view your stats, type: stats"   
            print "> To view your map, type: map"  
            print "> To save your game, type: save"
            print "> To load your game, type: load"
#------------------------------------------------------------------------------- 
#Brings up the player's inventory
        elif command == "inventory":
            
            def the_description():
                print
                print "/// %s's Inventory: %s" %(player.name, "\\\\\\")
                print "> (1) Physical Weapon: %s" %player.physical.name
                print "> (2) Magical Weapon: %s" %player.magical.name
                print "> (3) Headgear: %s" %player.headgear.name
                print "> (4) Chest: %s" %player.chest.name
                print "> (5) Gauntlets: %s" %player.gauntlets.name
                print "> (6) Boots: %s" %player.boots.name
                print "> (7) Key(s): %s" %player.other.name  
                print "> (8) Quest: %s" %player.quest.name 
                print "> (9) %s's Miscellaneous Items" %player.name            
                print 
                
            the_description()
                        
            physical = ["1", "Physical Weapon", "physical weapon", player.physical.name]
            magical = ["2", "Magical Weapon", "magical weapon", player.magical.name]
            headgear = ["3", "headgear", "headgear", player.headgear.name]
            chest = ["4", "Chest", "chest", player.chest.name]
            gauntlets = ["5", "Gauntlets", "gauntlets", player.gauntlets.name]
            boots = ["6", "Boots", "boots", player.boots.name]
            other = ["7", "Other", "other", player.other.name]
            quest = ["8", "Quest", "quest", player.quest.name]
            misc  = ["9", "Misc", "misc", "Miscellaneous", "miscellaneous"]
            exit_inventory = ["exit", "no"]
            
            while True:
                print
                print "Type the name or number of the item you would like to \
inspect. To close your inventory, type \"exit\"."
                item = raw_input(">  ")
                print
                
                if item in physical:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.physical.name
                    print "> DESCRIPTION: %s" %player.physical.description
                    print "> DMG: %s" %player.physical.damage 
                    print "------------------------------------------------------------------------"
                    the_description()
                    
                elif item in magical:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.magical.name
                    print "> DESCRIPTION: %s" %player.magical.description
                    print "> MAGIC DMG: %s" %player.magical.magic_damage 
                    print "------------------------------------------------------------------------"
                    the_description()
                    
                elif item in headgear:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.headgear.name
                    print "> DESCRIPTION: %s" %player.headgear.description
                    print "> DEF: %s" %player.headgear.defense 
                    print "------------------------------------------------------------------------"
                    the_description() 
                    
                elif item in chest:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.chest.name
                    print "> DESCRIPTION: %s" %player.chest.description
                    print "> DEF: %s" %player.chest.defense 
                    print "------------------------------------------------------------------------"
                    the_description()
                    
                elif item in gauntlets:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.gauntlets.name
                    print "> DESCRIPTION: %s" %player.gauntlets.description
                    print "> DEF: %s" %player.gauntlets.defense
                    print "------------------------------------------------------------------------"
                    the_description() 
                    
                elif item in boots:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.boots.name
                    print "> DESCRIPTION: %s" %player.boots.description
                    print "> DEF: %s" %player.boots.defense
                    print "------------------------------------------------------------------------"
                    the_description()
                
                elif item in other:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.other.name
                    print "> DESCRIPTION: %s" %player.other.description
                    print "------------------------------------------------------------------------"
                    the_description()
                    
                elif item in quest:
                    print "------------------------------------------------------------------------"
                    print "> NAME: %s" %player.quest.name
                    print "> DESCRIPTION: %s" %player.quest.description
                    print "------------------------------------------------------------------------"
                    the_description()  
                
                elif item in misc:
                        
                    while True:
                        print "------------------------------------------------------------------------"
                        print "Miscellaneous Items: "
                        print "Misc. Items Collected: %s" %Misc_Counter.number
                        
                        for items in player.miscellaneous:
                            items = (items)
                            print "------------------------------------------------------------------------"
                            print "- %s: %s" %(items.name, items.description)
                        
                        print "------------------------------------------------------------------------"
                        print
                        print "To close your miscellaneous inventory, type: \"exit\"."
                        inspect_item = raw_input("> ")
   
                        if inspect_item in exit_inventory:
                            break
                                
                    the_description()
                    
                elif item in exit_inventory:
                    Inventory_Counter.number +=1
                    print "------------------------------------------------------------------------"
                    print "> You closed your inventory"
                    print "------------------------------------------------------------------------"
                    break
                    
                elif item in quit:
                    sys.exit(0)
                    
#-------------------------------------------------------------------------------
#Brings up the player's statistics  
        elif command == "stats":
            Stats_Counter.number += 1
            print
            print "/// %s's Stats %s" %(player.name, "\\\\\\")
            print "> HP: %s / %s" %(player.health, player.max_health)
            print "> MP: %s" %player.magic
            print "> DEF: %s" %(player.defense + player.headgear.defense + player.chest.defense + player.gauntlets.defense + player.boots.defense)
            print "> DMG: %s" %(player.damage + player.physical.damage)
            print "> MAGIC DMG: %s" %(player.magic_damage + player.magical.magic_damage)
            print 
            print "> LEVEL: %s" %player.level
            print "> XP: %s" %player.xp  
            print 
            print "> Times Moved: %s" %Movement_Counter.number
            print "> Inventory Opened: %s" %Inventory_Counter.number
            print "> Statistics Examined: %s" %Stats_Counter.number
            print "> Help Requested: %s" %Help_Counter.number
            print "> Map Inspected: %s" %Map_Counter.number
            print
            print "> Enemies Killed: %s" %Enemy_Counter.number
            print "> Damage Dealt: %s" %Damage_Dealt.number
            print "> Magic Damage Dealt: %s" %MDamage_Dealt.number
            print "> Damage Received: %s" %Damage_Taken.number
            print "> Magic Damage Received: %s" %MDamage_Taken.number
#-------------------------------------------------------------------------------
#Brings up a map with paths 

        elif command == "map":
                
            Map_Counter.number += 1
            
            print 
            print "------------------------------------------------------------------------"
            print
            print "/// %s (Map) %s" %(node.name, "\\\\\\")
            
            if node.north != None:
                print "> (↑) North: %s" %(globals()[node.north].name)
                
            if node.south != None:
                print "> (↓) South: %s" %(globals()[node.south].name)
                
            if node.east != None:
                print "> (→) East: %s" %(globals()[node.east].name)
                
            if node.west != None:
                print "> (←) West: %s" %(globals()[node.west].name)
                
            if node.up != None:
                print "> (⇈) Up: %s" %(globals()[node.up].name)
                
            if node.down != None:
                print "> (⇊) Down: %s" %(globals()[node.down].name)
                
#------------------------------------------------------------------------------- 
#So that the program will not respond to "loot" with "> That command does not exist."     
        elif command == "loot":
            pass          
#------------------------------------------------------------------------------- 
#If the player types in a command that the program does not recognize, it will respond with this               
        else:
            print "> That command does not exist."
#-------------------------------------------------------------------------------                
#Pick up items and throw away your current item. You will always obtain items stronger than your current item        
    
        for Loot in node.loot:
            
            if Loot == Empty or Loot == Empty2:
                lootable = False
            else:
                lootable = True 
                
            if command in loot:
                if Loot == Empty:
                    print "> There is no loot here. <" 
                    
                if Loot == Empty2:
                    print "> You have already picked up the loot. <"
                    
                if lootable == True:
                    if Loot.name in physical:
                        player.physical = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                        
                    if Loot.name in magical:
                        player.magical = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                            
                    if Loot.name in headgear:
                        player.headgear = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                        
                    if Loot.name in chest:
                        player.chest = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                          
                    if Loot.name in gauntlets:
                        player.gauntlets = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                        
                    if Loot.name in boots:
                        player.boots = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up and equipped the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                    
                    if Loot.name in other:
                        player.other = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                    
                    if Loot.name in quest:
                        player.quest = Loot
                        print "------------------------------------------------------------------------"
                        print "> %s picked up the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                    
                    if Loot.name in misc:
                        Misc_Counter.number += 1
                        player.miscellaneous.append(Loot)
                        print "------------------------------------------------------------------------"
                        print "> %s picked up the %s <" %(name, Loot.name)
                        print "> Open your inventory for more information <"
                            
                    if Loot.name in general:
                        node.loot = [Empty2]

                    print "------------------------------------------------------------------------"

#-------------------------------------------------------------------------------        
#RANDOM ENCOUNTER NUMBER GENERATOR
        encounter_number = [1, 2, 3, 4]   
        if command in movement:
            random_encounter = random.choice(encounter_number)                        
#-------------------------------------------------------------------------------
#RANDOM WEREWOLF ENCOUNTER #1
        if node == South_Lake:
            if random_encounter == 1:
                player.turn_based(WerewolfR1)
                
        if node != South_Lake:         
            if WerewolfR1.health <= 0:
                WerewolfR1.health = 55 
#-------------------------------------------------------------------------------    
#RANDOM WEREWOLF ENCOUNTER #2    
        if node == West_Lake:
            if random_encounter == 2:
                player.turn_based(WerewolfR2)
                
        if node != West_Lake:         
            if WerewolfR2.health <= 0:
                WerewolfR2.health = 55 
#-------------------------------------------------------------------------------    
#RANDOM WEREWOLF ENCOUNTER #3
        if node == East_Lake:
            if random_encounter == 3:
                player.turn_based(WerewolfR3)
                
        if node != East_Lake:         
            if WerewolfR3.health <= 0:
                WerewolfR3.health = 55 
#-------------------------------------------------------------------------------
#RANDOM WEREWOLF ENCOUNTER #4  
        if node == North_Lake:
            if random_encounter == 4:
                player.turn_based(WerewolfR4)
                
        if node != North_Lake:         
            if WerewolfR4.health <= 0:
                WerewolfR4.health = 55 
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE
        if Werewolf1.health <= 0:
            Cave_East_Lake.description = "You are inside a cave found east of Lake \
Azure. You spot a pair of tattered pants on top a stalagmite. Deep scratch marks \
fill the walls. Taupe colored hair lies on the cave's floor. It is apparent that \
lycanthropy took place here. The uncanny sounds are gone, you killed the werewolf."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE       
        if player.chest == Dryad_Chest:
            Basement_Hut.description = "You are in the hut's basement. It is rather \
dark down here. The dryad's head lies on the basement's floor along with the werewolf's \
corpse. The stairs will take you up to the first floor of the hut."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE            
        if player.gauntlets == Dryad_Gauntlets:
            Hidden_Room_Lake.description = "You found the cave's hidden room. It is pitch-black. \
The werewolf's corpse lies on the ground."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE
        if player.boots == Dryad_Boots:
            Flower_Bed.description = "You found the dryad's shrine, a luscious flower bed of various plants and colorful \
flowers. A shrine commemorated by the townspeople of Grey Village to honor the dryad's \
efforts to keep the forest \"safe\". The sprawl of the dryad's lifeless body focuses \
the attention away from the shrine." 
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE & OPEN PATH       
        if (player.boots == Dryad_Boots and player.chest == Dryad_Chest and player.gauntlets == Dryad_Gauntlets) and node == Path_Wolf:
            Path_Wolf.description = "You are on the path to The Wolf's Den, the \
most dangerous area in Grey Forest."
            Path_Wolf.west = "Wolf_Totem"
            
            WerewolfQ.description = "The werewolves of Grey Forest have been causing \
immense unrest among the population of Grey Village. First, they started killing anyone \
who dared exit the safety of the village. The next thing you know, they raided the village, \
killing off half of its population. You have been hired by the Grey Baron to \
hunt down and kill the leader of the pack, thus causing the rest to disperse and bother \
the village no more. You will be rewarded for completing the task."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE   
        if player.magical == Emerald_Skull:
            Wolf_Totem.description = "You are south of The Wolf's Den. This location \
is brimming with totem poles of wolves. Deep scratch marks cover the totem poles, \
however a wolf is not strong enough to have produced a scrape so deep, it must \
have been a werewolf."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGES       
        if Werewolf4.health <= 0:
            Wolf_Den.description = "You are inside The Wolf's Den. It smells of \
blood and wet dog, a crippling stench. The Grey Wolf lies lifeless on the cave's \
floor. Carve its face out and wear it as a trophy for your exploit."

            Grey_Baron.description = "You are inside the Grey Baron's manor in the \
forest. You have completed the task of killing the leader of the wolf pack. As \
promised, you have been rewarded. Your reward is The Viper Sword."

            Residential.west = "Grey_Baron"
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE
        if player.headgear == Werewolf_Mask:
            Wolf_Den.description = "You are inside The Wolf's Den. It smells of \
blood and wet dog, a crippling stench. The Grey Wolf lies lifeless on the cave's \
floor, you wear its face as a mask. Head to the Grey Baron's Manor to receive \
your reward."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE, REWARD, & REMOVES QUEST
        if node == Grey_Baron:
            if Werewolf4.health <= 0:
                if player.physical != Viper_Sword:
                    player.physical = Viper_Sword
                    print "------------------------------------------------------------------------"
                    print "> %s was rewarded the Viper Sword! <" %name 
                    print "> Open your inventory for more information <"  
                if player.physical == Viper_Sword:
                    Grey_Baron.description = "You are inside the Grey Baron's manor \
in the forest. You have completed the task, now it is time to leave Grey Forest \
since you have no more business here. Travel north to Red Mountain. "
                    print 
                    print "On The Next Chapter:"
                    print "- More enemies"
                    print "- More consequences"
                    print "- More 'loot'"
                    print "- A tsyro ahtt skmea eozro enses"
                    print "- %s will be punished if the level is not explored." %name
                  
                    player.quest = Empty_Quest
                    Residential.west = None
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE & ENTRY TO RED MOUNTAIN                
        if player.quest != WerewolfQ:
            Road_Red.north = "Gate_Red"
            Road_Red.description = "You are on the road to Red Mountian, a domain \
dominated by volcanic activity."
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE & FREE DRINKS (BAR)
        if node == Bar:
            Bar_Counter.number += 1  
            
            if Bar_Counter.number == 2:
                Bar.description = "You are inside the Mar's Bar, the village's \
most popular social center. You receive a free drink from Mar. It fills you up and \
replenishes you with energy! Come back later for another drink." 
                player.health = player.max_health
                
            if Bar_Counter.number == 3:
                Bar.description = "You are inside the Mar's Bar, the village's \
most popular social center. You receive a free drink from Mar. It fills you up and \
replenishes you with energy! He is all out of drinks, for you atleast." 
                player.health = player.max_health
            
            if Bar_Counter.number == 4:
                Bar.description = "You are inside the Mar's Bar, the village's \
most popular social center. He is all out of drinks, for you atleast." 
                player.health = player.max_health
#-------------------------------------------------------------------------------
#NEW QUEST            
        if player.quest == PhoenixQ:
            
            Town_Square.east = None
            
            Red_Stairway.up = "Fog_Room"
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE & OPEN DOOR
        if player.other == Key1:
            Fog_Room.north = "Thousand_Steps"
            Fog_Room.description = "You are inside the first room of Red Mountain, \
many more await. Your surroundings are obscured by a thick layer of fog. "
#-------------------------------------------------------------------------------
#ENVIRONMENTAL DAMAGE
        if node == Lava_LakeX:
            player.health -= 10
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE 
        if player.boots == Red_Boots:
            
            Red_Chest1.description = "You are inside a small room."
            
            Illuminated_Passage.east = "Lava_Lake1"
            
            Stairwell.south = "Lava_Lake1"
            
            Illuminated_Passage.description = "You are inside a cave with no source \
of light other than the colossal lava lake to the east. There appears to be a door \
at the end of the lake."

            Red_Chest1.description = "You are inside a small room with nothing \
else but a chest, which you have already looted."
#-------------------------------------------------------------------------------
#HEALTH RESET FOR CH2
        if node == Gate_Red:
            player.health = player.max_health
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE
        if player.chest == Red_Chest:
            Reward.description = "You have succesfully completed all of the Challenge \
Nodes! The path to the east leads to some stairs leading upwards. Go!"

        if player.physical == Obsidian_Sword:
            Pedestal.description = "You are inside a room with lava gushing out \
of the walls, creating lavafalls. There is a pedestal in the center of the room, \
untouched by the molten rock."
#-------------------------------------------------------------------------------
#PUZZLE A
        if node == PuzzleA:
            
            while True:
                
                if APuzzle.number == 0:
                    print
                    print "------------------------------------------------------------------------"
                    print "> %s, %s" %(node.name, node.domain)
                    print "%s" %node.description
                    print
                    print "Answer the following riddle: "
                    print
                    print "\"If I drink, I die. If I eat, I am fine. What am I?\""
                    answer = raw_input("> ")
                    
                    if answer.lower() == "fire":
                        print "Correct! The candle in front of you is now lit."
                        APuzzle.number = 1
                        Candle_Counter.number += 1
                        PuzzleA.description = "You are inside a room with one dull, \
blue crystal hanging from the roof. There is also a wooden chair and table with \
a piece of parchment, quill, and ink. "
                        print "------------------------------------------------------------------------"
                        break
                    else:
                        print "Wrong... The feeling of not being able to solve the \
riddle is burning through your body."
                        print "------------------------------------------------------------------------"
                        break
                else:
                    break
#-------------------------------------------------------------------------------
#PUZZLE B
        if node == PuzzleB:
            
            teh_name = "%s" %name 
            
            while True:
                
                if BPuzzle.number == 0:
                    print
                    print "------------------------------------------------------------------------"
                    print "> %s, %s" %(node.name, node.domain)
                    print "%s" %node.description
                    print
                    print "Answer the following: "
                    print
                    print "\"What is your name?\""
                    answer = raw_input("> ")
                    
                    if answer.lower() in teh_name.lower():
                        print "Correct! The candle in front of you is now lit."
                        BPuzzle.number = 1
                        Candle_Counter.number += 1
                        PuzzleB.description = "You are inside a room with one dull, \
green crystal hanging from the roof. There is also a wooden chair and table with \
a piece of parchment, quill, and ink. "
                        print "------------------------------------------------------------------------"
                        break
                    else:
                        print "Wrong... The pain of not being able to remember \
your own name is... painful."
                        print "------------------------------------------------------------------------"
                        break
                else:
                    break
#-------------------------------------------------------------------------------
#PUZZLE C
        if node == PuzzleC:
            while True:
                
                if CPuzzle.number == 0:
                    print
                    print "------------------------------------------------------------------------"
                    print "> %s, %s" %(node.name, node.domain)
                    print "%s" %node.description
                    print
                    print "Answer the following: "
                    print
                    print "\"Take away my first letter, and I still sound the same. \
Take away my last letter, I still sound the same. Even take away my letter in the \
middle, I will still sound the same. I am a five letter word. What am I?\""
                    answer = raw_input("> ")
                    
                    if answer.lower() == "empty":
                        print "Correct! The candle in front of you is now lit."
                        CPuzzle.number = 1
                        Candle_Counter.number += 1
                        PuzzleB.description = "You are inside a room with one dull, \
red crystal hanging from the roof. There is also a wooden chair and table with \
a piece of parchment, quill, and ink. "
                        print "------------------------------------------------------------------------"
                        break
                    else:
                        print "Wrong... Your inability to solve this riddle leaves \
you feeling empty on the inside."
                        print "------------------------------------------------------------------------"
                        break
                else:
                    break
#-------------------------------------------------------------------------------
#GLOWING CRYSTALS
        if Candle_Counter.number == 1:
            Three_Crystals.description = "There are two dull, white crystals hanging \
from the ceiling. One of them is glowing. The room breaks off into four locations."
        
        if Candle_Counter.number == 2:
            Three_Crystals.description = "There is one dull, white crystal hanging \
from the ceiling. Two of them are glowing. The room breaks off into four locations."

        if Candle_Counter.number == 3:
            Three_Crystals.description = "You have completed all of the puzzles. \
All three crystals are now glowing, each with their own respective color. From left \
to right, their colors are: blue, red, and green. Before your very own eyes, a ghostly, \
almost transparent, and cloudy staircase is formed from nothingness. The stairs \
lead to an opening on the roof, it might be one of the exits of Red Mountain..."
            Three_Crystals.up = "To_Summit"
#-------------------------------------------------------------------------------
#DESCRIPTION CHANGE
        if player.physical == Phoenix_Sword:
            BPhoenix.description = "You enter a room to the south. You are inside \
what appears to have once been a treasure room. Gold coins and platinum trophies \
litter the floor, however, none of this filthy currency matters to a Monster Hunter \
like you, of course. "
#-------------------------------------------------------------------------------
#QUEST (UPDATE)
        if Red.health <= 0:
            player.quest = PhoenixQ_Updated
            Red_Stairway.description = "You are in the stone stairway leading to \
the dungeon hidden away the inside of the mountain. The Burning Tree atop Red \
Mountain has vanished..."
            Red_Stairway.up = None
            Town_Square.east = "Chief_Palace" 
            Chief_Palace.description = "You are inside the Red Chief's Palace. \
It is a colossal building with decorum appropiate for a wealthy leader like the \
Red Chief. The place looks intact, as if the invasion of Red Town never occured. \
The remaining population of the town is in here, they are afraid. Guards are \
positioned in every corner."
        
        if player.quest == PhoenixQ_Updated:
            if node == Chief_Palace:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "%s" %node.description
                print 
                print "The Red Chief salutes you and thanks you for completing the \
task. The town is now safe, thanks to you, and thanks to you the beasts residing \
in Red Mountain will all be driven to extinction by the townfolk. You walk away \
before you can receive your reward, as there is no need for one. No one will remember \
this adventure, no one but you and a few people. This will not go down in the textbooks, \
but it is alright, for the only thing that matters to you is that you were lucky \
enough to have experienced it. However, somehow you feel like this isn't over yet..." 
                print 
#                print "Thank you, #%s..." %teh_number
                print "------------------------------------------------------------------------"
                break
                
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ 
#CHAPTER 1 ENCOUNTERS
#COMBAT
        if node == Hidden_Room_Lake:
            if Werewolf1.health > 0:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "%s" %node.description
                print 
                print "Proving your suspicions correct, you stumble upon a werewolf. \
Kill the werewolf, put an end to its misery."
                print "Would you like a tutorial for combat? Yes or no?"
                print
                question = raw_input("> ")
                print
                if question in yes:
                    print "Alright. You have three options in combat. Your first option \
is to simply attack, you will deal \"solid\" amounts of damage this way. Your second \
option is to drain your opponent's health, you will deal 70% of your normal damage \
and gain 30 % health of whatever damage you dealt. Your third and final option is \
to use \"randomality\". With randomality, you have the potential to deal massive \
amounts of damage or the potential to deal inconsiderable amounts of damage."
                if question in no:
                    print "Fine."
                print "------------------------------------------------------------------------"
            player.turn_based(Werewolf1)
#-------------------------------------------------------------------------------
#COMBAT        
        if node == Flower_Bed:
            if Dryad1.health > 0:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "%s" %node.description
                print 
                print "You hear the crackle of the leaves. The footsteps are getting \
closer and closer. You turn around and see a dryad rushing towards you. They can \
sense your thirst for monster slaughter, they are not content. Slay it."
                print "Would you like a tutorial for combat? Yes or no?"
                question = raw_input("> ")
                print
                if question in yes:
                    print "Alright. You have three options in combat. Your first option \
is to simply attack, you will deal solid amounts of damage this way. Your second \
option is to drain your opponent's health, you will deal 70% of your normal damage \
and gain 30 % health of whatever damage you dealt. Your third and final option is \
to use \"randomality\". With randomality, you have the potential to deal massive \
amounts of damage or the potential to deal inconsiderable amounts of damage."
                if question in no:
                    print "Fine."
            player.turn_based(Dryad1)
#-------------------------------------------------------------------------------
#COMBAT 
        if node == Basement_Hut:
            if Werewolf2.health > 0:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "%s" %node.description
                print 
                print "You are in front of a werewolf. It must have been responsible \
for the deaths of the villager and the dryad. Kill it."
                print "Would you like a tutorial for combat? Yes or no?"
                print
                question = raw_input("> ")
                if question in yes:
                    print "Alright. You have three options in combat. Your first option \
is to simply attack, you will deal solid amounts of damage this way. Your second \
option is to drain your opponent's health, you will deal 70% of your normal damage \
and gain 30 % health of whatever damage you dealt. Your third and final option is \
to use \"randomality\". With randomality, you have the potential to deal massive \
amounts of damage or the potential to deal inconsiderable amounts of damage."
                if question in no:
                    print "Fine."
            player.turn_based(Werewolf2)
#-------------------------------------------------------------------------------
#COMBAT 
        if node == Wolf_Totem:
            if Werewolf3.health > 0:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "%s" %node.description
                print 
                print "A werewolf has spotted you. The werewolves around The Wolf's \
Den are stronger than the werewolves found around Lake Azure. Fight cautiously."
            player.turn_based(Werewolf3)
#-------------------------------------------------------------------------------
#COMBAT
        if node == Wolf_Den:
            if Werewolf4.health > 0:
                print
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "You are inside The Wolf's Den. It smells of blood and wet \
dog, a crippling stench."
                print 
                print "You are face to face with The Grey Wolf, the leader of the \
pack and the fiercest wolf in the forest. Kill it and the Grey Baron's task will be \
complete." 
            player.turn_based(Werewolf4)
#-------------------------------------------------------------------------------
#COMBAT      
        if node == N_Upstairs:
            if Sorcerer1.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "You interrupt the sorcerer while he was reading one of his \
demonic tomes. Get rid of him."
            player.turn_based(Sorcerer1)
#-------------------------------------------------------------------------------
#COMBAT
        if node == N_Basement:
            if Sorcerer2.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print "You find a sorcerer sitting in a chair. The chair appears \
to be built with dryad flesh, a durable and strong material. Kill him."
            player.turn_based(Sorcerer2)
#-------------------------------------------------------------------------------
#CHAPTER 2 ENCOUNTERS
#COMBAT 
        if node == Red_Market:
            if Phoenix1.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "%s encountered an Injured Phoenix!" %name
            player.turn_based(Phoenix1) 
#-------------------------------------------------------------------------------
#COMBAT 
        if node == Skulls_Bones:
            if Bat1.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "%s encountered a Fire Bat!" %name
            player.turn_based(Bat1) 
#-------------------------------------------------------------------------------
#COMBAT
        if node == Droppings:
            if Bat2.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "%s encountered a Fire Bat!" %name
            player.turn_based(Bat2) 
#-------------------------------------------------------------------------------
#COMBAT
        if node == Primus:
            if Knight1.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "You walk into the room, it is darker than a moonless night. \
Suddenly, the candles in the room light up. You see an armored humanoid rising from \
its sleep. Strangely enough, it is wearing Red Armor. Could it be? Is that thing \
one of the four Knights of Red?"
            player.turn_based(Knight1)
#-------------------------------------------------------------------------------  
#COMBAT
        if node == Secundo:
            if Knight2.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "One less monster to go. You walk into the next room, this \
time there is a Red Knight waiting for you with its sword drawn. You prepare for combat." 
            player.turn_based(Knight2)
                
#-------------------------------------------------------------------------------
#COMBAT
        if node == Tertium:
            if Knight3.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "Two less monsters you have to worry about. You walk inside \
the next room and, coming to you as no surprise, a Red Knight attempts to strike \
you. You dodge his attack and strike him. He blocks the hit with his gauntlets, he \
is wearing stronger armor relative to the other two knights. " 
            player.turn_based(Knight3)

#-------------------------------------------------------------------------------
#COMBAT
        if node == Quartam:
            if Knight4.health > 0:
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "This is the last of the Knights of Red that you will fight. \
You can't help but feel confused. What are the the Knights of Red doing inside here? \
Their fates were unclear for decades, until now. They entered the mountain alongside \
Red, hoping to kill the phoenix that ruled the mountain. They never returned, of \
course, and everyone believed that they were dead. What is going on? " 
            player.turn_based(Knight4)
#-------------------------------------------------------------------------------
        if node == BPhoenix:
            if Avis.health > 0:
                player.health = player.max_health
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "The Knights of Red's treasure room was not left alone. It \
is guarded by The Black Bird, the last of its kind. It is standing before you, with \
its claws pointed at your head, it swoops down and swings at you. You roll away \
to safety and draw your %s. Kill it and the treasure is yours." %player.physical.name 
            player.turn_based(Avis)
#-------------------------------------------------------------------------------
        if node == Kill:
            if Red.health > 0:
                player.health = player.max_health
                print 
                print "------------------------------------------------------------------------"
                print "> %s, %s" %(node.name, node.domain)
                print
                print "You are standing before Red, leader of the Knights of Red \
and a warrior of legends. Believed to be dead by everyone, he is now standing in \
front of you. He is more of a demon, now, than a man. He opens his mouth to speak, \
his voice is harsh like an ogre's."
                print
                print "Red: I have gone through hell to get this far, to protect \
the beasts of the mountain from those vile creatures that call themselves \"civilized.\" \
They care not about the beasts's well-being... they care only \
about how much wealth they can obtain from murdering them and selling their. You \
killed my Knights, it is alright. The Mountain still has me as a protector, and \
I will not let you kill me... at least not without a fight. So, draw your weapon \
and face me in battle, human." 
                print
            player.turn_based(Red)
            
#-------------------------------------------------------------------------------

print
print "> To move around the map, type the following: North, South, East, West, Up, or Down"
print "> To pick up loot, type: loot"
print "> To view your inventory, type: inventory"
print "> To view your stats, type: stats" 
print "> To view your map, type: map"
print "> To save your game, type: save"
print "> To load your game, type: load"
start()