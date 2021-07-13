from DNA_project.creation_commands.new import New
from DNA_project.database import DataBase
from DNA_project.find_new_name import find_new_name


# concats sequences into the first seq or a new seq
class Concat:
    database = DataBase()

    # data = [<seq_1> <seq_2> ... <seq_n>  @<new_seq_name>|@@|None]
    def __init__(self, data):
        self.seq_names_list = [Concat.database.get_name_by_name_or_id(i) for i in data[:-1]]
        self.seq_list = [Concat.database.get_seq_by_name(i) for i in self.seq_names_list]
        self.concat_seq = "".join(self.seq_list)
        if data[-1] == "@@":
            if len(self.seq_names_list) <= 2:
                self.new_name = '@' + find_new_name("_".join(self.seq_names_list), '_c')
            else:
                self.new_name = '@' + find_new_name("conseq", '_')
        elif not data[-1] or data[-1][0] == '@':
            self.new_name = data[-1]
        else:
            raise Exception("invalid seq name")

    def execute(self):
        if self.new_name:
            new = New([self.concat_seq, self.new_name])
            new.execute()
        else:
            Concat.database.update_seq(self.seq_names_list[0], self.concat_seq)
            print("[{}] {}: {}".format(Concat.database.get_id_by_name(self.seq_names_list[0]), self.seq_names_list[0],
                                       self.concat_seq))
