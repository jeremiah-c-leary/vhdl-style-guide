
from vsg import rule
from vsg import check
from vsg import fix

from vsg.rules import line_below_rule

class rule_030(line_below_rule):
    '''
    If rule 030 checks for a blank line after the "end if" keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'if', '030', 'isLastEndIf')
        self.solution = 'Add a blank line after the "end if"'
