
from vsg import parser


class units_keyword(parser.keyword):
    '''
    unique_id = physical_type_definition : units_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = physical_type_definition : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_units_keyword(parser.keyword):
    '''
    unique_id = physical_type_definition : end_units_definition
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class simple_name(parser.simple_name):
    '''
    unique_id = physical_type_definition : simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)
