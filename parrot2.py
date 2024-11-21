class parrot:
    def __init__(self,name):
        self.name=name
    def hobby(self,hob):
        return self.name +" likes "+ hob
    def ambition(self,amb):
        return self.name+" wants to become "+amb
obj=parrot("Rishik")
print(obj.hobby("coding"))
print(obj.ambition("coder"))

    
    



