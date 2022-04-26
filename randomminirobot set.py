#Made by MaryOfGold, anyone who copies this code shall be defenestrated
import random
from tokenize import Special
from xml.dom.minidom import Element

GroundUnits = ["Gunner", "Cannon", "Boomerang", "Bubble", "Spider", "Missiler", "Snowballer", "D. Shotgunner", "Shocker", "Sniper"]
HighDamage = ["Sniper", "Plasma", "D. Shotgunner", "Missiler", "Snowballer", "Atomic"]
ElementalUnits = ["Freezer", "Flame", "Plasma"]
AirUnits = ["Copter", "Dropper", "Float"]
UnderwaterUnits = ["Diver", "Submerger"]
MarineUnits = ["Mariner", "Buoy"]
SpecialUnits = ["Hammer","Mini-Mine", "Mini-Bomber", "Storm", "Atomic"]
DamageSpecial = ["Mini-Mine", "Mini-Bomber", "Storm", "Atomic"]
Producer = ["Fusor", "Papa"]
Support = ["Fixer", "Mini-Magnet", "Factory", "Mama", "Recycler"]
LowSupport = ["Fixer", "Mini-Magnet", "Factory", "Recycler"]
Defense = ["Blocker", "Warrior", "Barrier"]
GroundDefense = ["Blocker", "Warrior"]
AntiStealth = ["Sonar", "Surveyor"]
SpecialTR = ["Mini-Mine", "Hammer", "Mini-Bomber", "Storm"]
GreenFieldsTRGround = ["Gunner", "Cannon", "Boomerang", "Bubble"]
WasteSandsTRGround = ["Missiler", "Spider", "Snowballer", "Shocker"]
GlacierLandsTRGround = ["D. Shotgunner", "Plasma", "Sniper"]
IronFortressRecommended = ["Missiler", "D. Shotgunner", "Plasma", "Hammer"]

print("Welcome to the random Minirobot roller! To start, write down what world are you in and hit [ENTER] to roll.")
episode = input("Which episode are you in? ")
while 2<3:
    world = input("What world are you in? ")
    randomity = random.randint(1,12)
    if world == "Green Fields":
        randomity = random.randint(1,12)
        if episode == "The Revenge":
            ProducerChoice = random.choice(Producer)
            print(ProducerChoice)
            randomity = random.randint(1,12)
            print(random.choice(LowSupport))
            if randomity <= 4:
                GroundSet = random.sample(GreenFieldsTRGround, 3)
                SpecialSet = random.sample(SpecialTR, 2)
                print(*GroundSet, sep = "\n")
                print(*AirUnits, sep = "\n")
                print(*SpecialSet, sep = "\n")
            elif randomity >= 8:
                AirSet = random.sample(AirUnits, 2)
                SpecialSet = random.sample(SpecialTR, 2)
                print(*GreenFieldsTRGround, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*SpecialSet, sep = "\n")
            else:
                GroundSet = random.sample(GreenFieldsTRGround, 2)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print("Freezer")
                SpecialSet = random.sample(SpecialTR, 3)
                print(*SpecialSet, sep = "\n")
        else:
            randomity = random.randint(1,12)
            if episode == "The Last Stand":
                print("Papa")
                print ("Fixer")
            else:
                ProducerChoice = random.choice(Producer)
                print(ProducerChoice)
                if ProducerChoice == "Papa":
                    print(random.choice(Support))
                else:
                    print(random.choice(LowSupport))
            if randomity <= 4:
                GroundSet = random.sample(GroundUnits, 3)
                AirSet = random.sample(AirUnits, 3)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
            elif randomity >= 8:
                GroundSet = random.sample(GroundUnits, 4)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
            else:
                GroundSet = random.sample(GroundUnits, 2)
                AirSet = random.sample(AirUnits, 2)
                ElementalSet = random.sample(ElementalUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*ElementalSet, sep = "\n")
            SpecialSet = random.sample(SpecialUnits, 2)
            print(*SpecialSet, sep = "\n")
    
    elif world == "Waste Sands":
        randomity = random.randint(1,12)
        ProducerChoice = random.choice(Producer)
        print(ProducerChoice)
        if episode == "The Revenge":
            if randomity <= 6:
                GroundSet = random.sample(GreenFieldsTRGround, 2)
                GroundAdd = random.sample(WasteSandsTRGround, 2)
                AirSet = random.sample(AirUnits, 2)
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*GroundAdd, sep = "\n")
                print(*AirSet, sep = "\n")
                if randomity <=3:
                    print(random.choice(Defense))
                    random.shuffle(Defense)
                else:
                    print(random.choice(AntiStealth))
                    random.shuffle(AntiStealth)
                print(*SpecialSet, sep = "\n")
            else:
                GroundSet = random.sample(GreenFieldsTRGround, 2)
                GroundAdd = random.sample(WasteSandsTRGround, 2)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*GroundAdd, sep = "\n")
                print(*AirSet, sep = "\n")
                print(random.choice(SpecialTR))
                random.shuffle(SpecialTR)
                if randomity >= 9:
                    print(random.choice(Defense))
                    random.shuffle(Defense)
                    randomity = random.randint(1,12)
                    if randomity <=6:
                        print("Flame")
                    else:
                        print("Freezer")
                else:
                    print(random.choice(AntiStealth))
                    random.shuffle(AntiStealth)
                    randomity = random.randint(1,12)
                    if randomity >=6:
                        print("Freezer")
                    else:
                        print("Flame")
        else:
            if episode == "The Last Stand":
                    print ("Fixer")
            else:
                    if ProducerChoice == "Papa":
                        print(random.choice(Support))
                    else:
                        print(random.choice(LowSupport))
            if randomity <= 6:
                GroundSet = random.sample(GroundUnits, 3)
                AirSet = random.sample(AirUnits, 2)
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                if randomity <=3:
                    print(random.choice(Defense))
                    random.shuffle(Defense)
                else:
                    print(random.choice(AntiStealth))
                    random.shuffle(AntiStealth)
                print(*SpecialSet, sep = "\n")
            else:
                GroundSet = random.sample(GroundUnits, 2)
                AirSet = random.sample(AirUnits, 2)
                ElementalSet = random.sample(ElementalUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*ElementalSet, sep = "\n")
                print(random.choice(SpecialUnits))
                random.shuffle(SpecialUnits)
                if randomity >= 9:
                    print(random.choice(Defense))
                    random.shuffle(Defense)
                else:
                    print(random.choice(AntiStealth))
                    random.shuffle(AntiStealth)
    
    elif world == "South Ocean":
        randomity = random.randint(1,12)
        
        if episode == "The Last Stand":
            print("Papa")
            print("Fixer")
            if randomity <= 4:
                GroundSet = random.sample(GroundUnits, 5)
                print(*GroundSet, sep = "\n")
                print(random.choice(UnderwaterUnits))
                random.shuffle(UnderwaterUnits)
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*SpecialSet, sep ="\n")
            elif randomity >= 8:
                GroundSet = random.sample(GroundUnits, 4)
                print(*GroundSet, sep = "\n")
                print(*UnderwaterUnits, sep = "\n")
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*SpecialSet, sep ="\n")
            else:
                GroundSet = random.sample(GroundUnits, 4)
                print(*GroundSet, sep = "\n")
                print(random.choice(UnderwaterUnits))
                random.shuffle(UnderwaterUnits)
                SpecialSet = random.sample(SpecialUnits, 3)
                print(*SpecialSet, sep ="\n")
            
        elif episode == "The Revenge":
            ProducerChoice = random.choice(Producer)
            print(ProducerChoice)
            if randomity >= 6:
                GroundSet = random.sample(GreenFieldsTRGround, 3)
                print(*GroundSet, sep = "\n")
                GroundAdd = random.sample(WasteSandsTRGround, 3)
                print(*GroundAdd, sep = "\n")
                print(random.choice(UnderwaterUnits))
                random.shuffle(UnderwaterUnits)
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*SpecialSet, sep ="\n")
            else:
                GroundSet = random.sample(GreenFieldsTRGround, 3)
                print(*GroundSet, sep = "\n")
                GroundAdd = random.sample(WasteSandsTRGround, 3)
                print(*GroundAdd, sep = "\n")
                print(*UnderwaterUnits, sep = "\n")
                SpecialSet = random.sample(SpecialUnits, 1)
                print(*SpecialSet, sep ="\n")
        else:
            ProducerChoice = random.choice(Producer)
            print(ProducerChoice)
            if ProducerChoice == "Papa":
                print(random.choice(Support))
            else:
                print(random.choice(LowSupport))
            GroundSet = random.sample(GroundUnits, 3)
            print(*GroundSet, sep = "\n")
            print(random.choice(UnderwaterUnits))
            random.shuffle(UnderwaterUnits)
            print(random.choice(Defense))
            random.shuffle(Defense)
            print(random.choice(AntiStealth))
            random.shuffle(AntiStealth)
            print(random.choice(SpecialSet))
            
    
    elif world == "Glacier Lands":
        randomity = random.randint(1,12)
        if episode == "The Revenge":
            ProducerChoice = "Papa"
            print(ProducerChoice)
            randomity = random.randint(1,12)
            if randomity <=8:
                GroundSet = random.sample(GroundUnits, 3)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*MarineUnits, sep = "\n")
            else:
                GroundSet = random.sample(GroundUnits, 4)
                AirSet = random.sample(AirUnits, 1)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                randomity = random.randint(1,12)
                if randomity <=4:
                    print(random.choice(ElementalUnits))
                    print(random.choice(MarineUnits))
                    random.shuffle(ElementalUnits)
                    random.shuffle(MarineUnits)
                else:
                    print(*MarineUnits, sep = "\n")
            print(random.choice(SpecialUnits))
            print(random.choice(AntiStealth))
        elif episode == "The Last Stand":
            ProducerChoice = "Papa"
            print(ProducerChoice)
            if randomity <=8:
                GroundSet = random.sample(GroundUnits, 4)
                AirSet = random.sample(AirUnits, 1)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*MarineUnits, sep = "\n")
            else:
                GroundSet = random.sample(GroundUnits, 4)
                AirSet = random.sample(AirUnits, 1)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(random.choice(ElementalUnits))
                print(random.choice(MarineUnits))
                random.shuffle(ElementalUnits)
                random.shuffle(MarineUnits)
            print(random.choice(SpecialUnits))
            print(random.choice(AntiStealth))
        else:
            ProducerChoice = random.choice(Producer)
            print(ProducerChoice)
            if ProducerChoice == "Papa":
                print(random.choice(Support))
            else:
                print(random.choice(LowSupport))
            if randomity <=8:
                GroundSet = random.sample(GroundUnits, 2)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(*MarineUnits, sep = "\n")
            else:
                GroundSet = random.sample(GroundUnits, 2)
                AirSet = random.sample(AirUnits, 2)
                print(*GroundSet, sep = "\n")
                print(*AirSet, sep = "\n")
                print(random.choice(ElementalUnits))
                print(random.choice(MarineUnits))
                random.shuffle(ElementalUnits)
                random.shuffle(MarineUnits)
            print(random.choice(SpecialUnits))
            print(random.choice(AntiStealth))
    
    elif world == "Iron Fortress":
        randomity = random.randint(1,12)
        
        if episode == "The Revenge":
            print("Papa")
            print("Barrier")
            if randomity >= 4:
                print(*IronFortressRecommended, sep = "\n")
            else:
                HeavySet = random.sample(HighDamage, 2)
                print(*HeavySet, sep = "\n")
                print("Hammer")
                print(random.choice(GroundDefense))
            print(random.choice(DamageSpecial))
            print("Float")
            print(*MarineUnits, sep = "\n")
        elif episode == "The Last Stand":
            print("Papa")
            print("Barrier")
            if randomity <= 2:
                print(*IronFortressRecommended, sep = "\n")
            else:
                HeavySet = random.sample(HighDamage, 4)
                print(*HeavySet, sep = "\n")
            print(random.choice(DamageSpecial))
            print("Float")
            print(*MarineUnits, sep = "\n")
        else:
            print(random.choice(Producer))
            print(random.choice(LowSupport))
            if randomity <=6:
                if randomity <= 3:
                    HeavySet = random.sample(HighDamage, 4)
                    print(*HeavySet, sep = "\n")
                else:
                    GroundSet = random.sample(GroundUnits, 4)
                    print(*GroundSet, sep = "\n")
                print(random.choice(AirUnits))
                print(random.choice(MarineUnits))
            else:
                if randomity >= 9:
                    HeavySet = random.sample(HighDamage, 2)
                    print(*HeavySet, sep = "\n")
                else:
                    GroundSet = random.sample(GroundUnits, 2)
                    print(*GroundSet, sep = "\n")
                print(*MarineUnits, sep = "\n")
                print(random.choice(AirUnits))
            if randomity <= 2:
                SpecialSet = random.sample(SpecialUnits, 2)
                print(*SpecialSet, sep = "\n")
            elif randomity >= 6:
                print("Hammer")
                print(random.choice(DamageSpecial))
            else:
                print(random.choice(SpecialUnits))
                print(random.choice(AntiStealth))
            
