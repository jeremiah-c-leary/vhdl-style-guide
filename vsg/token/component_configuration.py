
from vsg import parser


class for_keyword(parser.keyword):
    '''
    unique_id = component_configuration : for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class binding_indication_semicolon(parser.semicolon):
    '''
    unique_id = component_configuration : binding_indication_semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class end_keyword(parser.keyword):
    '''
    unique_id = component_configuration : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_for_keyword(parser.keyword):
    '''
    unique_id = component_configuration : end_for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = component_configuration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
