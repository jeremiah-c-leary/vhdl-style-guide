
from vsg import parser


class entity_tag(parser.identifier):
    '''
    unique_id = entity_designator : entity_tag
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)
