from DNA_project.database import DataBase


#  shows the content of that batch
class BatchShow:
    database = DataBase()

    def __init__(self, data):
        if data[0][0] != '@':
            raise Exception("invalid batch name")
        self.batch_name = data[0][1:]

    def execute(self):
        print(BatchShow.database.get_batch_content(self.batch_name))
