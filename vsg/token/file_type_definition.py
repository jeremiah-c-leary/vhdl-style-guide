
from vsg import parser


class file_keyword(parser.keyword):
    '''
    unique_id = file_type_definition : file_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class of_keyword(parser.keyword):
    '''
    unique_id = file_type_definition : of_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
