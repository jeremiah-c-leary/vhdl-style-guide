
from vsg import token
from vsg import violation

from vsg.rule_group import structure


class rule_001(structure.Rule):
    '''
    This rule checks for **with** statements.

    **Violation**

    .. code-block:: vhdl

       with buttons select

    **Fix**

    Refactor **with** statement into a process.
    '''

    def __init__(self):
        structure.Rule.__init__(self, name='with', identifier='001')
        self.solution = "Rewrite with as a process"
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([token.concurrent_selected_signal_assignment.with_keyword])

    def _analyze(self, lToi):
        for oToi in lToi:
            self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
