class DnaSequence:
    __ids = 1

    def __init__(self, dna, name):
        for i in dna:
            if i not in "ACTGactg":
                raise Exception("invalid DNA! the DNA must contain only the letters: A,C,T,G,a,c,t,g")
        self.__dna = dna
        self.__id = DnaSequence.__ids
        self.__name = name
        DnaSequence.__ids += 1

    def get_name(self):
        return self.__name

    def get_seq_id(self):
        return self.__id

    def get_dna(self):
        return self.__dna

    def insert(self, value, index):
        if value not in 'ACTGactg':
            raise Exception("invalid value! the value must be one of the letters: A,C,T,G,a,c,t,g")
        self.__dna = self.__dna[0:index] + value + self.__dna[index:]

    def assignment(self, other):
        if type(other) == str:
            self.__dna = other
        elif type(other) == DnaSequence:
            self.__dna = other.__dna

    def __str__(self):
        return "[" + str(self.__id) + "] " + self.__name + ": " + self.__dna

    def __eq__(self, other):
        return self.__dna == other.__dna

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, index):
        return self.__dna[index]

    def __len__(self):
        return len(self.__dna)
