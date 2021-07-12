from DNA_project.database import DataBase


class BatchList:
    database = DataBase()

    def __init__(self, arg):
        pass

    def execute(self):
        print(BatchList.database.get_batch_names())
