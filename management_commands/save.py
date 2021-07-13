from DNA_project.database import DataBase


# saves the seq into a file
class Save:
    database = DataBase()

    # data = [<seq>, [<filename>]]
    def __init__(self, data):
        self.seq_name = Save.database.get_name_by_name_or_id(data[0])
        if len(data) == 1:
            self.file_name = self.seq_name + '.rawdna'
        else:
            self.file_name = data[1] + '.rawdna'
        self.seq = Save.database.get_seq_by_name(self.seq_name)

    def execute(self):
        with open('seq_files/'+self.file_name, 'w') as file:
            file.write(self.seq)
            print("seq {} saved!".format(self.seq_name))
