from src.building.farm import Farm
from src.building.gold_mine import GoldMine
from src.building.iron_mine import IronMine
from src.building.lumber_mill import LumberMill
from src.building.building_name_list import BuildingNameList


class Builder:
    def __init__(self):
        pass

    def build(self, building_name, id):
        if building_name == BuildingNameList.GOLD_MINE:
            return self.buildBasicGoldMine(id)
        elif building_name == BuildingNameList.LUMBER_MILL:
            return self.buildBasicLumberMill(id)
        elif building_name == BuildingNameList.FARM:
            return self.buildBasicFarm(id)
        elif building_name == BuildingNameList.IRON_MINE:
            return self.buildBasicIronMine(id)
        else:
            print("building name : " + building_name + " is invalid!")
            raise ValueError

    def getCost(self, building_name):
        if building_name == BuildingNameList.GOLD_MINE:
            return GoldMine(0).getCost()
        elif building_name == BuildingNameList.LUMBER_MILL:
            return LumberMill(0).getCost()
        elif building_name == BuildingNameList.FARM:
            return Farm(0).getCost()
        elif building_name == BuildingNameList.IRON_MINE:
            return IronMine(0).getCost()
        else:
            print("building name : " + building_name + " is invalid!")
            raise ValueError


    def buildBasicLumberMill(self, id):
        return LumberMill(id)

    def buildBasicGoldMine(self, id):
        return GoldMine(id)

    def buildBasicIronMine(self, id):
        return IronMine(id)

    def buildBasicFarm(self, id):
        return Farm(id)