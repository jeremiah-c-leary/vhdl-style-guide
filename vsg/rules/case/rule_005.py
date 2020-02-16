
from vsg import rule
from vsg import fix
from vsg import check

from vsg.rules import single_space_before_rule

class rule_005(single_space_before_rule):
    '''Case rule 005 checks for a single space before the "=>" keyword.'''

    def __init__(self):
        single_space_before_rule.__init__(self, 'case', '005', 'isCaseWhenEnd', '=>')
        self.solution = 'Ensure a single space exists before the "=>" keyword.'
