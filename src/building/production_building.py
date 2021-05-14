from src.building.building import Building

class ProductionBuilding(Building):
    def __init__(self, name, building_id, base_production, resource_type):
        super().__init__(name, building_id)
        self.base_production = base_production
        self.resource_type = resource_type

    def produce(self):
        return (self.base_production, self.resource_type)

    def __str__(self):
        return super().__str__() + " production : " + str(self.base_production)


