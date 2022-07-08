
from vsg import parser


class type_mark(parser.name):
    '''
    unique_id = subtype_indication : type_mark
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
