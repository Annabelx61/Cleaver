import numpy as np

class WeaponStats:
    def __init__(self, nametag, tier, randdmg, bonusdmg):
        self.nametag = nametag
        self.tier = tier
        self.randdmg = randdmg
        self.bonusdmg = bonusdmg

# List of all Tier I weapons
dagger = WeaponStats('Dagger', 1, np.sum(np.random.randint(1, 5, size = 2)), 0)
smallsword = WeaponStats('Small Sword', 1, np.sum(np.random.randint(1, 5, size = 3)), 0)
smallmace = WeaponStats('Small Mace', 1, np.random.randint(1, 9, size = 1), 0)
smallhammer = WeaponStats('Small Hammer', 1, np.random.randint(1, 7, size = 1), 0)
shortspear = WeaponStats('Short Spear', 1, np.sum(np.random.randint(1, 5, size = 3)), 0)
mailedfist = WeaponStats('Mailed Fist', 1, np.random.randint(1, 5, size = 1), 0)
smallaxe = WeaponStats('Small Axe', 1, np.sum(np.random.randint(1, 5, size = 2)), 0)
club = WeaponStats('Club', 1, np.random.randint(1, 7, size = 1), 0)
smalltrident = WeaponStats('Small Trident', 1, np.random.randint(1, 9, size = 1), 0)
cleaver = WeaponStats('Cleaver', 1, np.random.randint(1, 11, size = 1), 0)

# Tier I weapons list
weapons_tier1 = [dagger, smallsword, smallmace, smallhammer, shortspear, mailedfist,
                 smallaxe, club, smalltrident, cleaver]