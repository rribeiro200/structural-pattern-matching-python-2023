def execute_command(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list:
            for directory in directories:
                print('$ listing files from: ', directory)
            print(f'{the_command=}, {the_list=}')

        case ['cd' | 'change', path]:
            print('$ changing directory to: ', path)
        
        case _:
            print('$ command not implemented')

execute_command('ls /home/luiz')


def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            print('DEU MATCH!')
            for directory in command['directories']:
                print(command['directories'])
                print(directory)

        case _:
            print('NÃO DEU MATCH')

execute_command({'command': 'ls', 'directories': ['/users']})