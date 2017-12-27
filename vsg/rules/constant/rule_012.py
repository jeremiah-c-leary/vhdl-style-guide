
from vsg.rules import indent_rule


class rule_012(indent_rule):
    '''
    Constant rule 012 checks for the proper indentation of multiline constants.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'constant', '012', 'insideConstant', 'isConstant')
