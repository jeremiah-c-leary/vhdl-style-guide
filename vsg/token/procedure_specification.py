
from vsg import parser


class procedure_keyword(parser.keyword):
    '''
    unique_id = procedure_specification : procedure_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class designator(parser.designator):
    '''
    unique_id = procedure_specification : designator
    '''

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class parameter_keyword(parser.keyword):
    '''
    unique_id = procedure_specification : parameter_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = procedure_specification : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = procedure_specification : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
