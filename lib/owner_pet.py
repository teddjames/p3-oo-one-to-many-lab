class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of Pet instances owned by this owner."""
        # Filter all pets by owner
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign a Pet to this Owner."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")
        pet.owner = self
        return pet

    def get_sorted_pets(self):
        """Return the pets owned by this owner, sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        # Add to registry
        Pet.all.append(self)
        # If owner provided, assign via add_pet to enforce checks
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            owner.add_pet(self)
