
from vsg import parser


class for_keyword(parser.keyword):
    '''
    unique_id = simple_configuration_specification : for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = simple_configuration_specification : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_for_keyword(parser.keyword):
    '''
    unique_id = simple_configuration_specification : end_for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = simple_configuration_specification : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
