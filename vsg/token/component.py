
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = component : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = component : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = component : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = component : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_component_keyword(parser.keyword):
    '''
    unique_id = component : end_component_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class simple_name(parser.simple_name):
    '''
    unique_id = component : simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = component : semicolon
    '''

    def __init__(self, sString):
        parser.semicolon.__init__(self)
