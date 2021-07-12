from DNA_project.cli.batch.run import Run
from DNA_project.cli.factory import Factory


def Cmd():
    factory = Factory()
    while True:
        command = input("> cmd >>> ")
        if command[:3] == 'run':
            try:
                command_to_exe = Run(command.split(" ")[1])
            except IndexError:
                raise Exception("invalid command")
        else:
            command_to_exe = factory.execute_command(command)
        command_to_exe.execute()
