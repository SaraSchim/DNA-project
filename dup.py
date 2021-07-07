from DNA_project.new import New
from DNA_project.seq_database import seq_DB_by_id, seq_DB_by_name


class Dup:
    __num = 1

    def __init__(self, data):
        try:
            if data[0][0] == "#":
                seq_name = seq_DB_by_id.get(int(data[0][1:]))[0]
            elif data[0][0] == "@":
                seq_name = (data[0][1:])
            else:
                raise Exception("the sequence name must come after a @ and the id after a #")
        except IndexError:
            raise Exception("required arguments weren't  sent")
        try:
            new_name = data[1]
        except:
            if seq_DB_by_name.get(seq_name):
                new_name = seq_name + '_' + str(Dup.__num)
                Dup.__num += 1
            else:
                raise Exception("the sequence does not exist")
        New([seq_DB_by_name.get(seq_name), '@' + new_name])
