
from vsg import parser


class with_keyword(parser.keyword):
    '''
    unique_id = selected_waveform_assignment : with_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class select_keyword(parser.keyword):
    '''
    unique_id = selected_waveform_assignment : select_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class question_mark(parser.question_mark):
    '''
    unique_id = selected_waveform_assignment : question_mark
    '''

    def __init__(self, sString='?'):
        parser.question_mark.__init__(self)


class target(parser.target):
    '''
    unique_id = selected_waveform_assignment : target
    '''

    def __init__(self, sString):
        parser.target.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = selected_waveform_assignment : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = selected_waveform_assignment : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
