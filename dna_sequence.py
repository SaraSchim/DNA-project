import re


class DnaSequence:

    def __init__(self, string):
        if not bool(re.match('^[ACTGactg]+$', string)):
            raise Exception("invalid string! the string must contain only the letters: A,C,T,G,a,c,t,g")
        self.string = string

    def insert(self, value, index):
        if value not in 'ACTGactg':
            raise Exception("invalid value! the value must be one of the letters: A,C,T,G,a,c,t,g")
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
