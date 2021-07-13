from DNA_project.analysis_commands.analysis_factory import Analysis
from DNA_project.cli.batch.batch_factory import BatchFactory
from DNA_project.creation_commands.creation_factory import Creation
from DNA_project.management_commands.management_factory import Management
from DNA_project.manipulation_commands.manipulation_factory import Manipulation


# this factory creates command object according to the first word of tne command
# it is a singleton class because there is no need of more than one object of the class
class Factory:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Factory.__instance:
            Factory.__instance = object.__new__(cls)
        return Factory.__instance

    def __init__(self):
        # every group of commands has a factory class of its type
        self.command_type = {
            "new": Creation,
            "load": Creation,
            "dup": Creation,
            "slice": Manipulation,
            "concat": Manipulation,
            "del": Management,
            "save": Management,
            "find": Analysis,
            "findall": Analysis,
            "len": Analysis,
            "count": Analysis,
            "batch": BatchFactory,
            "batchlist": BatchFactory,
            "batchshow": BatchFactory,
            "batchsave": BatchFactory,
            "batchload": BatchFactory,
        }

    # gets a command and creates an object according to the dictionary
    def execute_command(self, command):
        command_list = command.split(' ')
        if command_list[0] not in self.command_type.keys():
            raise Exception("invalid command")
        command_to_exe = self.command_type[command_list[0]](command)
        return command_to_exe
