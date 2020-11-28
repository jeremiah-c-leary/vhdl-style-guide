
from vsg import parser


class range_keyword(parser.keyword):
    '''
    unique_id = range_constraint : range_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
