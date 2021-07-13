from DNA_project.creation_commands.new import New
from DNA_project.database import DataBase
from DNA_project.find_new_name import find_new_name


# duplicates a sequence
class Dup:
    database = DataBase()

    # data = [ <seq>, [@<new_seq_name>] ]
    def __init__(self, data):
        self.seq_name = Dup.database.get_name_by_name_or_id(data[0])
        if not Dup.database.does_name_exist(self.seq_name):
            raise Exception("the sequence does not exist")
        self.new_name = data[1]
        if not self.new_name:
            self.new_name = find_new_name(self.seq_name, '_')

    def execute(self):
        seq = Dup.database.get_seq_by_name(self.seq_name)
        new = New([seq, '@' + self.new_name])
        new.execute()

