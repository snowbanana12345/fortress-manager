from src.building.building_name_list import BuildingNameList
from src.building.production_building import ProductionBuilding
from src.resource.resource import Resource
from src.resource.resource_collector import ResourceCollector
from src.resource.resource_name_list import ResourceNameList


class GoldMine(ProductionBuilding):
    def __init__(self, building_id):
        super().__init__(BuildingNameList.GOLD_MINE, building_id, 1, Resource.GOLD)
        self.cost = ResourceCollector()
        self.cost.add(200, Resource.WOOD)
        self.cost.add(25, Resource.IRON)
        self.cost.add(50, Resource.GOLD)
        self.cost.add(100, Resource.FOOD)

    def __str__(self):
        return super().__str__() + " resource : " + ResourceNameList().getName(Resource.GOLD)
