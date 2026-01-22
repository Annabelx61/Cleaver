import numpy as np
import weapons
import armors
import skills

# Defining class of 'character'
class Character:
    def __init__(self, nametag, might, agility, toughness, comeliness, maxhp,
                 currenthp, ac, skill, weapon, armor1, armor2, tier, index):
        self.name = nametag
        self.might = might
        self.agility = agility
        self.toughness = toughness
        self.comeliness = comeliness
        self.maxhp = maxhp
        self.currenthp = currenthp
        self.skill = skill
        self.weapon = weapon
        self.armor1 = armor1
        self.armor2 = armor2
        self.tier = tier
        self.index = index

# Importing list of names
lastNameList = []
with open("lastnamelist.txt") as file:
    for line in file:
        stripped_line = line.strip()
        lastNameList.append(stripped_line)

firstNameList = []
with open("firstnamelist.txt") as file:
    for line in file:
        stripped_line = line.strip()
        firstNameList.append(stripped_line)

# Attribute stuff
attributeList = ['Might', 'Agility', 'Toughness', 'Comeliness', 'Hit Points']
attributeBonus = {1: -5, 2: -5, 3: -4, 4: -4, 5: -3, 6: -3, 7: -2, 8: -2, 9: -1, 10: -1, 11: 0, 14: 0, 15: 1, 16: 1, 17: 2, 18: 2, 19: 3, 20: 3, 21: 4, 22: 4, 23: 5, 24: 5}

char_index = 0
characterList = []
def generateRandomCharacter():
    # Which tier? (placeholder)
    tier = 1

    # Global character index
    global char_index
    char_index += 1

# Generating Name
    # Getting first name
    index = np.random.randint(0, len(firstNameList))
    firstname = firstNameList[index]

    # Getting last name
    index = np.random.randint(0, len(lastNameList))
    lastname = lastNameList[index]

    name = firstname + ' ' + lastname

# Generating Attributes
    # Selecting specialty attribute
    specialty = np.random.randint(0, 4)

    # Generating attribute stats
    attributeScores = []
    for i in range(len(attributeList)):
        score = np.sum(np.random.randint(1, 5, size=5))
        attributeScores.append(score)

    attributeScores[specialty] = attributeScores[specialty] + np.random.randint(1, 3)
    attributeScores[4] += 10

# Generating Equipment
    # Randomizing which weapon
    weaponValue = np.random.randint(0, 10)

    # Fetching weapon
    weapon = weapons.weapons_tier1[weaponValue]


    # Randomizing armor
    #armorValue = np.random.randint(0, 10
    armorValue = 9
    if armorValue == 9:
        armor1Value = np.random.randint(0, 9)
        armor2Value = np.random.randint(0, 9)
        while armor1Value == armor2Value:
            armor2Value = np.random.randint(0, 9)

        armor1 = armors.armors_tier1[armor1Value]
        armor2 = armors.armors_tier1[armor2Value]
    else:
        armor = armors.armors_tier1[armorValue]

# Skill Generation
    # Randomize the skill
    skillValue = np.random.randint(0, 6)

    # Fetching Skill
    skill = skills.skills_tierI[skillValue]

# Displaying all randomized info
    # First, see if there are 1 or 2 armor pieces -- print based on that (also define total AC bonus)
    if 'armor' in locals():
        # AC bonus
        acbonus = armor.acbonus + skill.acbonus

        # Name
        print(name + ' -- ' + 'AC: ' + str(10 + armor.acbonus + skill.acbonus))

        # Equipment
        print('Weapon: ' + weapon.nametag + ' -- Armor: ' + armor.nametag + '\n')
    else:
        # AC bonus
        acbonus = armor1.acbonus + armor2.acbonus + skill.acbonus

        # Name
        print(name + ' -- ' + 'AC: ' + str(10 + armor1.acbonus + armor2.acbonus + skill.acbonus))

        # Equipment
        print('Weapon: ' + weapon.nametag + ' -- Armor: ' + armor1.nametag + ', ' + armor2.nametag + '\n')

    # Attributes
    print('Might:        ' + str(attributeScores[0]) + '\n'
          'Agility:      ' + str(attributeScores[1]) + '\n'
          'Toughness:    ' + str(attributeScores[2]) + '\n'
          'Comeliness:   ' + str(attributeScores[3]) + '\n'
          'Lifepoints:   ' + str(attributeScores[4]) + '\n')

    # Specialty & Skill
    print('Specialty: ' + attributeList[specialty])
    print('Skill: ' + skill.nametag)

    # Defining character class
    if 'armor' in locals():
        character = Character(name, attributeScores[0], attributeScores[1], attributeScores[2], attributeScores[3],
                              attributeScores[4], attributeScores[4], 10 + acbonus, skill, weapon, armor, 0, tier,
                              char_index)
    else:
        character = Character(name, attributeScores[0], attributeScores[1], attributeScores[2], attributeScores[3],
                              attributeScores[4], attributeScores[4], 10 + acbonus, skill, weapon, armor1, armor2, tier,
                              char_index)
    characterList.append(character)

generateRandomCharacter()
print(char_index)
generateRandomCharacter()
print(char_index)
generateRandomCharacter()
print(char_index)
print(characterList)

print(characterList[2].index)