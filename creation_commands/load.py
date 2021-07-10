from DNA_project.creation_commands.new import New


class Load:
    def __init__(self, data):
        self.file_name = data[0]
        self.seq_name = data[1]
        if not self.seq_name:
            self.seq_name = self.file_name.split('.')[0]

    def execute(self):
        with open('seq_files/' + self.file_name) as file:
            seq = file.read()
            new = New([seq, '@' + self.seq_name])
            new.execute()
