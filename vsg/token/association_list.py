
from vsg import parser


class comma(parser.comma):
    '''
    unique_id = association_list : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)
