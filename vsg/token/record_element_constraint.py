
from vsg import parser


class record_element_simple_name(parser.name):
    '''
    unique_id = record_element_constraint : record_element_simple_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
