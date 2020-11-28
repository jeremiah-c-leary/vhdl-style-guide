
from vsg import parser


class vhdl_range(parser.item):
    '''
    unique_id = vhdl_range : vhdl_range
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)
