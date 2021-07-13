from DNA_project.database import DataBase


# loads a list of commands from a file and saves it as a batch in the DB
class BatchLoad:
    database = DataBase()

    def __init__(self, data):
        self.file_name = data[0]
        try:
            if data[1][0] != '@':
                raise Exception("invalid batch name")
            self.batch_name = data[1][1:]
        except:
            self.batch_name = self.file_name.replace(".dnabatch", "")

    def execute(self):
        with open("cli/batch/batch_files/"+self.file_name, "r") as file:
            commands = file.read().splitlines()
            BatchLoad.database.update_command(self.batch_name, commands)


