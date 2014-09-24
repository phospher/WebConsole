import importlib, time, os
from command.CommandParse import OutputType

def _import_object(callable_object):
    module_name, obj_name = callable_object.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, obj_name)

def _generate_colsole_result(command_parse_result, command_result):
    return {'type':'CONSOLE', 'result':command_result}

def _generate_file_result(command_parse_result, command_resut):
    file_name = '%s_%d' % (command_parse_result.output_name, (time.time() * 100))
    file_path = os.path.join(os.getcwd(), 'DownloadFiles', file_name)
    with open(file_path) as result_file:
        result_file.write('>>')
        result_file.write(input)
        result_file.write('\n')
        result_file.write(command_resut)
    return {'type':'FILE', 'result':file_name}

GENERATE_COMMAND_RESULT = {
    OutputType.Console:_generate_colsole_result,
    OutputType.File:_generate_file_result
}

def run_callable_object(callable_object, args):
    try:
        obj = _import_object(callable_object)
        if callable(obj):
            command_result = obj(args)
        else:
            command_result = 'Error-Invalid Command'
    except ImportError:
        command_result = 'Error-Invalid Command'
    return command_result

def generate_command_result(command_parse_result, command_result):
    return GENERATE_COMMAND_RESULT[command_parse_result.output_type](command_parse_result, command_result)
