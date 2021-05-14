from src.resource.resource_collector import ResourceCollector


class Building:
    def __init__(self, name, building_id):
        self.name = name
        self.building_id = building_id # the id used to reference the building
        self.cost = ResourceCollector()

    def getId(self):
        return self.building_id

    def getCost(self):
        return self.cost

    def __str__(self):
        return self.name + " id : " + str(self.building_id)



