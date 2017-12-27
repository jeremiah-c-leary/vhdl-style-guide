
from vsg import rule
from vsg import check
from vsg import fix


class indent_rule(rule.rule):
    '''
    Checks for and fixes indent violations.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    sUnless : string
       If set, will not check if attribute matches.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, sUnless=None):
        rule.rule.__init__(self, name, identifier)
        self.solution = 'Invalid indentation.'
        self.phase = 4
        self.sTrigger = sTrigger
        self.sUnless = sUnless

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if self.sUnless:
                if oLine.__dict__[self.sTrigger] and not oLine.__dict__[self.sUnless]:
                    check.indent(self, oLine, iLineNumber)
            elif oLine.__dict__[self.sTrigger]:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
