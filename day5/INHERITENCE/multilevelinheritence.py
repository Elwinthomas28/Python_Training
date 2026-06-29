class grandfather:
    def skill(self):
        print("reading current affairs")
class father(grandfather):
    def fatherskill(self):
        print("making money")
class son(father):
    def sonskill(self):
        print("1.watching reel")
Son=son()
Son.sonskill()
Son.fatherskill()
Son.skill()