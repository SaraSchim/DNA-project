from DNA_project.manipulation_commands.concat import Concat
from DNA_project.manipulation_commands.slice import Slice
from DNA_project.parse_strategy import Parse, manipulation_parse


# a factory class for Manipulation commands
class Manipulation:
    def __init__(self, command):
        self.command = command
        self.commands = {
            "slice": Slice,
            "concat": Concat
        }

    def execute(self):
        parser = Parse(self.command, manipulation_parse)    # parse with the specific function of Manipulation commands
        parser.parse_command()
        command_list = parser.command_list
        command_to_exe = self.commands[command_list[0]](command_list[1:])
        command_to_exe.execute()
