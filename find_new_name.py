from DNA_project.database import DataBase


# this function is called whenever the user doesn't send a name of the new seq to create
# the function gets the origin name and the suffix that should be in the end of the name
# the function finds the number that is suppose to be in the end of the name
# the function makes sure that the name does not exist in the DB
def find_new_name(orig_name, suf):
    num = 1
    database = DataBase()
    new_name = orig_name + suf + str(num)
    num += 1
    while database.does_name_exist(new_name):
        new_name = orig_name + suf + str(num)
        num += 1
    return new_name
