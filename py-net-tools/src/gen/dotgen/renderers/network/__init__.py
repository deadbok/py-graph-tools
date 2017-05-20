# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------
from base.netobjbase import NetObjBase
from dotgen.exceptions import NoNameException
import ipaddress


class Network(NetObjBase):
    def __init__(self, name, network):
        """
        Construct a base object for class graph objects.

        :param name: Name of the object. 
        """
        if name == '':
            raise NoNameException('Network')

        super().__init__(name)
        print('New network: {}.'.format(self.name))

        self.network = ipaddress.ip_network(network)

    def __str__(self):
        """
        Overwrite this class with a function that outputs the dot representation
        of the object.

        :return: String in dot format. 
        """
        ret = '"{}" '.format(self.name) + '[shape=circle];'
        return ret
