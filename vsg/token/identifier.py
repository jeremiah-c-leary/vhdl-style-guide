
from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = identifier : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)
