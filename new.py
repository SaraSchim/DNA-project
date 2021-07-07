from DNA_project.dna_sequence import DnaSequence
from DNA_project.seq_database import seq_DB_by_id, seq_DB_by_name


class New:
    __num = 1

    def __init__(self, data):
        try:
            seq = data[0]
        except:
            raise Exception("required arguments weren't  sent")
        try:
            if data[1][0] == '@':
                seq_name = data[1][1:]
            else:
                raise Exception("invalid input! the name must come after a @")
            if seq_DB_by_name.get(seq_name):
                raise Exception("sequence name already exists")
        except IndexError:
            seq_name = 'seq' + str(New.__num)
            New.__num += 1
            while seq_DB_by_name.get(seq_name):
                seq_name = 'seq' + str(New.__num)
                New.__num += 1
        sequence = DnaSequence(seq, seq_name)
        seq_id = sequence.get_seq_id()
        seq_DB_by_id.update({seq_id: (seq_name, seq)})
        seq_DB_by_name.update({seq_name: seq})
        if len(seq) > 40:
            seq = seq[:32] + '...' + seq[-3:]
        print("[" + str(seq_id) + "] " + seq_name + ": " + seq)
