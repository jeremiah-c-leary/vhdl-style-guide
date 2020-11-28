
from vsg import parser


class comma(parser.comma):
    '''
    unique_id = identifier_list : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class identifier(parser.identifier):
    '''
    unique_id = identifier_list : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)
