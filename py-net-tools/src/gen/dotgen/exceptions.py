class BaseException(Exception):
    pass

class NoNameException(BaseException):
    def __init__(self, type=None):
        if type is None:
            msg = 'Missing name.'
        else:
            msg = '{0} has no {1}.'.format(type, 'name')
        super(NoNameException, self).__init__(msg)

class NoDeviceDataException(BaseException):
    def __init__(self, name=None):
        if (name is None) or (type is None):
            msg = 'Missing data.'
        else:
            msg = '{0} "{1}" is empty.'.format('Device', name)
        super(NoDeviceDataException, self).__init__(msg)


class NoRendererException(BaseException):
    def __init___(self):
        super().__init__("Device has no renderer.}")
