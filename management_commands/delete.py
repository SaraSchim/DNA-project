from DNA_project.database import DataBase


# deletes the seq from the DB
class Delete:
    database = DataBase()

    # data = [<seq>]
    def __init__(self, data):
        if len(data) != 1:
            raise Exception("invalid number of arguments")
        self.seq_name = Delete.database.get_name_by_name_or_id(data[0])
        if not Delete.database.does_name_exist(self.seq_name):
            raise Exception("sequence does not exist")
        self.seq = Delete.database.get_seq_by_name(self.seq_name)

    def execute(self):
        confirm = input("Do you realy want to delete {}: {}?\nPlease confirm by 'Y' or 'y', or cancel by 'N' or "
                        "'n'.\n> confirm >> ".format(self.seq_name, self.seq))
        while confirm.lower() not in ['y', 'n']:
            confirm = input("You have typed an invalid response. Please either confirm by 'Y'/'y', or cancel by "
                            "'N'/'n'.\n > confirm >> ")
        if confirm.lower() == 'y':
            print("Deleted: ", end="")
            Delete.database.print_seq(self.seq_name)
            Delete.database.delete_seq(self.seq_name)
        else:
            print("delete canceled")
