
from vsg import rule
from vsg import check
from vsg import fix


class no_space_after_rule(rule.rule):
    '''
    No space after rule checks for spaces after a user specified keyword.
    '''

    def __init__(self, sName=None, sIdentifier=None, sWord=None, sTrigger=None):
        rule.rule.__init__(self, sName, sIdentifier)
        self.phase = 2
        self.sTrigger = sTrigger
        self.sWord = sWord
        self.identifier = sIdentifier
        self.solution = None

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_no_space_after(self, self.sWord, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_no_space_after_word(self, oLine, self.sWord)
