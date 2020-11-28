
from vsg import parser


class comma(parser.comma):
    '''
    unique_id = waveform : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class unaffected_keyword(parser.keyword):
    '''
    unique_id = waveform : unaffected_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
