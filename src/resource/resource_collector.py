from src.resource.resource import Resource
from src.resource.resource_name_list import ResourceNameList


class ResourceCollector:
    def __init__(self):
        self.resources = {
            Resource.FOOD: 0,
            Resource.GOLD: 0,
            Resource.IRON: 0,
            Resource.WOOD: 0,
        }

    def add(self, amount, resource_type):
        self.resources[resource_type] += amount

    def add_all(self, other):
        for resource_type in self.resources:
            self.resources[resource_type] += other.resources[resource_type]

    def __str__(self):
        string = "resource collector" + "\n"
        for resource_type in self.resources:
            string += ResourceNameList().getName(resource_type) + " amount : " + str(self.resources[resource_type]) + "\n"
        return string