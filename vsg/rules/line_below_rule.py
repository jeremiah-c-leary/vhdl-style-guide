
from vsg import fix
from vsg import check
from vsg import rule


class line_below_rule(rule.rule):
    '''
    Checks for blank lines below a line and will insert a blank line if one does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None):
        rule.rule.__init__(self, name, identifier)
        self.solution = 'Insert blank line below.'
        self.phase = 3
        self.condition = sTrigger

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.condition]:
            check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            fix.insert_blank_line_below(self, oFile, dViolation['lineNumber'])
