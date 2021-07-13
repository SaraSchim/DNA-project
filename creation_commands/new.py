from DNA_project.dna_sequence import DnaSequence
from DNA_project.database import DataBase
from DNA_project.find_new_name import find_new_name


# creates a new sequence and saves it in the database
class New:
    database = DataBase()

    # data = [<sequence>, [@<sequence_name>]]
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
            self.seq_name = find_new_name('seq', "")

    def execute(self):
        sequence = DnaSequence(self.seq, self.seq_name)
        seq_id = sequence.get_seq_id()
        New.database.add_seq(seq_id, self.seq_name, self.seq)
        if len(self.seq) > 40:
            self.seq = self.seq[:32] + '...' + self.seq[-3:]
        print(sequence)

