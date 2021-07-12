from DNA_project.database import DataBase


class Batch:
    database = DataBase()

    def __init__(self, data):
        if data[0] is None:
            raise Exception("invalid number of arguments")
        self.name = data[0]
        self.commands = []

    def execute(self):
        command = input("> batch >>> ")
        while command != 'end':
            if command[:5] == 'batch':
                raise Exception("you cannot enter batch commands in batch mode!")
            self.commands.append(command)
            command = input("> batch >>> ")
        self.end()

    def end(self):
        Batch.database.update_command(self.name, self.commands)
