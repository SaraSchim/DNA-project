class Parse:
    def __init__(self, command, parse_strategy):
        self.command = command
        self.command_list = []
        self.parse_strategy = parse_strategy

    def parse_command(self):
        self.command_list = self.parse_strategy(self)


def creation_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    if len(command_list) == 2:
        command_list.append(None)
    elif len(command_list) < 2:
        raise Exception("invalid number of arguments")
    return command_list


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


def management_parse(command_to_parse):
    fixed_command = " ".join(command_to_parse.command.split())
    command_list = fixed_command.split(' ')
    if len(command_list) < 2 or len(command_list) > 3:
        raise Exception("invalid number of arguments")
    return command_list
