
from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = parameter_specification : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class in_keyword(parser.keyword):
    '''
    unique_id = parameter_specification : in_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
