from src.resource.resource import Resource
from src.resource.resource_collector import ResourceCollector


class PlayerResourceCollector(ResourceCollector):
    def __init__(self):
        super().__init__()
    # initializes the resources to starting values
        self.resources = {
            Resource.FOOD: 1000,
            Resource.GOLD: 200,
            Resource.IRON: 200,
            Resource.WOOD: 1000,
        }

    # subtract the cost from the resource, resources cannot be negative,
    # returns False if any of the resources will end up negative without performing any deduction
    # returns True if the deduction is successful
    def subtract(self, cost):
        temp_resources = {}
        for resource_type in self.resources:
            temp_resources[resource_type] = self.resources[resource_type]
        for resource_type in self.resources:
            new_resources_value = temp_resources[resource_type] - cost.resources[resource_type]
            if new_resources_value < 0:
                return False
            temp_resources[resource_type] = new_resources_value
        self.resources = temp_resources
        return True

