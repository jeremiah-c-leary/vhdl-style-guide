
from vsg import parser


class when_keyword(parser.keyword):
    '''
    unique_id = selected_expressions : when_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = selected_expressions : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self, sString)
