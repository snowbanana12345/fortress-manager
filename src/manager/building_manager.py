from src.building.builder import Builder
from src.building.production_building import ProductionBuilding
from src.resource.resource_collector import ResourceCollector


class BuildingManager:
    def __init__(self):
        self.buildings = []
        self.builder = Builder()

    def produce(self):
        resource_collector = ResourceCollector()
        for building in self.buildings:
            if isinstance(building, ProductionBuilding):
                amount, resource_type = building.produce()
                resource_collector.add(amount, resource_type)
        return resource_collector

    def build(self, name, id_number):
        try:
            new_building = self.builder.build(name, id_number)
            self.buildings.append(new_building)
        except ValueError:
            print("building : " + name + " was not built.")

    def getCost(self, name):
        try:
            return self.builder.getCost(name)
        except ValueError:
            print("building : " + name + " was not built.")
            return ResourceCollector()

    def demolish(self, id_number):
        pointer = None
        for i in range(len(self.buildings)):
            building = self.buildings[i]
            if building.getId() == id_number:
                pointer = i
        try:
            self.buildings.pop(pointer)
        except TypeError:
            print("There is no building with this id to demolish!")

    def __str__(self):
        string = "building manager + \n"
        for building in self.buildings:
            string += str(building) + "\n"
        return string

