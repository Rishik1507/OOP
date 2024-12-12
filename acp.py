class robot():
    def __init__(self,name,place):
        self.name=name
        self.place=place
       
        
    def n(self):
       
        print(f'I am {self.name}')
    def p(self):
        
        print(f'I was made in {self.place}')
rob=robot("Tom","USA")
rob.n()
rob.p()

        