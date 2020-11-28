
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = entity : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = entity : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = entity : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = entity : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = entity : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_entity_keyword(parser.keyword):
    '''
    unique_id = entity : end_entity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class simple_name(parser.simple_name):
    '''
    unique_id = entity : simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = entity : semicolon
    '''

    def __init__(self):
        parser.semicolon.__init__(self)
