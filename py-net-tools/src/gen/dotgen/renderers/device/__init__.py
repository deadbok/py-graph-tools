# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------
from dotgen.renderers.device.client import Client
from dotgen.renderers.device.router import Router
from dotgen.renderers.device.server import Server
from dotgen.renderers.device.switch import Switch
from base.netobjbase import NetObjBase
from dotgen.exceptions import NoNameException
from dotgen.exceptions import NoRendererException
from dotgen.exceptions import NoDeviceDataException
import ipaddress

# Add new renders here.
renderers = [Router(), Client(), Server(), Switch()]

class Device(NetObjBase):
    def __init__(self, type, data):
        """
        Construct a base object for class graph objects.

        :param name: Name of the object. 
        """
        self.intefaces = []
        self.ports = []
        if data is None:
            raise NoDeviceDataException

        if 'name' not in data.keys():
            raise NoNameException(type)

        super().__init__(data['name'])
        print('New device: {}.'.format(self.name))

        self.type = type.lower()

        self.renderer = None

        for renderer in renderers:
            if renderer.isType(self.type):
                print(' Device renderer: {}.'.format(self.type))
                self.renderer = renderer

        if self.renderer is None:
            raise NoRendererException(self.name)

        self.parseInterfaces(data)

    def parseInterfaces(self, data):
        if 'interfaces' not in data.keys():
            return
        self.interfaces = data['interfaces']

    def parsePorts(self, data):
        if 'ports' not in data.keys():
            return
        self.ports = data['ports']


    def __str__(self):
        """
        Overwrite this class with a function that outputs the dot representation
        of the object.

        :return: String in dot format. 
        """
        ret = '"{}" '.format(self.name) + str(self.renderer) + ';'
        return ret
