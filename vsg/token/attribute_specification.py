
from vsg import parser


class attribute_keyword(parser.keyword):
    '''
    unique_id = attribute_specification : attribute_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class attribute_designator(parser.designator):
    '''
    unique_id = attribute_specification : attribute_designator
    '''

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class of_keyword(parser.keyword):
    '''
    unique_id = attribute_specification : of_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = attribute_specification : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = attribute_specification : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
