from DNA_project.management_commands.delete import Delete
from DNA_project.management_commands.save import Save
from DNA_project.parse_strategy import management_parse, Parse


# a factory class for Management commands
class Management:
    def __init__(self, command):
        self.command = command
        self.commands = {
            "del": Delete,
            "save": Save
        }

    def execute(self):
        parser = Parse(self.command, management_parse)      # parse with the specific function of Management commands
        parser.parse_command()
        command_list = parser.command_list
        command_to_exe = self.commands[command_list[0]](command_list[1:])
        command_to_exe.execute()
