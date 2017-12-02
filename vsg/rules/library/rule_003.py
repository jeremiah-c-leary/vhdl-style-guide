
from vsg.rules import line_above_rule


class rule_003(line_above_rule):
    '''
    Library rule 003 checks for a blank line above the library keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self)
        self.name = 'library'
        self.identifier = '003'
        self.condition = 'isLibrary'
