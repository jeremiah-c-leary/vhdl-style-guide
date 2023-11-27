
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = assertion : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class report_keyword(parser.keyword):
    '''
    unique_id = assertion : report_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class severity_keyword(parser.keyword):
    '''
    unique_id = assertion : severity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
