import re


class DnaSequence:

    def __init__(self, string):
        if bool(re.match('^[ACTG]+$', string)):
            self.string = string
        else:
            raise Exception("invalid string! the string must contain only the letters: A,C,T,G")

    def insert(self, value, index):
        self.string = self.string[0:index] + value + self.string[index:]

    def assignment(self, other):
        if type(other) == str:
            self.string = other
        elif type(other) == DnaSequence:
            self.string = other.string

    def __str__(self):
        return self.string

    def __eq__(self, other):
        return self.string == other.string

    def __nq__(self, other):
        return self.string != other.string

    def __getitem__(self, index):
        return self.string[index]

    def __len__(self):
        return len(self.string)
