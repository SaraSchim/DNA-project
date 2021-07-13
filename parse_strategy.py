from DNA_project.database import DataBase


# this class is a strategy class that gets a parse function according to the command that creates it
# parses the command according to the type of the command
class Parse:
    def __init__(self, command, parse_strategy):
        self.command = command
        self.command_list = []
        self.parse_strategy = parse_strategy

    def parse_command(self):
        self.command_list = self.parse_strategy(self)


# each of the following functions parses a different type of commands with its specific rules:

# parse function for the creation commands
def creation_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    if len(command_list) == 2:
        command_list.append(None)
    elif len(command_list) < 2:
        raise Exception("invalid number of arguments")
    return command_list


# parse function for the manipulation commands
def manipulation_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    try:
        if command_list[-2] == ":":
            command_list.pop(-2)
        else:
            command_list.append(None)
    except IndexError:
        raise Exception("invalid number of arguments")
    return command_list


# parse function for the management commands
def management_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    if len(command_list) < 2 or len(command_list) > 3:
        raise Exception("invalid number of arguments")
    return command_list


# parse function for the analysis commands
def analysis_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    database = DataBase()
    if len(command_list) < 2 or len(command_list) > 3:
        raise Exception("invalid number of arguments")
    command_list[1] = database.get_seq_by_name(database.get_name_by_name_or_id(command_list[1]))
    try:
        if command_list[2][0] in ['@', '#']:
            command_list[2] = database.get_seq_by_name(database.get_name_by_name_or_id(command_list[2]))
    except IndexError:
        pass
    return command_list


# parse function for the batch commands
def batch_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    if len(command_list) == 1:
        command_list.append(None)
    if ':' in command_list:
        if len(command_list) != 4:
            raise Exception("invalid number of arguments")
        command_list.remove(":")
        return command_list
    if len(command_list) != 2:
        raise Exception("invalid number of arguments")
    return command_list
