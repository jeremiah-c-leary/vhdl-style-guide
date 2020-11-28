
from vsg import parser


class all_keyword(parser.keyword):
    '''
    unique_id = process_sensitivity_list : all_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
