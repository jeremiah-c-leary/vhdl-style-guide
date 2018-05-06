
from vsg import rule
from vsg import fix
from vsg import check
from vsg import utilities


class uppercase_word_rule(rule.rule):
    '''
    Checks for and fixes uppercase violations.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    iIndex : integer
       Which word in the string to uppercase.
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
                sWord = utilities.remove_parenthesis_from_word(oLine.line.split()[self.iIndex])
                check.is_uppercase(self, sWord, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[self.iIndex])
