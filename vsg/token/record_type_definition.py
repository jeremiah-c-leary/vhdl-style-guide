
from vsg import parser


class record_keyword(parser.keyword):
    '''
    unique_id = record_type_definition : record_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = record_type_definition : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_record_keyword(parser.keyword):
    '''
    unique_id = record_type_definition : end_record_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class record_type_simple_name(parser.simple_name):
    '''
    unique_id = record_type_definition : record_type_simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)
