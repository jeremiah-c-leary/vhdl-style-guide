
from vsg import parser


class file_keyword(parser.keyword):
    '''
    unique_id = interface_file_declaration : file_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = interface_file_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = interface_file_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)
