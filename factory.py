from DNA_project.dup import Dup
from DNA_project.load import Load
from DNA_project.new import New


class CreatorCommand:
    def __init__(self):
        """Factory Method"""
        self.commands = {
            "new": New,
            "load": Load,
            "dup": Dup,
        }

    def execute_command(self, command):
        return self.commands[command]()
