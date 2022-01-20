
from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = secondary_unit_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class equal_sign(parser.item):
    '''
    unique_id = secondary_unit_declaration : equal_sign
    '''

    def __init__(self):
        parser.item.__init__(self, '=')


class physical_literal(parser.item):
    '''
    unique_id = secondary_unit_declaration : physical_literal
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = secondary_unit_declaration : semicolon
    '''

    def __init__(self):
        parser.semicolon.__init__(self)
