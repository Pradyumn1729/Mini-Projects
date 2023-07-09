class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("talk")
information=Person("john")
print(information.name)
information.talk()    
    