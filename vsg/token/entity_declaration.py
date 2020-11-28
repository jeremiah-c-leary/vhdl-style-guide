
from vsg import parser


class entity_keyword(parser.keyword):
    '''
    unique_id = entity_declaration : entity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = entity_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = entity_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = entity_declaration : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = entity_declaration : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_entity_keyword(parser.keyword):
    '''
    unique_id = entity_declaration : end_entity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class entity_simple_name(parser.simple_name):
    '''
    unique_id = entity_declaration : entity_simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = entity_declaration : semicolon
    '''

    def __init__(self, sString):
        parser.semicolon.__init__(self)
