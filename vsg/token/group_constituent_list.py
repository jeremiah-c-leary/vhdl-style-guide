
from vsg import parser


class comma(parser.comma):
    '''
    unique_id = group_constituent_list : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class group_constituent(parser.item):
    '''
    unique_id = group_constituent_list : group_constituent
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)

