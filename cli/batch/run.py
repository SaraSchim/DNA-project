from DNA_project.cli.factory import Factory
from DNA_project.database import DataBase


class Run:
    database = DataBase()

    def __init__(self, batch_name):
        if batch_name[0] != '@':
            raise Exception("invalid batch name")
        self.batch_name = batch_name[1:]
        self.commands_to_run = Run.database.batch_commands.get(self.batch_name)
        if not self.commands_to_run:
            raise Exception("batch does not exist")

    def execute(self):
        factory = Factory()
        for i in self.commands_to_run:
            command_to_exe = factory.execute_command(i)
            command_to_exe.execute()
