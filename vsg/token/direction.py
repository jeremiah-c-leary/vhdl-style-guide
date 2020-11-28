
from vsg import parser


class to(parser.keyword):
    '''
    unique_id = direction : to
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class downto(parser.keyword):
    '''
    unique_id = direction : downto
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
