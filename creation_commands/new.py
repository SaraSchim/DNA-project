from DNA_project.dna_sequence import DnaSequence
from DNA_project.database import DataBase


class New:
    __num = 1
    database = DataBase()

    def __init__(self, data):
        self.seq = data[0]
        try:
            if data[1][0] == '@':
                self.seq_name = data[1][1:]
            else:
                raise Exception("invalid input! the name must come after a @")
            if New.database.does_name_exist(self.seq_name):
                raise Exception("sequence name already exists")
        except TypeError:
            self.seq_name = 'seq' + str(New.__num)
            New.__num += 1
            while New.database.does_name_exist(self.seq_name):
                self.seq_name = 'seq' + str(New.__num)
                New.__num += 1

    def execute(self):
        sequence = DnaSequence(self.seq, self.seq_name)
        seq_id = sequence.get_seq_id()
        New.database.add_seq(seq_id, self.seq_name, self.seq)
        if len(self.seq) > 40:
            self.seq = self.seq[:32] + '...' + self.seq[-3:]
        print("[" + str(seq_id) + "] " + self.seq_name + ": " + self.seq)
