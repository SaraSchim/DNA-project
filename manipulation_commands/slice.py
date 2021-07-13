from DNA_project.creation_commands.new import New
from DNA_project.database import DataBase
from DNA_project.find_new_name import find_new_name


# slices the seq from index to index
class Slice:
    database = DataBase()

    # data = [<seq>, <from_ind>, <to_ind>, @<new_seq_name>|@@|None]
    def __init__(self, data):
        if len(data) != 4:
            raise Exception("invalid number of arguments")
        self.seq_name = Slice.database.get_name_by_name_or_id(data[0])
        if not Slice.database.does_name_exist(self.seq_name):
            raise Exception("sequence does not exist")
        self.seq = Slice.database.get_seq_by_name(self.seq_name)
        if not (data[1].isnumeric() and data[2].isnumeric()):
            raise Exception("invalid input! the indexes must be numbers")
        self.from_ind = int(data[1])
        self.to_ind = int(data[2])
        if self.from_ind > self.to_ind or self.from_ind > len(self.seq):
            raise Exception("invalid indexes")
        self.sliced_seq = self.seq[self.from_ind:self.to_ind+1]
        self.new_name = data[3]
        if data[3] == "@@":
            self.new_name = '@' + find_new_name(self.seq_name, '_s')
        elif not data[3] or data[3][0] == '@':
            self.new_name = data[3]
        else:
            raise Exception("invalid seq name")
        if Slice.database.does_name_exist(self.new_name):
            raise Exception("sequence already exists")

    def execute(self):
        if self.new_name:
            new = New([self.sliced_seq, self.new_name])
            new.execute()
        else:
            Slice.database.update_seq(self.seq_name, self.sliced_seq)
            Slice.database.print_seq(self.seq_name)