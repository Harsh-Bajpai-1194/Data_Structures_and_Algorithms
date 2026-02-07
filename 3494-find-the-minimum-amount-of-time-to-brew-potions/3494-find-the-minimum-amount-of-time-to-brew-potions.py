class Solution(object):
    def minTime(self, skill, mana):
        sumSkill = sum(skill)
        prevWizardDone = sumSkill * mana[0]
        for j in range(1, len(mana)):
            prevPotionDone = prevWizardDone
            for i in range(len(skill) - 2, -1, -1):
                prevPotionDone -= skill[i + 1] * mana[j - 1]
                prevWizardDone = max(prevPotionDone,prevWizardDone - skill[i] * mana[j])
            prevWizardDone += sumSkill * mana[j]
        return prevWizardDone