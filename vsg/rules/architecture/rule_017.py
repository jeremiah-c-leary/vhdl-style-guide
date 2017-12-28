
from vsg.rules import line_below_rule


class rule_017(line_below_rule):
    '''
    Architecture rule 017 checks for a blank line below the "begin" keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'architecture', '017', 'isArchitectureBegin')
