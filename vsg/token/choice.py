
from vsg import parser


class others_keyword(parser.keyword):
    '''
    unique_id = choice : others_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
