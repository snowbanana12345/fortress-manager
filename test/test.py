from src.building.building_name_list import BuildingNameList
from src.command.command import Command
from src.command.command_fields import CommandFields
from src.command.commands import Commands
from src.manager.manager import Manager

cmd1 = Command(Commands.BUILD)
cmd2 = Command(Commands.BUILD)
cmd1.putField(CommandFields.NAME, BuildingNameList.FARM)
cmd2.putField(CommandFields.NAME, BuildingNameList.IRON_MINE)


manager = Manager()
id1 = manager.recieveCommand(cmd1)
id2 = manager.recieveCommand(cmd2)
manager.produce()
print(str(manager))

cmd3 = Command((Commands.DEMOLISH))
cmd3.putField(CommandFields.ID, id1)
manager.recieveCommand(cmd3)
manager.produce()
print(str(manager))