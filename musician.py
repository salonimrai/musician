class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        print("created a musician")

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()


class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self): # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Crash", "Thump"])
    
    def count(self):
        print("1... 2... 3... FOUR!")
    
    def selfCombust(self):
        print("Drummer has combusted")
        

class Band(object):
    members = {"Bassist": None,"Guitarist":None,"Drummer":None,}
    
    def hire(self, artist):
        memberType = type(artist).__name__
        try:
            self.members[memberType] = artist
        except:
            print("Wrong band member type")
    
    def fire(self, artist):
        memberType = type(artist).__name__
        try:
            self.members[memberType] = None
        except:
            print("Wrong band member type")


if __name__ == "__main__":
    print("Starting up..")
    dave = Guitarist()
    mike = Bassist()
    tom = Drummer()
    mike.solo(5)
    dave.tune()
    tom.count()
    redHot = Band()
    redHot.hire(dave)
    print(redHot.members)
    dave2 = redHot.members[type(dave).__name__]
    dave2.tune()
    redHot.fire(dave)
    print(redHot.members)
    
