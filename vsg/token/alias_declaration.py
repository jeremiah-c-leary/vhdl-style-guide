
from vsg import parser


class alias_keyword(parser.keyword):
    '''
    unique_id = alias_declaration : alias_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class alias_designator(parser.designator):
    '''
    unique_id = alias_declaration : alias_designator
    '''

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = alias_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class is_keyword(parser.keyword):
    '''
    unique_id = alias_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = alias_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class name(parser.name):
    '''
    unique_id = alias_declaration : name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
