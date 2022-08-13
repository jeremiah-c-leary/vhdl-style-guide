
from vsg import parser


class for_keyword(parser.keyword):
    '''
    unique_id = block_configuration : configuration_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = block_configuration : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_for_keyword(parser.keyword):
    '''
    unique_id = block_configuration : end_for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class unspecified(parser.name):
    '''
    unique_id = block_configuration : unspecified
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = block_configuration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
