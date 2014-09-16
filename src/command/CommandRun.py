import importlib
from command.CommandParse import OutputType 

def _import_object(callable_object):
    module_name, obj_name = callable_object.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, obj_name)

GENERATE_COMMAND_RESULT = {
    OutputType.Console:None,
    OutputType.File:None
}

def run_callable_object(callable_object, args, output_type):
    try:
        obj = _import_object(callable_object)
        if callable(obj):
            command_result = obj(args)
        else:
            command_result = 'Error-Invalid Command'
    except ImportError:
        command_result = 'Error-Invalid Command'
    return GENERATE_COMMAND_RESULT[output_type](command_result)