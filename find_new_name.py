from DNA_project.database import DataBase


def find_name_suffix(orig_name, suf):
    num = 1
    database = DataBase()
    new_name = orig_name + '_' + str(num)
    num += 1
    while database.does_name_exist(new_name):
        new_name = 'seq' + str(num)
        num += 1


