
from vsg import rule
from vsg import fix
from vsg import check


class lowercase_word_rule(rule.rule):
    '''
    Checks for and fixes lowercase violations.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    iIndex : integer
       Which word in the string to lowercase.
    '''

    def __init__(self, name, identifier, sTrigger, iIndex):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.solution = None
        self.sTrigger = sTrigger
        self.iIndex = iIndex

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_lowercase(self, oLine.line.split()[self.iIndex], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[self.iIndex])
