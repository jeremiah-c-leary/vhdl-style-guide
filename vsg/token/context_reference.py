
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = context_reference : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class library_name(parser.selected_name):
    '''
    unique_id = context_reference : library_name
    '''

    def __init__(self, sString):
        parser.selected_name.__init__(self, sString)


class context_name(parser.selected_name):
    '''
    unique_id = context_reference : context_name
    '''

    def __init__(self, sString):
        parser.selected_name.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = context_reference : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class dot(parser.dot):
    '''
    unique_id = context_reference : dot
    '''

    def __init__(self, sString='.'):
        parser.dot.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = context_reference : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
