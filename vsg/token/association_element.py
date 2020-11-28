
from vsg import parser


class assignment(parser.item):
    '''
    unique_id = association_element : assignment
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class formal_part(parser.item):
    '''
    unique_id = association_element : formal_part
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class actual_part(parser.item):
    '''
    unique_id = association_element : actual_part
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)
