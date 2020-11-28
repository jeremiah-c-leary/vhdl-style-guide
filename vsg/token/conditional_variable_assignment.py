
from vsg import parser


class target(parser.target):
    '''
    unique_id = conditional_variable_assignment : target
    '''

    def __init__(self, sString):
        parser.target.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = conditional_variable_assignment : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = conditional_variable_assignment : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
