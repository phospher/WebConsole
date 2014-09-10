import os
import 
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class CommandConfigurationManager(object):
    config_object = None
    file_name = 'CommandConfiguration.xml'
    
    def __init__(self, file_path):
        assert os.path.isdir(file_path)
        self.file_dir_path = file_path
        if self._need_refresh():
            pass
    
    def _need_refresh(self):
        if CommandConfigurationManager.config_object is None:
            return True
        else:
            return False
    
    def read_config_from_file(self):
       root = ET.parse(os.path.join(self.file_dir_path, CommandConfigurationManager.file_name))
       result=[]
       for item in root.iter('command'):
           pass
