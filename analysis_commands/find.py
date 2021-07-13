from DNA_project.database import DataBase


# finds a sub-sequence within a sequence.
class Find:

    # data = [<seq_to_find_in>, <seq_to_be_found>]
    def __init__(self, data):
        self.seq_to_find_in = data[0]
        self.seq_to_be_found = data[1]

    def execute(self):
        index = self.seq_to_find_in.find(self.seq_to_be_found)
        print(index)
