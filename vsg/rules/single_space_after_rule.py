
from vsg import rule
from vsg import check
from vsg import fix


class single_space_after_rule(rule.rule):
    '''
    Checks for and fixes none or multiple spaces after a word.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    sWord : string
       The word to check for a single space after.

    Attributes
    ----------

    self.phase : integer = 2
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, sWord=None):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.sTrigger = sTrigger
        self.sWord = sWord
        self.phase = 2
        self.solution = None

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_single_space_after(self, self.sWord, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_after_word(self, oLine, self.sWord)
