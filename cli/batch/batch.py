from DNA_project.database import DataBase


# this is what happens when the user creates a batch
# the batch saves the commands (as strings) in a list
class Batch:
    database = DataBase()

    def __init__(self, data):
        if data[0] is None:
            raise Exception("invalid number of arguments")
        self.name = data[0]
        self.commands = []

    # the batch runs till the user puts in the "end" command
    def execute(self):
        command = input("> batch >>> ")
        while command != 'end':
            if command[:5] == 'batch':
                raise Exception("you cannot enter batch commands in batch mode!")
            self.commands.append(command)
            command = input("> batch >>> ")
        self.end()

    # when the user decides to end the batch - the list of the commands is saved in the DB
    def end(self):
        Batch.database.update_command(self.name, self.commands)
