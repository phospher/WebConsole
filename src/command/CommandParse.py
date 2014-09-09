from collections import namedtuple

class OutputType(object):
    Console = 0
    File = 1

class ParseCommandResult(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value

def _parse_command(command):
    command_array = command.split(' ')
    if len(command_array) == 0:
        return ('', [])
    else:
        args = command_array[1:]
        return (command_array[0], args)

def parse_input(input):
    input_strip = input.strip()
    if len(input_strip) == 0:
        return ParseCommandResult(command='', args=[], output_type=OutputType.Console, output_name='')
    else:
        input_array = input_strip.split('>')
        command_result = _parse_command(input_array[0].strip())
        result = ParseCommandResult(command=command_result[0], args=command_result[1])
        if len(input_array) >= 2 and input_array[1].strip() != '':
            result.output_type = OutputType.File
            result.output_name = input_array[1].strip()
        else:
            result.output_type = OutputType.Console
            result.output_name = ''
        return result
