
from vsg.rules import line_above_rule


class rule_003(line_above_rule):
    '''
    Package rule 003 checks for a blank line above the package keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self)
        self.name = 'package'
        self.identifier = '003'
        self.condition = 'isPackageKeyword'
