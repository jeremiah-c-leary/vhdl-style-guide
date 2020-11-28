
from vsg import parser


class others_keyword(parser.keyword):
    '''
    unique_id = entity_name_list : others_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class all_keyword(parser.keyword):
    '''
    unique_id = entity_name_list : all_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = entity_name_list : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)
