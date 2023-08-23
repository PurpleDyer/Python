from datetime import datetime

class Anim:

    def __init__(self, name, freeroam, switch):
        self.name = name
        self.freeroam = freeroam
        self.switch = switch

        
    def intro(self):
        return f"HI EVERYONE! MY NAME IS {(self.name).upper}! I WISH WE ALL HAVE THE BEST PARTY IN THE WORLD"


    class Head:

        def __init__(self, mouth, eyes, ears, eyebrows, headendo):
            self.mouth = mouth
            self.eyes = eyes
            self.ears = ears
            self.eyebrows = eyebrows
            self.headendo = headendo


        def __str__(self):
            print(f""" State Mouth = {self.mouth}
                State Eyes = {self.eyes}
                State Ears = {self.ears}
                State Eyebrows = {self.eyebrows}
                State HeadEndo = {self.headendo}
            """)


    class Torso:

        def __init__(self, bowtie, chest, body, bodyendo):
            self.bowtie = bowtie
            self.chest = chest
            self.body = body
            self.bodyendo = bodyendo


        def __str__(self):
            print(f""" State: Bowtie = {self.bowtie}
                State: Chest = {self.chest}
                State: Body = {self.body}
                State: BodyEndo = {self.bodyendo}
            """)


    class Legs:

        def __init__(self, legs, feet, legsendo):
            self.legs = legs
            self.feet = feet
            self.legsendo = legsendo


        def __str__(self):
            print(f""" State: Legs = {self.legs}
                State: Feet = {self.feet}
                State: LegsEndo = {self.legsendo}
            """)

time = int(str(str(datetime.now()).split()[-1]).split(':')[0])-1
roam = 0 < time < 6 or time == 24
Freddy = Anim("Freddy", roam, True)
print(Freddy.freeroam)
