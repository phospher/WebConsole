class DynamicObject(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value