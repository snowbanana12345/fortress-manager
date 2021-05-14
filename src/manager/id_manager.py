import random

class IdManager:
    def __init__(self):
        self.Ids = []

    # dont ever exceed 100000 distinct IDs
    def generateID(self):
        new_id = random.randint(10000,99999)
        while new_id in self.Ids:
            new_id = random.randint(10000,99999)
        self.Ids += [new_id]
        return new_id

    def removeID(self, id_number):
        self.Ids.remove(id_number)

