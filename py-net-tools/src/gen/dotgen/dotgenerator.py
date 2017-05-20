# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------

from dotgen.exceptions import NoNameException
from dotgen.exceptions import NoDeviceDataException
from dotgen.renderers import Device
from dotgen.renderers import Network


class DotGenerator:
    title = 'Network diagram'

    def __init__(self, title_visible=False):
        """
        Constructor.
        
        :param title_visible: Show the title in the network diagram if True. 
        """
        self.title_visible = title_visible
        self.objects = []

    def addDevice(self, type, data):
        try:
            device = Device(type, data)
            self.objects.append(device)
        except NoNameException as nne:
            print('Warning: {}'.format(str(nne)))
        except NoDeviceDataException as ndde:
            print('Warning: {}'.format(str(ndde)))


    def addConnection(self, name, data):
        print('Add connection: {}.'.format(name))

    def addNetwork(self, name, network):
        try:
            network = Network(name, network)
            self.objects.append(network)
        except NoNameException as nne:
            print('Warning: {}'.format(str(nne)))
        except NoDeviceDataException as ndde:
            print('Warning: {}'.format(str(ndde)))

    def fromDict(self, network=None):
        if network is None:
            return False

        for key, value in network.items():
            if key == 'name':
                self.title = value
                print('Network name: {}'.format(self.title))
            elif key == 'networks':
                for name, network in value.items():
                    self.addNetwork(name, network)
            else:
                self.addDevice(key, value)

    def __str__(self):
        ret = 'graph "{}" '.format(self.title) + '{\n'

        for object in self.objects:
            ret += str(object) + '\n'
        ret += '}\n'

        return ret
