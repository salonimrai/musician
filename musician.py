class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
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
        super().__init__(["Bang", "Crash", "Thump")
    
    def count(self):
        print("1... 2... 3... FOUR!")
    
    def selfCombust(self):
        print("Drummer has combusted")
        

class Band(object):
    members = {"Bassist":,"Guitarist":,"Drummer":}
    
    def hire(self, artist):
        memberType = type(artist)
        try:
            members.[memberType] = artist
        except:
            print("Wrong band member type")
    
    def fire(self, artist):
        memberType = type(artist)
        try:
            members.[memberType] = None
        except:
            print("Wrong band member type")


    
