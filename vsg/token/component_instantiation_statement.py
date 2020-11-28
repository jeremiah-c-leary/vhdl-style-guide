
from vsg import parser


class instantiation_label(parser.label):
    '''
    unique_id = component_instantiation_statement : instantiation_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = component_instantiation_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = component_instantiation_statement : semicolon
    '''

    def __init__(self, sString=None):
        parser.semicolon.__init__(self)
