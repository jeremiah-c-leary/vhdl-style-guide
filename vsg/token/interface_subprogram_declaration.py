
from vsg import parser


class is_keyword(parser.keyword):
    '''
    unique_id = interface_subprogram_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

