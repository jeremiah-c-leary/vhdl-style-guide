
from vsg import parser


class configuration_keyword(parser.keyword):
    '''
    unique_id = configuration_body : configuration_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = configuration_body : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class of_keyword(parser.keyword):
    '''
    unique_id = configuration_body : of_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class entity_name(parser.name):
    '''
    unique_id = configuration_body : entity_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = configuration_body : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = configuration_body : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_configuration_keyword(parser.keyword):
    '''
    unique_id = configuration_body : end_configuration_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class configuration_simple_name(parser.simple_name):
    '''
    unique_id = configuration_body : configuration_simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = configuration_body : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
