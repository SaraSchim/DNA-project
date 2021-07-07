from DNA_project.factory import Factory


def main():
    factory = Factory()
    while True:
        command = input("> cmd >>> ")
        factory.execute_command(command)


if __name__ == '__main__':
    main()
