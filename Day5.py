class Animals():
    def __init__(self, Name, Age, Colour):
        print("This init function belongs to Animal class.")
        self.name=Name
        self.age=Age
        self.colour=Colour


    def showInfo(self):
        print("Info about animals!")
        print("Name:{}\n Age:{}\n Colour:{}".format(self.name,self.age,self.colour))

class Dogs(Animals):
    def __init__(self, Name, Age, Colour, Number_of_legs, Sex):
        super().__init__(Name,Age,Colour)
        print("This init function belongs to Dogs class.")
        self.number_of_legs = Number_of_legs
        self.sex = Sex

    def showInfo(self):
        print("Info about dogs!")
        print("Name:{}\n Age:{}\n Colour:{}\n Number_of_legs:{}\n Sex:{}".format(self.name,self.age,self.colour,self.number_of_legs,self.sex))

class Cats(Dogs):
    def __init__(self, Name, Age, Colour, Number_of_legs, Sex, Species):
        super().__init__(Name, Age, Colour, Number_of_legs, Sex)
        self.species=Species

    def showInfo(self):
        print("Info about cats!")
        print("Name:{}\n Age:{}\n Colour:{}\n Number_of_legs:{}\n Sex:{}\n Species:{}".format(self.name,self.age,self.colour,self.number_of_legs,self.sex,self.species))

#animal1=Animals("hawk",8,"black",2)
#animal1.showInfo()

#max = Dogs("Max",8,"white",4,"male")
#max.showInfo()

cat = Cats("Ceku",2,"Snow White",4,"Female","Bengal Cat")
cat.showInfo()





