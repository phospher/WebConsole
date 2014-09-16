import os
from command import DynamicObject
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class CommandConfigurationManager(object):
    config_object = None
    config_timestamp = None
    file_name = 'CommandConfiguration.xml'
    
    def __init__(self, file_path):
        assert os.path.isdir(file_path)
        self.file_full_path = os.path.join(file_path, CommandConfigurationManager.file_name)
        if self._need_refresh():
            self._read_config_from_file()
    
    def _need_refresh(self):
        return CommandConfigurationManager.config_object is None or os.path.getmtime(self.file_full_path) > CommandConfigurationManager.config_timestamp
    
    def _read_config_from_file(self):
        root = ET.parse(self.file_full_path)
        result = []
        for item in root.iter('command'):
            result.append(DynamicObject(command=item.get('command', None), callable_object=item.get('callableObject', None)))
        CommandConfigurationManager.config_timestamp = os.path.getmtime(self.file_full_path)
        CommandConfigurationManager.config_object = result
        return result

    def get_callable_object(self, command):
        config = [x for x in CommandConfigurationManager.config_object if x.command == command]
        if len(config) == 0:
            return None
        else:
            return config[0]
