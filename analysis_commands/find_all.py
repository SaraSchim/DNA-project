import re


class FindAll:

    # data = [<seq_to_find_in>, <seq_to_be_found>]
    def __init__(self, data):
        self.seq_to_find_in = data[0]
        self.seq_to_be_found = data[1]

    def execute(self):
        indexes = [m.start() for m in re.finditer('(?={})'.format(self.seq_to_be_found), self.seq_to_find_in)]
        if not indexes:
            print(-1)
            return
        for i in indexes:
            print(i, end=" ")
        print()
