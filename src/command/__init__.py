#from CommandParse import parse_input
import CommandParse
from Configurations import CommandConfigurationManager
import CommandRun

class DynamicObject(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value

def run_command(input, config_file_path):
    command_parse = CommandParse.parse_input(input)
    config_manager = CommandConfigurationManager(config_file_path)
    command_result = CommandRun.run_callable_object(config_manager.get_callable_object(command_parse.command), command_parse.args)
    return CommandRun.generate_command_result(command_parse, command_result)