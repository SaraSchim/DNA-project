from DNA_project.creation_commands.dup import Dup
from DNA_project.creation_commands.load import Load
from DNA_project.creation_commands.new import New
from DNA_project.parse import creation_parse, Parse


class Creation:
    def __init__(self, command):
        self.command = command
        self.commands = {
            "new": New,
            "load": Load,
            "dup": Dup,
        }

    def execute(self):
        parser = Parse(self.command, creation_parse)
        parser.parse_command()
        command_list = parser.command_list
        command_to_exe = self.commands[command_list[0]](command_list[1:])
        command_to_exe.execute()
