
from vsg.rules import line_below_rule


class rule_018(line_below_rule):
    '''
    Component rule 018 checks for a blank line below the
    "end component" keywords.
    '''

    def __init__(self):
        line_below_rule.__init__(self)
        self.name = 'component'
        self.identifier = '018'
        self.condition = 'isComponentEnd'
