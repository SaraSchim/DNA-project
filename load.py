from DNA_project.new import New


class Load:
    def __init__(self, data):
        try:
            file_name = data[0]
        except:
            raise Exception("required arguments weren't  sent")
        try:
            seq_name = data[1]
        except:
            seq_name = file_name.split('.')[0]
        with open('seq_files/'+file_name) as file:
            seq = file.read()
            print(seq)
            New([seq, '@'+seq_name])
