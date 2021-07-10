from DNA_project.new import New
from DNA_project.database import DataBase


class Dup:
    __num = 1
    database = DataBase()

    def __init__(self, data):
        if data[0][0] == "#":
            self.seq_name = Dup.database.get_name_by_id(int(data[0][1:]))
        elif data[0][0] == "@":
            self.seq_name = (data[0][1:])
        else:
            raise Exception("the sequence name must come after a @ and the seq_id after a #")
        self.new_name = data[1]
        if not self.new_name:
            if Dup.database.does_name_exist(self.seq_name):
                self.new_name = self.seq_name + '_' + str(Dup.__num)
                Dup.__num += 1
                while Dup.database.does_name_exist(self.new_name):
                    self.new_name = 'seq' + str(Dup.__num)
                    Dup.__num += 1
            else:
                raise Exception("the sequence does not exist")

    def execute(self):
        seq = Dup.database.get_seq_by_name(self.seq_name)
        new = New([seq, '@' + self.new_name])
        new.execute()

