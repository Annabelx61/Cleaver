class SkillStats:
    def __init__(self, nametag, tohit, damage, acbonus, init, move, reduct, type):
        self.nametag = nametag
        self.tohit = tohit
        self.damage = damage
        self.acbonus = acbonus
        self.init = init
        self.move = move
        self.reduct = reduct
        self.type = type

# Defining all Tier I skills
#   0 = Offensive
#   1 = Defensive
#   2 = Movement
tierI_offA = SkillStats('+1 to Hit (Offensive)', 1, 0, 0, 0, 0, 0, 0)
tierI_offB = SkillStats('+1 Damage (Offensive)', 0, 1, 0, 0, 0, 0, 0)
tierI_defA = SkillStats('+1 Armor Class (Defensive)', 0, 0, 1, 0, 0, 0, 1)
tierI_defB = SkillStats('+1 Damage Reduction (Defensive)', 0, 0, 0, 0, 0, 1, 1)
tierI_movA = SkillStats('+1 Initiative (Movement)', 0, 0, 0, 1, 0, 0, 2)
tierI_movB = SkillStats('+1 Movement (Movement)', 0, 0, 0, 0, 1, 0, 2)

skills_tierI = [tierI_offA, tierI_offB, tierI_defA, tierI_defB, tierI_movA, tierI_movB]