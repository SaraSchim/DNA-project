from DNA_project.database import DataBase


# saves the batch's list of commands in a file
class BatchSave:
    database = DataBase()

    def __init__(self, data):
        if data[0][0] != '@':
            raise Exception("invalid batch name")
        self.batch_name = data[0][1:]
        try:
            self.file_name = data[1]
        except:
            self.file_name = self.batch_name + ".dnabatch"

    def execute(self):
        with open("cli/batch/batch_files/"+self.file_name, "w") as file:
            data = BatchSave.database.get_batch_content(self.batch_name)
            for line in data:
                file.write(line+'\n')

