import numpy as np

class ArmorStats:
    def __init__(self, nametag, tier, acbonus, dmgred):
        self.nametag = nametag
        self.tier = tier
        self.acbonus = acbonus
        self.dmgred = dmgred

# Defining all Tier I armors
smallshield = ArmorStats('Small Shield', 1, 1, np.random.randint(1, 3))
leftgreave = ArmorStats('Left Greave', 1, 0, np.random.randint(1, 3))
rightgreave = ArmorStats('Right Greave', 1, 0, np.random.randint(1, 3))
smallhelm = ArmorStats('Small Helm', 1, 0, np.random.randint(1, 4))
leftarmguard = ArmorStats('Left Armguard', 1, 0, np.random.randint(1, 3))
rightarmguard = ArmorStats('Right Armguard', 1, 0, np.random.randint(1, 3))
broadbelt = ArmorStats('Broadbelt', 1, 0, np.random.randint(1, 3))
leftshoulderguard = ArmorStats('Left Shoulderguard', 1, 0, np.random.randint(1, 3))
rightshoulderguard = ArmorStats('Right Shoulderguard', 1, 0, np.random.randint(1, 3))

armors_tier1 = [smallshield, leftgreave, rightgreave, smallhelm, leftarmguard, rightarmguard,
                broadbelt, leftshoulderguard, rightshoulderguard]