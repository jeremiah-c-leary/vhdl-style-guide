
from vsg.rules import line_above_rule


class rule_004(line_above_rule):
    '''
    Instantiation rule 004 checks for a blank line above the instantiation
    declaration.
    '''

    def __init__(self):
        line_above_rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '004'
        self.condition = 'isInstantiationDeclaration'
