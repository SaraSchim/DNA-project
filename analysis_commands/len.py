# prints the length of the seq
class Len:

    def __init__(self, data):
        self.seq = data[0]

    def execute(self):
        print(len(self.seq))
