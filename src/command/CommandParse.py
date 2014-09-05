from collections import namedtuple

class OutputType(object):
    Console = 0
    File = 1

ParseCommandResult = namedtuple('ParseCommandResult', 'command, args, output_type, output_name')

def parse_command(input):
    pass