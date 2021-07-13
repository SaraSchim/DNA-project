import re


# counts the number of instances of the sub-sequence within the larger sequence.
class Count:

    # data = [<seq_to_find_in>, <seq_to_be_found>]
    def __init__(self, data):
        self.seq_to_find_in = data[0]
        self.seq_to_be_found = data[1]

    def execute(self):
        print(len(re.findall('(?={})'.format(self.seq_to_be_found), self.seq_to_find_in)))
