from src.command.commands import Commands


class CommandsNameList:
    def __init__(self):
        self.name_list = {
            Commands.BUILD : "build"
        }

    def getName(self, command_type):
        return self.name_list[command_type]
