class DataBase(object):
    __instance = None
    seq_DB_by_id = dict()
    seq_DB_by_name = dict()

    def __new__(cls, *args, **kwargs):
        if not DataBase.__instance:
            DataBase.__instance = object.__new__(cls)
        return DataBase.__instance

    # def __init__(self):
        # self.seq_DB_by_id = dict()
        # self.seq_DB_by_name = dict()

    def add_seq(self, seq_id, name, seq):
        DataBase.seq_DB_by_id.update({seq_id: (name, seq)})
        DataBase.seq_DB_by_name.update({name: seq_id})

    def get_seq_by_id(self, seq_id):
        seq = DataBase.seq_DB_by_id.get(seq_id)[1]
        if seq:
            return seq
        raise Exception("sequence does not exist")

    def get_seq_by_name(self, name):
        seq_id = self.get_id_by_name(name)
        if not seq_id:
            raise Exception("sequence does not exist")
        seq = self.get_seq_by_id(seq_id)
        if seq:
            return seq
        raise Exception("sequence does not exist")

    def get_name_by_id(self, seq_id):
        try:
            name = DataBase.seq_DB_by_id.get(seq_id)[0]
            if name:
                return name
        except:
            raise Exception("sequence does not exist")

    def get_id_by_name(self, name):
        try:
            seq_id = DataBase.seq_DB_by_name.get(name)
            if seq_id:
                return seq_id
        except:
            raise Exception("sequence does not exist")

    def get_name_by_name_or_id(self, name_or_id):
        if name_or_id[0] == "#":
            return self.get_name_by_id(int(name_or_id[1:]))
        elif name_or_id[0] == "@":
            return name_or_id[1:]
        else:
            raise Exception("the sequence name must come after a @ and the seq_id after a #")

    def does_name_exist(self, name):
        if DataBase.seq_DB_by_name.get(name):
            return True
        return False

    def update_seq(self,name, new_seq):
        seq_id = self.get_id_by_name(name)
        DataBase.seq_DB_by_id[seq_id] = (name, new_seq)

    def delete_seq(self, name):
        try:
            seq_id = self.get_id_by_name(name)
            del self.seq_DB_by_name[name]
            del self.seq_DB_by_id[seq_id]
        except:
            raise Exception("sequence does not exist")

    def print_seq(self, name):
        if self.does_name_exist(name):
            seq_id = self.get_id_by_name(name)
            seq = self.get_seq_by_id(seq_id)
            print("[{}] {}: {}".format(seq_id, name, seq))
        else:
            raise Exception("sequence does not exist")


