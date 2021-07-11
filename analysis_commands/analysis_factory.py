from DNA_project.analysis_commands.count import Count
from DNA_project.analysis_commands.find import Find
from DNA_project.analysis_commands.find_all import FindAll
from DNA_project.analysis_commands.len import Len
from DNA_project.parse_strategy import Parse, analysis_parse


class Analysis:
    def __init__(self, command):
        self.command = command
        self.commands = {
            "find": Find,
            "findall": FindAll,
            "len": Len,
            "count": Count
        }

    def execute(self):
        parser = Parse(self.command, analysis_parse)
        parser.parse_command()
        command_list = parser.command_list
        command_to_exe = self.commands[command_list[0]](command_list[1:])
        command_to_exe.execute()
