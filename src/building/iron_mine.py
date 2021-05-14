from src.building.building_name_list import BuildingNameList
from src.building.production_building import ProductionBuilding
from src.resource.resource import Resource
from src.resource.resource_collector import ResourceCollector
from src.resource.resource_name_list import ResourceNameList


class IronMine(ProductionBuilding):
    def __init__(self, building_id):
        super().__init__(BuildingNameList.IRON_MINE, building_id, 5, Resource.IRON)
        self.cost = ResourceCollector()
        self.cost.add(150, Resource.WOOD)
        self.cost.add(15, Resource.IRON)
        self.cost.add(50, Resource.GOLD)

    def __str__(self):
        return super().__str__() + " resource : " + ResourceNameList().getName(Resource.IRON)