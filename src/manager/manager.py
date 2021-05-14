from src.command.command_fields import CommandFields
from src.command.commands import Commands
from src.manager.building_manager import BuildingManager
from src.manager.id_manager import IdManager
from src.resource.player_resource_collector import PlayerResourceCollector
from src.resource.resource_collector import ResourceCollector


class Manager:
    def __init__(self):
        self.building_manager = BuildingManager()
        self.resource_collector = PlayerResourceCollector()
        self.id_manager = IdManager()

    def recieveCommand(self, command):
        if command.getCommandType() == Commands.BUILD:
            return self.handle_build_command(command)
        elif command.getCommandType() == Commands.DEMOLISH:
            return self.handle_demolish_command(command)
        else:
            print("Invalid command type : " + str(command))
            raise Exception

    def handle_demolish_command(self, command):
        building_id = command.getField(CommandFields.ID)
        self.building_manager.demolish(building_id)
        return 0

    def handle_build_command(self, command):
        building_name = command.getField(CommandFields.NAME)
        cost = self.building_manager.getCost(building_name)
        if self.resource_collector.subtract(cost):
            return self.build(building_name)
        else:
            return 0

    def build(self, name):
        building_id = self.id_manager.generateID()
        self.building_manager.build(name, building_id)
        return building_id

    def produce(self):
        temp_resource_collector = self.building_manager.produce()
        self.resource_collector.add_all(temp_resource_collector)

    def __str__(self):
        return str(self.building_manager) + "\n" + str(self.resource_collector)