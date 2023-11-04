
from vsg import parser


class when_keyword(parser.keyword):
    '''
    unique_id = conditional_waveforms : when_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class else_keyword(parser.keyword):
    '''
    unique_id = conditional_waveforms : else_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
