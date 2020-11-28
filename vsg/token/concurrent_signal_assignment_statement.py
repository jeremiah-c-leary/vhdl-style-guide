
from vsg import parser


class postponed_keyword(parser.keyword):
    '''
    unique_id = concurrent_signal_assignment_statement : postponed_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class label_name(parser.label):
    '''
    unique_id = concurrent_signal_assignment_statement : label_name
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)

class label_colon(parser.colon):
    '''
    unique_id = concurrent_signal_assignment_statement : label_colon
    '''

    def __init__(self, sString=';'):
        parser.colon.__init__(self, sString)
