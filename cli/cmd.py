from DNA_project.cli.batch.run import Run
from DNA_project.cli.factory import Factory


# the cmd gets commands from the user and executes them
# each command has an execute function
def Cmd():
    factory = Factory()
    while True:
        command = input("> cmd >>> ")
        # in order to avoid circular imports error I checked here the case of "run" command
        if command[:3] == 'run':
            try:
                command_to_exe = Run(command.split(" ")[1])
            except IndexError:
                raise Exception("invalid command")
        else:
            command_to_exe = factory.execute_command(command)   # create the command object
        command_to_exe.execute()    # execute the command
