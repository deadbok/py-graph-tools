# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------

class NetObjBase:
    def __init__(self, name = ''):
        """
        Construct a base object for class graph objects.
        
        :param name: Name of the object. 
        """
        self.name = name

    def __str__():
        """
        Overwrite this class with a function that outputs the dot representation
        of the object.
        
        :return: String in dot format. 
        """
        return 'Not implemented'
