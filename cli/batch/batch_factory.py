from DNA_project.cli.batch.batch import Batch
from DNA_project.cli.batch.batch_list import BatchList
from DNA_project.cli.batch.batch_load import BatchLoad
from DNA_project.cli.batch.batch_save import BatchSave
from DNA_project.cli.batch.batch_show import BatchShow
from DNA_project.parse_strategy import Parse, batch_parse


# # a factory class for batch commands
class BatchFactory:
    def __init__(self, command):
        self.command = command
        self.commands = {
            "batch": Batch,
            "batchlist": BatchList,
            "batchshow": BatchShow,
            "batchsave": BatchSave,
            "batchload": BatchLoad
        }

    def execute(self):
        parser = Parse(self.command, batch_parse)       # parse function for the batch commands
        parser.parse_command()
        command_list = parser.command_list
        command_to_exe = self.commands[command_list[0]](command_list[1:])
        command_to_exe.execute()
