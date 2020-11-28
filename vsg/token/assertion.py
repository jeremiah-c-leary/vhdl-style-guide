
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = assertion : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class condition(parser.condition):
    '''
    unique_id = assertion : condition
    '''

    def __init__(self, sString):
        parser.condition.__init__(self, sString)


class report_keyword(parser.keyword):
    '''
    unique_id = assertion : report_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class report_expression(parser.expression):
    '''
    unique_id = assertion : report_expression
    '''

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class severity_keyword(parser.keyword):
    '''
    unique_id = assertion : severity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class severity_expression(parser.expression):
    '''
    unique_id = assertion : severity_expression
    '''

    def __init__(self, sString):
        parser.expression.__init__(self, sString)
