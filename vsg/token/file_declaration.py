
from vsg import parser


class file_keyword(parser.keyword):
    '''
    unique_id = file_declaration : file_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = file_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = file_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class keyword(parser.keyword):
    '''
    unique_id = file_declaration : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = file_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = file_declaration : comma
    '''

    def __init__(self):
        parser.comma.__init__(self)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = file_declaration : subtype_indication
    '''

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class open_keyword(parser.keyword):
    '''
    unique_id = file_declaration : open_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_kind_expression(parser.expression):
    '''
    unique_id = file_declaration : open_kind_expression
    '''

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = file_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class logical_name(parser.logical_name):
    '''
    unique_id = file_declaration : logical_name
    '''

    def __init__(self, sString):
        parser.logical_name.__init__(self, sString)
