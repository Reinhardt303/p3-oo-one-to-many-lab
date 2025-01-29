class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = ''):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Not a valid pet type")
       
        self.name = name
        self.pet_type = pet_type
        self.owner = owner 
        Pet.all.append(self)
    

class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            if pet.owner is None:
                pet.owner = self
                self._pets.append(pet)
            elif pet.owner != self:
                raise ValueError(f"This pet already belongs to {pet.owner.name}.")
        else:
            raise ValueError("Only instances of Pet can be added.")
        
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

        
