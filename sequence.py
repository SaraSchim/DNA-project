from DNA_project.dna_sequence import DnaSequence


class Sequence:
    def __init__(self, dna, name=None):
        self.dna = DnaSequence(dna)
        if name:
            self. name = name

