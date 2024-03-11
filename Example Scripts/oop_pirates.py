##class Pirate:
##    def __init__ (self, name, age, weapon):
##        self.name = name
##        self.age = age
##        self.weapon = weapon
##
##    def attack(self):
##        print(f"{self.name} attacks with their {self.weapon}!")
##
##    def plunder(self):
##        print(f"{self.name} is plundering the ship!!")


class Ship:
    def __init__ (self, name, captain, max_crew, current_crew):
        self.name = name
        self.captain = captain
        self.max_crew = max_crew
        self.current_crew = current_crew

    def set_sail(self):
        print(f"The Ship {self.name} is ready to sail\nwith {pirate1.rank} {pirate1.name} at the helm and his crew of {self.current_crew}")

class CrewMember:
    def __init__ (self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

class Pirate(CrewMember):
    rank = 'Captain'
    def steer(self):
        print(f"\n{self.rank} {self.name} calls for all ahead!!!")
        print(f"{self.rank} {self.name} demands his small crew of {ship1.current_crew} be filled to capacity of {ship1.max_crew}")

        
crew_mem1 = CrewMember("One-Eyed Willie", 56, "cook")
crew_mem2 = CrewMember("Smalls", 32, "thief")
pirate1 = Pirate("Blackbeard", 62, "Master Sailor")
ship1 = Ship("Black Oyster", "Blackbeard", 30, 20)
ship1.set_sail()
pirate1.steer()

        
