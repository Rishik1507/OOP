class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

penguin=parrot("penguin",12)
peacock=parrot("peacock",10)
print("penguin is a ",penguin.species)
print(f'Peacock is a {peacock.species}')
print(f'{penguin.name} is {penguin.age} yrs old')
print(f'{peacock.name} is {peacock.age} yrs old')
        