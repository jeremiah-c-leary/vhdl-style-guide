
from vsg import parser


class architecture_keyword(parser.keyword):
    '''
    unique_id = architecture_body : architecture_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = architecture_body : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class of_keyword(parser.keyword):
    '''
    unique_id = architecture_body : of_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class entity_name(parser.name):
    '''
    unique_id = architecture_body : entity_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = architecture_body : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = architecture_body : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = architecture_body : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_architecture_keyword(parser.keyword):
    '''
    unique_id = architecture_body : end_architecture_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class architecture_simple_name(parser.simple_name):
    '''
    unique_id = architecture_body : architecture_simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = architecture_body : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
