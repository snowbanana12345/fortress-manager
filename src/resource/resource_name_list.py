from src.resource.resource import Resource


class ResourceNameList:
    def __init__(self):
        self.name_list = {
            Resource.FOOD : "food",
            Resource.IRON : "iron",
            Resource.GOLD : "gold",
            Resource.WOOD : "wood"
        }

    def getName(self, resource_type):
        return self.name_list[resource_type]
