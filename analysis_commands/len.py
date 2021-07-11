class Len:

    # data = [<seq_to_find_in>, <seq_to_be_found>]
    def __init__(self, data):
        self.seq = data[0]

    def execute(self):
        print(len(self.seq))
