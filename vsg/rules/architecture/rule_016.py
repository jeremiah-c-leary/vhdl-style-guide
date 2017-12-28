
from vsg.rules import line_above_rule


class rule_016(line_above_rule):
    '''
    Architecture rule 016 checks for a blank line above the "begin" keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'architecture', '016', 'isArchitectureBegin')
