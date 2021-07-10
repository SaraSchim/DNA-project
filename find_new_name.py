from DNA_project.database import DataBase


def find_new_name(orig_name, suf):
    num = 1
    database = DataBase()
    new_name = orig_name + suf + str(num)
    num += 1
    while database.does_name_exist(new_name):
        new_name = orig_name + suf + str(num)
        num += 1
    return new_name


# def orig_name_or_new(orig_name, name):
#     if name == "@@":
#         return '@' + find_new_name(orig_name, '_s')
#     if name[0] == '@':
#         return name
#     raise Exception("invalid new name! the name must begin with a @")
