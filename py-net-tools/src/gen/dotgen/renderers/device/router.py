# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------

from dotgen.renderers.renderbase import RenderBase

class Router(RenderBase):
    def __init__(self):
        self.type='router'

    def __str__(self):
        """
        Overwrite this class with a function that outputs the dot representation
        of the object.

        :return: String in dot format. 
        """
        ret = "[shape=circle]"
        return ret


