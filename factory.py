from DNA_project.creation_commands.creation_factory import Creation
from DNA_project.management_commands.management_factory import Management
from DNA_project.manipulation_commands.manipulation_factory import Manipulation


class Factory:
    def __init__(self):
        """Factory Method"""
        self.command_type = {
            "new": Creation,
            "load": Creation,
            "dup": Creation,
            "slice": Manipulation,
            "concat": Manipulation,
            "del": Management,
            "save": Management
        }

    def execute_command(self, command):
        command_list = command.split(' ')
        if command_list[0] not in self.command_type.keys():
            raise Exception("invalid command")
        command_to_exe = self.command_type[command_list[0]](command)
        command_to_exe.execute()
