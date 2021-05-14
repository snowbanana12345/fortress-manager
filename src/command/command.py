from src.command.command_fields import CommandFields
from src.command.commands_name_list import CommandsNameList


class Command:
    def __init__(self, command_type):
        self.command_type = command_type
        self.fields = {
            CommandFields.NAME : None,
            CommandFields.AMOUNT : None,
        }

    def getCommandType(self):
        return self.command_type

    def putField(self, field, value):
        self.fields[field] = value

    def getField(self, field):
        return self.fields[field]

    def __str__(self):
        return "command type : " + CommandsNameList().getName(self.command_type)


