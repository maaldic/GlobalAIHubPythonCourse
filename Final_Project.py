class Employees():
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
        self.language = set({})

    def addLanguage(self,languageList):
        self.language.add(languageList)

    def showInfo(self):
        for i in self.language:
            print(i)

class Manager():
    def __init__(self,firstName, lastName, mAge, mLanguage):
        self.firstName = firstName
        self.lastName = lastName
        self.m_age = mAge
        self.m_language = mLanguage

employee1 = Employees("Mehmet Ali", 23)
employee1.addLanguage("French")
employee1.addLanguage("French")
employee1.addLanguage("English")

employee2 = Employees("Van Gogh", 38)
employee2.addLanguage("Deutsch")

employee3 = Employees("Rıfat Ilgaz", 56)
employee3.addLanguage("Turkish")

employees = [employee1, employee2, employee3]

for i in employees:
    #print( str(i) + "can speak these language(s):")
    i.showInfo()


