from src.building.building_name_list import BuildingNameList
from src.building.production_building import ProductionBuilding
from src.resource.resource import Resource
from src.resource.resource_collector import ResourceCollector
from src.resource.resource_name_list import ResourceNameList


class LumberMill(ProductionBuilding):
    def __init__(self, building_id):
        super().__init__(BuildingNameList.LUMBER_MILL, building_id, 10, Resource.WOOD)
        self.cost = ResourceCollector()
        self.cost.add(100, Resource.WOOD)
        self.cost.add(10, Resource.IRON)
        self.cost.add(20, Resource.GOLD)

    def __str__(self):
        return super().__str__() + " resource : " + ResourceNameList().getName(Resource.WOOD)


